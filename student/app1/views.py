from django.shortcuts import render

# Create your views here.
def stu_view(request):
    return render(request,'app1/home1.html',context={})
