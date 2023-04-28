from django import forms


class CompletionForm(forms.Form):
    prompt = forms.CharField(label='Prompt', widget=forms.Textarea)

    class Media:
        css = {
            'all': ['gpt_form/css/completion-form.css']
        }
