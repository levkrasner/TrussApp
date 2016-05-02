import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_protect, csrf_exempt
from models import Tenant
from newApp.serializers import TenantSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getName(request):
    return HttpResponse(request.body)

@method_decorator(csrf_exempt)
def getInput(request):
    #objs = json.loads(request.POST)
    return HttpResponse(str(json.loads(request.body)))

def get_first_request(request):
    queryset = Tenant.objects.first()
    return createJson(queryset)

@method_decorator(csrf_exempt)
def save_tenant(request):
       json_content = json.loads(request.body)
       Tenant.objects.get_or_create(**json_content)
       return HttpResponse('User Saved Successfully')

def get_all_tenants(request):
    queryset = Tenant.objects.all()
    return createJson(queryset)

def createJson(response):
    return JsonResponse(serialize('json', response), safe=False)

