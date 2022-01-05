from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('',views.postz,name='postz'),
    path('<int:post_id>/',views.details,name='details')
]