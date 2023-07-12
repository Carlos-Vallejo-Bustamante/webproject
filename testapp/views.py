import json
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers)}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    # Para los test usamos el body
    # body = json.loads(request.body.decode())
    # response = {'resultado': int(body['a']) + int(body['b'])}
    suma = int(request.GET.get('a')) + int(request.GET.get('b'))
    response = {'resultado': suma}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


def home(request):
    return render(request, 'testapp/home.html')


def gallery(request):
    return render(request, 'testapp/gallery.html')


def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)


def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operator = request.POST['operator']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = None

        context = {
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'result': result
        }
    else:
        context = {}

    return render(request, 'testapp/calculadora.html', context)

