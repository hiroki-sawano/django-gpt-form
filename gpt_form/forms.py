from django import forms


class CompletionForm(forms.Form):
    prompt = forms.CharField(label='Prompt', widget=forms.Textarea)
