from django.urls import path
from .views import insert_data,Employee_detail

urlpatterns = [
    path('insert_data/', insert_data, name='insert_data'),
    path('employee/',Employee_detail , name='employee')

]