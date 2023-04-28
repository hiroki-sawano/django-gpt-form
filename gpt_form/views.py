import openai
from django.conf import settings
from django.http.response import (
    HttpResponseBadRequest,
    HttpResponseServerError,
    JsonResponse,
)
from django.views import View


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        openai.api_key = settings.OPENAI_API_KEY
        return super().dispatch(request, *args, **kwargs)


class Completion(BaseView):
    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
        if prompt:
            try:
                response = openai.Completion.create(
                    **settings.OPENAI_COMPLETION,
                    prompt=prompt,
                )
                return JsonResponse(response)
            except:
                return HttpResponseServerError()
        return HttpResponseBadRequest()
