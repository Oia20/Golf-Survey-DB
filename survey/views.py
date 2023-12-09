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

        new_surv = surverySubmit(fname=fname, strokes=strokes, years=years, seasons=seasons, areas=areas)
        new_surv.save()
        name = surverySubmit.objects.all()
        strokes = 0
        counter = 0
        driving = 0
        for i in name:
            counter += 1
            strokes += i.strokes
        springs = surverySubmit.objects.filter(seasons='spring').count()
        summers = surverySubmit.objects.filter(seasons='summer').count()
        winters = surverySubmit.objects.filter(seasons='winter').count()
        falls = surverySubmit.objects.filter(seasons='fall').count()
        strokes = strokes // counter
        lessThan1Yr = surverySubmit.objects.filter(years='less than one.').count()
        oneYr = surverySubmit.objects.filter(years='one').count()
        twoYr = surverySubmit.objects.filter(years='two').count()
        threeYr = surverySubmit.objects.filter(years='three').count()
        fourYr = surverySubmit.objects.filter(years='four').count()
        fiveYr = surverySubmit.objects.filter(years='five').count()
        moreThan6Yr = surverySubmit.objects.filter(years='six or more.').count()
        putting = surverySubmit.objects.filter(areas='putting').count()
        approuching = surverySubmit.objects.filter(areas='approuching').count()
        driving = surverySubmit.objects.filter(areas='driving').count()
        chipping = surverySubmit.objects.filter(areas='chipping').count()
        idk = surverySubmit.objects.filter(areas='idk').count()




        return render(request,'golf-data.html', {'strokes': strokes, 'subs': counter, 'springs': springs, 
                                                 'summers': summers, 'winters': winters, 'falls': falls,
                                                 'lessThan1Yr': lessThan1Yr, 'oneYr': oneYr, 'twoYr': twoYr, 
                                                 'threeYr': threeYr, 'fourYr': fourYr, 'fiveYr': fiveYr, 
                                                 'moreThan6Yr': moreThan6Yr , 'putting': putting, 'approuching': approuching, 
                                                 'driving': driving, 'chipping': chipping, 'idk': idk})
    return render(request, "golf.html")