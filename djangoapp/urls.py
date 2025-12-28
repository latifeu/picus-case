from django.urls import path
from . import views

urlpatterns = [
    path('list', views.user_list),
    path('put', views.user_put),
    path('get/<int:id>', views.user_get),
    path('<int:id>', views.user_delete),
]
