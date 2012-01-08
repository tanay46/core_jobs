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
        variables = RequestContext(request,
                {'form': form}
        )
        return render_to_response('jobs/post_job.html', variables)

def main(request):
    posts = Post.objects.all()
    variables = RequestContext(request,
            {'posts': posts}
    )
    return render_to_response('jobs/main.html', variables)