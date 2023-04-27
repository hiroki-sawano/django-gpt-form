import openai
from django.conf import settings
from django.http.response import (
    HttpResponseBadRequest,
    HttpResponseServerError,
    JsonResponse,
)


def complete(request):
    prompt = request.POST.get('prompt')
    if prompt:
        openai.api_key = settings.OPENAI_API_KEY
        try:
            response = openai.Completion.create(
                **settings.OPENAI_COMPLETION,
                prompt=prompt,
            )
            return JsonResponse(response)
        except:
            return HttpResponseServerError()
    return HttpResponseBadRequest()
