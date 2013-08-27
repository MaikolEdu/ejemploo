from .models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def inicio(request):
	return render_to_response('inicio.html',context_instance=RequestContext(request))
