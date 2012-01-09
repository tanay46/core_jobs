from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages

from apps.jobs.models import *
from apps.jobs.forms import *

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def post_job(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                user=request.user,
                email=form.cleaned_data['email'],
                description=form.cleaned_data['description'],
                expires_on=form.cleaned_data['expires_on']
            )
            messages.add_message(request, messages.SUCCESS,
                u"Successfully posted."
            )
            return HttpResponseRedirect('/jobs/')
        else:
            messages.add_message(request, messages.ERROR,
                u"Something went wrong."
            )
        return HttpResponseRedirect('/jobs/post/')
    else:
        form = PostForm()
        vars = RequestContext(request,
                {'form': form}
        )
        return render_to_response('jobs/post_job.html', vars)

def view_tag(request):
    if request.is_ajax():
        if request.GET.has_key('q'):
            term = request.GET['q']
            return _render_for_tag(request, tag=term)
        else:
            return _render_for_tag(request)
    else:
        return HttpResponseRedirect('/jobs/')

def _render_for_tag(request, tag=None):
    if tag is not None:
        posts = Post.objects.filter(tags__name__in=[tag])
    else:
        posts = Post.objects.all()
    vars = RequestContext(request,
            {'posts': posts}
    )
    return render_to_response('jobs/posts.html', vars)

def main(request):
    posts = Post.objects.all()
    vars = RequestContext(request,
            {'posts': posts}
    )
    return render_to_response('jobs/main.html', vars)