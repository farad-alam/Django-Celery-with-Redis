from django.shortcuts import render
from .tasks import add, sub
from celery.result import AsyncResult
# Create your views here.

def index(request):
    result = add.delay(15,12)
    print(f"result add {result}")
    result2 = sub.delay(30,12)
    print(f"result Sub {result2}")

    return render(request, 'index.html', {'result':result, 'result2':result2})

def task_result(request, resId):
    result = AsyncResult(resId)
    return render(request, 'task_result.html', {'result':result})