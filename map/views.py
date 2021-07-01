from django.shortcuts import render

# Create your views here.
def location(request):
    return render(request,'location.html')

def main(request):
    return render(request,'main.html')