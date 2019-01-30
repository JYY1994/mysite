from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-image/$',views.list_images,name='list_images'),
    url(r'^upload-image/$',views.upload_image,name='upload_image'),
    url(r'^del-image/$',views.del_image,name='del_image'),
]