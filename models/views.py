"Views for training"
from django.shortcuts import render
from django.http import HttpResponse
from .models import TrainingModel
from .forms import TrainingModelForm

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")

def trainmodel(request):
    if request.method == 'POST':
        print("vi poster")
        trainform = TrainingModelForm(request.POST)
        if trainform.is_valid():
            print ("alting er godt")
            trainform.save()
            return HttpResponse("Input modtaget")
        print ("form is invalid")
    else:
        myid = request.GET.get('id')
        if id is not None:
            print("ID:", myid)
            train_elem = TrainingModel.objects.get(pk=myid)
            print (train_elem)
            trainform = TrainingModelForm(instance=train_elem)
        else:
            trainform = TrainingModelForm()
    mycontext = {
        'form': trainform,
    }

    return render(request, 'model.html', mycontext)

def list_models(request):
    models = list(TrainingModel.objects.all().values())
    mycontext = {"modellist": models}
    #print(mycontext)
    return render(request, 'modellist.html', mycontext)
