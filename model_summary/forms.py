from django import forms
from django.forms import ModelForm
from django.core import exceptions
from .models import ModelSummary
import hashlib
import json


class ModelSummaryDefaultForm(ModelForm):
    class Meta:
        model = ModelSummary
        fields = '__all__'

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)

        data = {}
        if self.cleaned_data['update'] is not None:
            data['update'] = self.cleaned_data.pop('update').update
            self.instance.update = ModelSummary.objects.filter(
                update=data['update'][0])[0]
        else:
            data['update'] = ''

        if self.cleaned_data['model_type'] is not None:
            data['model_type'] = self.cleaned_data.pop(
                'model_type').model_type
            self.instance.model_type = ModelSummary.objects.filter(
                model_type=data['model_type'])[0]
        else:
            data['model_type'] = ''

        if self.cleaned_data['target_symbol'] is not None:
            data['target_symbol'] = self.cleaned_data.pop(
                'target_symbol').target_symbol
            self.instance.target_symbol = ModelSummary.objects.filter(
                target_symbol=data['target_symbol'])[0]
        else:
            data['target_symbol'] = ''

        if self.cleaned_data['loss'] is not None:
            data['loss'] = self.cleaned_data.pop(
                'loss').loss
            self.instance.loss = ModelSummary.objects.filter(
                loss=data['loss'])[0]
        else:
            data['loss'] = ''

        if self.cleaned_data['accuracy'] is not None:
            data['accuracy'] = self.cleaned_data.pop(
                'accuracy').accuracy
            self.instance.accuracy = ModelSummary.objects.filter(
                accuracy=data['accuracy'])[0]
        else:
            data['accuracy'] = ''

        if self.cleaned_data['model_path'] is not None:
            data['model_path'] = self.cleaned_data.pop(
                'model_path').model_path
            self.instance.model_path = ModelSummary.objects.filter(
                model_path=data['model_path'])[0]
        else:
            data['model_path'] = ''

        
        m = hashlib.sha256()
        print('---m--')
        print(m)
        data_json = json.dumps(data, ensure_ascii=False, sort_keys=True)
        m.update(str(data_json).encode('utf-8'))
        hashed = m.hexdigest()
        print('--hashed---')
        print(hashed)
        if self.instance.checksum != hashed:
            print('this ModelSummary already changed')
            if ModelSummary.objects.filter(checksum=hashed).count() == 0:
                self.instance.checksum = hashed
                self.instance.save()
                print('new chcksum', hashed)
            else:
                raise exceptions.ValidationError(
                    'this ModelSummary already saved ModelSummary id:{}'.format(
                        ModelSummary.objects.get(checksum=hashed).pk))
        else:
            raise exceptions.ValidationError('ModelSummary no change')
        print('---data--')
        print(data)        
    