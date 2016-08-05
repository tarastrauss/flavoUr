from django.shortcuts import get_object_or_404, render_to_response

from django.template import loader, RequestContext

from django.http import HttpResponseRedirect, HttpResponse, Http404

def home(request):
    return render_to_response('flavoUr/landing.html', context=RequestContext(request))

def profile(request):
  request.message='this is a test'
  return render_to_response('flavoUr/base.html', context=RequestContext(request))
