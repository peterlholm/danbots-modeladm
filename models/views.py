"Views for training"
from pathlib import Path
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from modeladmin.settings import BASE_DIR
from .models import TrainingModel, SimulationModel
from .forms import TrainingModelForm, SimulationModelForm

def index(request):
    return render(request, 'index.html')

@login_required
def train_model(request):
    myid = request.GET.get('id')
    if request.method == 'POST':
        if myid is None:
            trainform = TrainingModelForm(request.POST)
        else:
            train_elem = TrainingModel.objects.get(pk=myid)
            trainform = TrainingModelForm(request.POST, instance=train_elem)
        if trainform.is_valid():
            trainform.save()
            return redirect('trainlist')
        print ("form is invalid")
    else:   # NOT POST
        if myid is not None:
            train_elem = TrainingModel.objects.get(pk=myid)
            trainform = TrainingModelForm(instance=train_elem)
        else:
            # new empty form
            trainform = TrainingModelForm(initial={'date': timezone.now()})
    mycontext = {
        'form': trainform,
        'head': "Training",
        'id': myid
    }
    return render(request, 'model.html', mycontext)

@login_required
def train_delete(request):
    if request.method == 'GET':
        myid = request.GET.get('id')
        if myid is not None:
            train_elem = TrainingModel.objects.get(pk=myid)
            train_elem.delete()
            return redirect('trainlist')
        return HttpResponse("ERROR")
    return redirect('/')

@login_required
def train_list(request):
    models = list(TrainingModel.objects.all().values().order_by('-date'))
    mycontext = {"modellist": models}
    #print(mycontext)
    return render(request, 'trainlist.html', mycontext)

@login_required
def train_log(request):
    myid = request.GET.get('id')
    print (myid)
    if not myid:
        return HttpResponseNotFound('no id')
    file_path = BASE_DIR / Path('data/trainlog/' + (str(myid) + ".log"))
    print(file_path)
    if not file_path.exists():
        return HttpResponseNotFound('no Log')
   
        #fd.write_text(received_json_data['text'], encoding="utf-8")
    return HttpResponse("<pre>" + open(file_path).read() + "</pre>")

# sim

@login_required
def sim_model(request):
    myid = request.GET.get('id')
    if request.method == 'POST':
        if myid is None:
            simform = SimulationModelForm(request.POST)
        else:
            sim_elem = SimulationModel.objects.get(pk=myid)
            simform = SimulationModelForm(request.POST, instance=sim_elem)
        if simform.is_valid():
            simform.save()
            return redirect('simlist')
        print ("form is invalid")
    else:   # NOT POST
        if myid is not None:
            sim_elem = SimulationModel.objects.get(pk=myid)
            simform = SimulationModelForm(instance=sim_elem)
        else:
            # new empty form
            simform = SimulationModelForm(initial={'date': timezone.now()})
    mycontext = {
        'form': simform,
        'head': "Simulation"
    }
    return render(request, 'model.html', mycontext)

@login_required
def sim_delete(request):
    if request.method == 'GET':
        myid = request.GET.get('id')
        if myid is not None:
            sim_elem = SimulationModel.objects.get(pk=myid)
            sim_elem.delete()
            return redirect('simlist')
        return HttpResponse("ERROR")
    return redirect('/')

@login_required
def sim_list(request):
    models = list(SimulationModel.objects.all().values().order_by('-date'))
    mycontext = {"simlist": models}
    #print(mycontext)
    return render(request, 'simlist.html', mycontext)
