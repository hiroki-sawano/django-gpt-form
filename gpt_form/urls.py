from django.urls import path

from gpt_form import views


app_name = 'gpt_form'
urlpatterns = [
    path(
        'complete/', views.complete, name='complete'
    )
]
