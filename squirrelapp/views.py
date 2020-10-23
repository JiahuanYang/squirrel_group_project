from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from .models import SquirrelDetails
from .forms import LatiForm

def map(request):
    sightings = SquirrelDetails.objects.all()[:100]
    context = {
            'sightings': sightings,
    }
    return render(request,'squirrelapp/map.html',context)

def index(request):
    sightings = SquirrelDetails.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request,'squirrelapp/index.html',context)

def update(request, squirrel_id):
    sighting = get_object_or_404(SquirrelDetails, pk=squirrel_id)
    context = {
            'sighting': sighting,
    }
    return render(request,'squirrelapp/update.html',context)

def update_lati(request, squirrel_id):
    if request.method == 'POST':
        sighting = get_object_or_404(SquirrelDetails, pk=squirrel_id)
        form = LatiForm(request.POST or None,
                        request.FILES or None, instance=sighting)
        if form.is_valid():
             form.save()
             context = {'form': form}
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next) 
    else:
        return JsonResponse({'errors': form.errors}, status=400)
    
    return render(request,'squirrelapp/update.html',context)
    
def sightingsadd(request):
    return render(request,'squirrelapp/sightingsadd.html',{})

def sightingsstats(request):
    return render(request,'squirrelapp/sightingsstats.html',{})
   
