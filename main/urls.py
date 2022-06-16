from django.urls import path

from main.views import ExpertFormView

urlpatterns = [
    path('', ExpertFormView.as_view()),
]
