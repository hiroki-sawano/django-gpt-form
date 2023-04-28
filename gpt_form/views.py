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
        if not hasattr(settings, 'OPENAI_API_KEY'):
            return HttpResponseServerError()
        openai.api_key = settings.OPENAI_API_KEY
        return super().dispatch(request, *args, **kwargs)


class Completion(BaseView):
    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
        if prompt:
            params = {
                'model': 'text-davinci-003',
            }
            if hasattr(settings, 'OPENAI_COMPLETION'):
                params = {**params, **settings.OPENAI_COMPLETION}
            params['prompt'] = prompt
            try:
                response = openai.Completion.create(**params)
                return JsonResponse(response)
            except:
                return HttpResponseServerError()
        return HttpResponseBadRequest()
