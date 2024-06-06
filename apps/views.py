from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from.serializers import StudentSerilzers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serilazer=StudentSerilzers(stu)
            json_data=JSONRenderer().render(serilazer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serilazer=StudentSerilzers(stu,many=True)
        json_data=JSONRenderer().render(serilazer.data)
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serilazer=StudentSerilzers(data=pythondata)
        if serilazer.is_valid():
            serilazer.save()
            res={'msg':'Data post'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serilazer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id =pythondata.get('id')
        stu=Student.objects.get(id=id)
        serilazer=StudentSerilzers(stu,data=pythondata,partial=True)
        if serilazer.is_valid():
            serilazer.save()
            res={'msg':'Data update'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serilazer.errors)
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method == 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id =pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}
        return JsonResponse(res,safe=False)
    

    





