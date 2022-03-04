"Views for training"
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import TrainingModel
from .forms import TrainingModelForm

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def trainmodel(request):
    if request.method == 'POST':
        print("vi poster")
        trainform = TrainingModelForm(request.POST)
        if trainform.is_valid():
            print ("alting er godt", trainform)
            trainform.save()
            return redirect('list')
        print ("form is invalid")
    else:
        myid = request.GET.get('id')
        if myid is not None:
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

@login_required
def delete_model(request):
    if request.method == 'GET':
        myid = request.GET.get('id')
        if myid is not None:
            train_elem = TrainingModel.objects.get(pk=myid)
            train_elem.delete()
            return redirect('list')
        return HttpResponse("ERROR")
    return redirect('/')

@login_required
def list_models(request):
    models = list(TrainingModel.objects.all().values().order_by('-date'))
    mycontext = {"modellist": models}
    #print(mycontext)
    return render(request, 'modellist.html', mycontext)
