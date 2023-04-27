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
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=7,
                temperature=0,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return JsonResponse(response)
        except:
            return HttpResponseServerError()
    return HttpResponseBadRequest()
