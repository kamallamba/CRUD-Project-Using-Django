from django.shortcuts import render,HttpResponseRedirect
from.forms import StudentForm
from.models import StudentsInfo



# Create your views here.

def Home(request):
    return render(request,'App1/Home.html')

def ShowFormData(request):
    if request.method=='POST':
        fm= StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm= StudentForm()
    all=StudentsInfo.objects.all()
    return render(request, 'App1/Home.html',{'Fillup':fm,'Show':all})

def Update(request,Roll_NO):
    pi= StudentsInfo.objects.get(pk=Roll_NO)
    if request.method=='POST':
        fm= StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm=StudentForm(instance=pi)
    return render(request, 'App1/Show_data.html',{'form':fm})

def Delete(request,Roll_NO):
    pi= StudentsInfo.objects.get(pk=Roll_NO)
    pi.delete()
    return HttpResponseRedirect('/')


