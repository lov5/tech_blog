from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect


# Create your views here.
def index(request):
    return render(request,'index.htm')
def about(request):
    return render(request,'about.htm')
def services(request):
    return render(request,'services.htm')
def contact(request):
    return render(request,'contact.htm')
def councling(request):
    return redirect('http://abhishekgautam2808.pythonanywhere.com/')