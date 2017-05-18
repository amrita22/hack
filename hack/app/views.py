# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render_to_response

# Create your views here.



def primary_view(request):
	print "YOU GOT ME"
	if request.method == 'GET':
		context = {}
		return render_to_response('primary.html',context)
	else:
		response = {'status': False, 'message': 'Unauthorized'}
		return HttpResponseNotFound(json.dumps(response))



def secondary_view(request):
	print "YOU GOT ME"
	if request.method == 'GET':
		context = {}
		return render_to_response('secondary.html',context)
	else:
		response = {'status': False, 'message': 'Unauthorized'}
		return HttpResponseNotFound(json.dumps(response))