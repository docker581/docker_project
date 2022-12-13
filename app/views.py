from django.http import HttpResponse

from .tasks import add


def index(request):
    add_result = add.delay(4, 7)
    return HttpResponse(f'Task result: {add_result.get()}')
