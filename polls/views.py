from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import timedelta,datetime
from .models import Building, SingleResponse
from .forms import ResponseForm, FoodForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    form = ResponseForm()
    fform= FoodForm()

    def get_queryset(self):
        """Return the last five published questions."""
        return Building.objects.order_by('-name')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # get the default context data
        context['form'] = self.form
        context['fform']= self.fform
        return context

def post_new(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ResponseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save()
            building = form.cleaned_data['building']
            building.avg_temp()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    else:
        form = ResponseForm()
    return render(request, 'polls/form.html', {'form': form})

def post_new_food(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = form.save(commit=False)
            building = form.cleaned_data['building']
            obj.geom = building.geom
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    else:
        form = FoodForm()
    return render(request, 'polls/food.html', {'form': form})

def plot_building(request,building_name):
    building_name = building_name.replace('_',' ')
    srlist = SingleResponse.objects.filter(building__name=building_name).order_by('-timestamp')
    rooms = srlist.values('room').distinct()
    num = len(srlist)
    cold,cool,jr,warm,hot=0,0,0,0,0
    for i in range(0,len(srlist)):
        t= srlist[i].temp
        if t== -2:
            cold += 1
        elif t== -1:
            cool += 1
        elif t== 0:
            jr +=1
        elif t== 1:
            warm += 1
        else:
            hot +=1
    temps = [cold,cool,jr,warm,hot]
    return render(request, 'polls/building.html',{'building':building_name,'srlist':srlist,'temps':temps,'num':num,'rooms':rooms})
