from django.shortcuts import render

# Create your views here.
def golfdata(request):
    return render(request, "golf-data.html")