from django.urls import path
from . import views
from views import my_form

urlpatterns = [
    url(r'^index/',send),
    path('my_form/',views.my_form,name="my_function"),
    path('members/', views.members, name='members'),
]
