from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_main),
    path('<int:month_num>', views.process_month_by_number),
    path('<str:month>', views.process_month, name='month-by-name')
]
