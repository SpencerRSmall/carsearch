from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def year_selector(request):
    return render(request, 'date_picker.html')

def make_selector(request):
    return render(request, 'make_picker.html')


