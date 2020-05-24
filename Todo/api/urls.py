from . import views
app_name ='api'


from django.urls import path

urlpatterns = [
    path('', views.TodoIndex, name='TodoIndex'),
    path('RUDView/<int:pk>/', views.RUDView.as_view(), name='TodoIndex')
]
