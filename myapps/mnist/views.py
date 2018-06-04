from django.views import generic
from .models import MNIST
from django.shortcuts import render
from django.views.generic.edit import FormMixin
from .forms import MNISTForm
from django.http import JsonResponse
from .digit_recognizer import digit_recognizer

import os
import re
import base64
from io import BytesIO
from PIL import Image
import tensorflow as tf

graph = tf.get_default_graph()
digit_recognizer = digit_recognizer()


class MainView(generic.ListView, FormMixin):
    model = MNIST
    template_name = 'mnist/mnist.html'
    context_object_name = 'digit_list'
    form_class = MNISTForm

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        exlist = self.model.objects.order_by('-data_id')[:8]
        preds = []
        global graph
        with graph.as_default():
            for data in exlist:
                preds.append(digit_recognizer.predict(data.path))
            context['predict'] = preds

        return context

    def post(self, request):
        # ajaxのサーバ側処理
        tmp = MNIST
        latest = tmp.objects.order_by('-data_id')[0]
        new_id = latest.data_id + 1
        new_path = '/mnist/datasets/'+str(new_id)+'.png'

        data = {
            'data_id': new_id,
            'path': new_path,
            'label': request.POST['label']
        }
        form = self.form_class(data)

        if form.is_valid():
            # データ登録
            save_image(request.POST['image_data'], new_path)
            obj = form.save(commit=True)
            obj.save()
            # canvas数字の識別
            global graph
            with graph.as_default():
                pred = digit_recognizer.predict(new_path)
            return JsonResponse({'pred_can': str(pred)})
        return JsonResponse({'pred_can': 'error'})


def detail(request):
    return render(request, 'mnist/detail.html', {})


def save_image(image_data, name):
    # canvasの画像データを保存
    image_data = re.sub("^data:image/png;base64,", "", image_data)
    image_data = base64.b64decode(image_data)
    img = Image.open(BytesIO(image_data))
    img = img.convert('L').resize((28, 28))
    img.save(os.getcwd()+'/myapps/mnist/static'+name)
    return

