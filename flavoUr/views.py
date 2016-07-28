from django.shortcuts import get_object_or_404, render_to_response

from django.template import loader, RequestContext

from django.http import HttpResponseRedirect, HttpResponse, Http404


def home(request):
    return render_to_response('flavoUr/landing.html', context_instance=RequestContext(request))
