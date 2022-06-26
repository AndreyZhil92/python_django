from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'hi', '123'],
        'obj': {
            'car': 'No',
            'age': '30',
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
