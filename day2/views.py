from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Ini pekerjaan day 2.")