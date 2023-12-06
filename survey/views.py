from django.shortcuts import render
from .models import surverySubmit
# Create your views here.

def golfsurv(request): 
    if request.method == 'POST':
        fname = request.POST['fname']
        strokes = request.POST['strokes']
        years = request.POST['years']
        seasons = request.POST['seasons']
        areas = request.POST['areas']

        new_surv = surverySubmit(fname=fname, strokes=strokes, years=years, season=seasons, areas=areas)
        new_surv.save()
    return render(request, "golf.html")