from django.shortcuts import render

from django.http import JsonResponse

def hello_world_json(request):
    return JsonResponse({"Message":  "Hello welcome to my world!"})
# Create your views here.
