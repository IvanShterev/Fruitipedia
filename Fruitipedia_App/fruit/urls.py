from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_fruit, name='create-fruit'),
    path('<int:pk>/', include([
        path('details/', views.details_fruit, name='details-fruit'),
        path('edit/', views.edit_fruit, name='edit-fruit'),
        path('delete/', views.delete_fruit, name='delete-fruit')
    ]))
]