from django.urls import path, re_path
from attrApp import views
from django.urls import path
from django.urls import path, include

app_name = 'attrApp'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name = 'attr'),
    #path('whats', views.WhatsappAnalaysis.as_view(), name = 'whats'),
    #path('result', views.finalresult.as_view(), name= 'result'),
    #path('success', views.Success.as_view(), name = 'success'),
    #path('fail',views.Failure.as_view(),name='fail'),
    #path('filenot',views.FileNotfound.as_view(), name='filenot'),
    #path('aboutus',views.AboutUs.as_view(), name='aboutus')
]
