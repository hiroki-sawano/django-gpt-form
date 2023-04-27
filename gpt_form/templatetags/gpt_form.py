from django import template
from django.template.loader import render_to_string

from gpt_form.forms import CompletionForm

register = template.Library()


@register.simple_tag(takes_context=True)
def completion_form(context):
    form = CompletionForm()
    html = render_to_string(
        'gpt_form/completion_form.html',
        context={
            'form': form,
        },
        request=context['request']
    )
    return html
