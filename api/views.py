"API functions"
import json
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from modeladmin.settings import API_KEY
from models.models import TrainingModel

# pylint: disable=too-many-branches, too-many-statements

@csrf_exempt
def save_training(request):
    print("API save model")
    if request.method in ['POST']:
        received_json_data = json.loads(request.body)
        print("received", received_json_data)
        if 'api-key' not in received_json_data:
            return HttpResponseForbidden('Error 1')
        if received_json_data['api-key'] != API_KEY:
            return HttpResponseForbidden('Error 2')

        #field_list = TrainingModel._meta.fields

        new_train = TrainingModel()
        new_train.date = str(timezone.now())
        if 'description' in received_json_data:
            new_train.description = received_json_data['description']
        if 'hostname'in received_json_data:
            new_train.hostname = received_json_data['hostname']
        if 'history_path'in received_json_data:
            new_train.history_path = received_json_data['history_path']
        if 'model_path'in received_json_data:
            new_train.model_path = received_json_data['model_path']
        if 'figures_dir'in received_json_data:
            new_train.figures_dir = received_json_data['figures_dir']
        if 'dict_text_output_path'in received_json_data:
            new_train.dict_text_output_path = received_json_data['dict_text_output_path']
        if 'checkpoint_path'in received_json_data:
            new_train.checkpoint_path = received_json_data['checkpoint_path']
        if 'test_indexes_list_path'in received_json_data:
            new_train.test_indexes_list_path = received_json_data['test_indexes_list_path']
        if 'imagecount'in received_json_data:
            new_train.imagecount = received_json_data['imagecount']
        if 'num_training_img'in received_json_data:
            new_train.num_training_img = received_json_data['num_training_img']
        if 'num_validation_img'in received_json_data:
            new_train.num_validation_img = received_json_data['num_validation_img']
        if 'epocs'in received_json_data:
            new_train.epocs = received_json_data['epocs']
        if 'batch_size'in received_json_data:
            new_train.batch_size = received_json_data['batch_size']
        if 'loss'in received_json_data:
            new_train.loss = received_json_data['loss']
        if 'metrics'in received_json_data:
            new_train.metrics = received_json_data['metrics']
        if 'optimizer'in received_json_data:
            new_train.optimizer = received_json_data['optimizer']
        if 'power'in received_json_data:
            new_train.power = received_json_data['power']
        if 'n_blocks'in received_json_data:
            new_train.n_blocks = received_json_data['n_blocks']
        if 'normalization'in received_json_data:
            new_train.normalization = received_json_data['normalization']
        if 'learning_rate'in received_json_data:
            new_train.learning_rate = received_json_data['learning_rate']
        # for field in field_list:
        #     print (field.name)
        #     if field.name in received_json_data:
        #         print("update field", field.name, received_json_data[field.name] )
        #         new_train.field = received_json_data[field.name]
        #         print (new_train)
        new_train.save()

        return HttpResponse('OK')

    models = list(TrainingModel.objects.all().values())
    mycontext = {"modellist": models}
    return render(request, 'modellist.html', mycontext)
