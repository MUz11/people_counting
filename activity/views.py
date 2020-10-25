from django.shortcuts import render
from .models import counting
from rest_framework import viewsets
from .Serializers import countSerializer
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.http import JsonResponse


# # Create your views here.
class countingViewSet(viewsets.ModelViewSet):
    queryset = counting.objects.all()
    serializer_class = countSerializer
    print(datetime.now()-timedelta(days=1))
    # counting.objects.filter(time__lt=datetime.now()-timedelta(days=1)).delete()

def index(request):
    qq = counting.objects.all()
    data = countSerializer(qq,many=True).data
    context = {
        "data": data
    }

    count = counting.objects.filter(time__lt=datetime.now() - timedelta(days=1))
    data = countSerializer(count,many=True).data
    for x in data:
        ClearData(x['id'])
        print(x['id'])
    return render(request, "index.html", context)


def ClearData(pk):
    count = counting.objects.get(pk=pk)
    count.human_in = 0
    count.human_out = 0
    count.save()