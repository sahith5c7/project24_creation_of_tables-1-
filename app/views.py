from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.filter(topic_name__startswith='B')
    QLTO=Topic.objects.filter(topic_name__endswith='t')
    QLTO=Topic.objects.filter(topic_name__contains='a')

    d={'topics':QLTO}
    return render(request,'display_topics.html',context=d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    /
    QLWO=Webpage.objects.all().order_by('-topic_name')
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.all().order_by(Length('-topic_name'))
    QLWO=Webpage.objects.all()[2:5:]
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='j')
    QLWO=Webpage.objects.filter(name__endswith='n')
    QLWO=Webpage.objects.filter(name__contains='a')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__contains='cricket',name__endswith='n')
    QLWO=Webpage.objects.filter(Q(name__contains='cricket') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(name__contains='cricket') & Q(url__endswith='in'))

    d={'webpages':QLWO}
    return render(request,'display_webpages.html',context=d)

def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().order_by('author')
    QLAO=AccessRecord.objects.all().order_by('name')
    QLAO=AccessRecord.objects.all().order_by('-author')
    QLAO=AccessRecord.objects.all().order_by('-name')
    QLAO=AccessRecord.objects.all().order_by(Length('author'))
    QLAO=AccessRecord.objects.all().order_by(Length('name'))
    QLAO=AccessRecord.objects.all().order_by(Length('author').desc())
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().filter(date__month__gt='10')
    QLAO=AccessRecord.objects.all().filter(date__month__gte='4')
    QLAO=AccessRecord.objects.all().filter(date__month__lt='2000')
    QLAO=AccessRecord.objects.all().filter(date__month__lte='6')
    QLAO=AccessRecord.objects.all().filter(date__year__gte='2020')
    QLAO=AccessRecord.objects.all().filter(date__day__gt='10')
    QLAO=AccessRecord.objects.all().filter(author__startswith='s')
    QLAO=AccessRecord.objects.all().filter(author__endswith='h')
    QLAO=AccessRecord.objects.all().filter(author__contains='a')



    d={'accessrecords':QLAO}
    return render(request,'display_accessrecords.html',context=d)

def insert_topics(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return render(request,'display_topics.html')

def insert_webpages(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    return render(request,'display_webpages.html')

def insert_accessrecords(request):
    pk=int(input('enter pk value of webpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objeccts.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return render(request,'display_accessrecords.html')

def update_webpages(request):
   
    Webpage.objects.filter(topic_name='Cricket').update(name='Boobmra')              #updated the cricket columns with the value boobmra
    Webpage.objects.filter(name='sania mirza').update(url='https://sania.com')       #updated the value with the column name
    Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'Danny'}) #Matches more than one row so throws an error
    Webpage.objects.update_or_create(topic_name='Kabbadi',defaults={'name':'Danny'}) #Cannot assign "'Kabbadi'": "Webpage.topic_name" must be a "Topic" instance.

    

    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',context=d)