# HelloWorld/views.py
from django.http import JsonResponse

def main(request):
    return JsonResponse({"Message": "Hello World!"})
