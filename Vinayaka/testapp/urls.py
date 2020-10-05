from django.conf.urls import url
from testapp import views

app_name='testapp'

urlpatterns=[
     url(r'^relative/',views.relative,name='relative'),
     url(r'^other/',views.other,name='other')
]
