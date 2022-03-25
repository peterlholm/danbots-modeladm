"API functions"
import json
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from modeladmin.settings import API_KEY
from models.models import TrainingModel, SimulationModel

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
        if 'epochs'in received_json_data:
            new_train.epocs = received_json_data['epochs']
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
        if 'training_data_path'in received_json_data:
            new_train.training_data_path = received_json_data['training_data_path']
        if 'sim_seen_score'in received_json_data:
            new_train.sim_seen_score = received_json_data['sim_seen_score']
        if 'sim_unseen_score'in received_json_data:
            new_train.sim_unseen_score = received_json_data['sim_unseen_score']
        if 'wand_score'in received_json_data:
            new_train.wand_score = received_json_data['wand_score']

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

@csrf_exempt
def save_sim(request):
    print("API save sim")
    if request.method in ['POST']:
        received_json_data = json.loads(request.body)
        print("received", received_json_data)
        if 'api-key' not in received_json_data:
            return HttpResponseForbidden('Error 1')
        if received_json_data['api-key'] != API_KEY:
            return HttpResponseForbidden('Error 2')

        new_simul = SimulationModel()
        new_simul.date = str(timezone.now())
        if 'description' in received_json_data:
            new_simul.description = received_json_data['description']
        # if 'hostname'in received_json_data:
        #     new_simul.hostname = received_json_data['hostname']
        if 'simulation_path'in received_json_data:
            new_simul.simulation_path = received_json_data['simulation_path']
        if 'analytic_path'in received_json_data:
            new_simul.analytic_path = received_json_data['analytic_path']
        if 'single_training_path'in received_json_data:
            new_simul.single_training_path = received_json_data['single_training_path']
        if 'batch_training_path'in received_json_data:
            new_simul.batch_training_path = received_json_data['batch_training_path']
        if 'sample_count'in received_json_data:
            new_simul.sample_count = received_json_data['sample_count']
        if 'file_size'in received_json_data:
            new_simul.file_size = received_json_data['file_size']
        if 'light_count'in received_json_data:
            new_simul.light_count = received_json_data['light_count']
        if 'light_intensity'in received_json_data:
            new_simul.light_intensity = received_json_data['light_intensity']
        if 'sim_type'in received_json_data:
            new_simul.sim_type = received_json_data['sim_type']
        if 'background'in received_json_data:
            new_simul.background = received_json_data['background']
        if 'material'in received_json_data:
            new_simul.material = received_json_data['material']

        new_simul.save()

        return HttpResponse('OK')

    models = list(SimulationModel.objects.all().values())
    mycontext = {"simlist": models}
    return render(request, 'simlist.html', mycontext)
