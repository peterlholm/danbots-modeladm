"Views for runqueue"
import json
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import RunQueue
from .forms import RunQueueForm

def index(request):
    return render(request, 'runqueue/index.html')

@login_required
def job(request):
    myid = request.GET.get('id')
    if request.method == 'POST':
        if myid is None:
            jobform = RunQueueForm(request.POST)
        else:
            job_elem = RunQueue.objects.get(pk=myid)
            jobform = RunQueueForm(request.POST, instance=job_elem)
        if jobform.is_valid():
            jobform.save()
            return redirect('joblist')
        print ("form is invalid")
    else:   # NOT POST
        if myid is not None:
            job_elem = RunQueue.objects.get(pk=myid)
            jobform = RunQueueForm(instance=job_elem)
        else:
            # new empty form
            jobform = RunQueueForm(initial={'date': timezone.now()})
    mycontext = {
        'form': jobform,
        'head': "Job"
    }
    return render(request, 'model.html', mycontext)

@login_required
def job_delete(request):
    if request.method == 'GET':
        myid = request.GET.get('id')
        if myid is not None:
            job_elem = RunQueue.objects.get(pk=myid)
            job_elem.delete()
            return redirect('joblist')
        return HttpResponse("ERROR")
    return redirect('/')

@login_required
def job_get(request):
    if request.method == 'GET':
        myid = request.GET.get('id')
        if myid is not None:
            # get specific job
            job_elem = RunQueue.objects.get(pk=myid)
            jobform = RunQueueForm(instance=job_elem)
            mycontext = {
                'form': jobform,
                'head': "Job"
                }
            return render(request, 'model.html', mycontext)
            #return redirect('joblist')

        # get first job
        job_elem = RunQueue.objects.filter(result=None).order_by('date')
        print (job_elem)
        #jobs = list(RunQueue.objects.get(result=None).values().order_by('-date'))
        jobs = list(job_elem)
        print ("antal", len(jobs))
        if len(jobs)>0:
            job = jobs[0]

        mycontext = {"joblist": jobs}
        #print(mycontext)
        return render(request, 'runqueue/joblist.html', mycontext)

            #jobform = RunQueueForm
        return HttpResponse("ERROR")
    return redirect('/')

@login_required
def job_list(request):
    jobs = list(RunQueue.objects.all().values().order_by('-date'))
    mycontext = {"joblist": jobs}
    #print(mycontext)
    return render(request, 'runqueue/joblist.html', mycontext)
