from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist

from botManager.models import Bot

# @require_POST
@csrf_exempt
def bot(request, endpoint):
    try:
        b = Bot.objects.get(endpoint=endpoint)
        ret = b.process(request)
        return HttpResponse('hi at {}, endpoint of {}: <br/> {}'.format(endpoint, b, ret))
    except ObjectDoesNotExist:
        return HttpResponse('Not Such Endpoint!')


def index(request):
    return HttpResponse('hi')
