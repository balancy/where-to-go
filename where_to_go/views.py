from django.shortcuts import render


def show_blank_page(request):
    return render(request, 'blank.html')


def show_index(request):
    return render(request, 'index.html')