from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('ideas', views.ideas, name='ideas'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('ideas/<int:id>', views.details, name='idea-details')
]
