from django.conf.urls import include, url
from . import views
#from webapp.views import upld
urlpatterns =[url(r'^$',views.page1,name='page1'),
              url(r'home/$',views.home,name='home'),
              #url(r'home/$',views.upload1,name='home'),
              url(r'graph/$', views.Graph.as_view(),name='graph'),
              url(r'graph2/$', views.Graph2.as_view(),name='graph2'),
              url(r'graph3/$', views.Graph3.as_view(),name='graph3'),
              url(r'debug2/$',views.debug2,name='debug2'),
              url(r'json/$',views.json,name='json')
            ]
# Create your views here.
