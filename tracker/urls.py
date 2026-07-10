from django.urls import path
from . import views

urlpatterns = [
    # Map the root address of the app to the memorial_home view function
    path('', views.memorial_home, name="home"),
    path('tribute/edit/<int:pk>/', views.edit_tribute, name='edit_tribute'),
    path('tribute/delete/<int:pk>', views.delete_tribute, name='delete_tribute'),   # noqa: E501
]
