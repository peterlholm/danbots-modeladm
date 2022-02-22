"API functions"
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from isort import file
from models.models import TrainingModel
# Create your views here.

@csrf_exempt
def save_training(request):
    print("API save model")
    if request.method in ['POST']:
        received_json_data = json.loads(request.body)
        print(received_json_data)

        field_list = TrainingModel._meta.fields
        print (field_list)
        print (field_list[1].name)
        #     description = models.CharField(max_length=200)
        # date = models.DateTimeField('date created')
        # hostname = models.CharField(max_length=40)
        # history_path = models.CharField(max_length=200)
        # model_path = models.CharField(max_length=200)
        # figures_dir = models.CharField(max_length=200)
        # dict_text_output_path = models.CharField(max_length=200)
        # checkpoint_path = models.CharField(max_length=200)
        # test_indexes_list_path = models.CharField(max_length=200)
        # test_indexes_list_path = models.CharField(max_length=200)
        # imagecount = models.IntegerField()
        # num_training_img = models.IntegerField()
        # num_validation_img = models.IntegerField()
        # epocs = models.IntegerField()
        # batch_size = models.IntegerField()
        # loss = models.CharField(max_length=20)
        # metrics = models.CharField(max_length=20)
        # optimizer = models.CharField(max_length=20)
        # power = models.IntegerField()
        # n_blocks = models.IntegerField()
        # normalization = models.CharField(max_length=20)
        # learning_rate =
        #new_train.
        new_train = TrainingModel()
        for field in field_list:
            print (field.name)
            if field.name in received_json_data:
                print("update field")
                new_train.field = received_json_data[field.name]

        return HttpResponse('OK')

    models = list(TrainingModel.objects.all().values())
    mycontext = {"modellist": models}
    return render(request, 'modellist.html', mycontext)
