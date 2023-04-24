from django.urls import path
from .views import index, list, delete

urlpatterns = [
    path('', index, name= 'home'),
    path('<int:id>/', index, name= 'edit'),
    path('list/', list, name='list'),
    path('delete/<int:id>/', delete, name='delete')
]