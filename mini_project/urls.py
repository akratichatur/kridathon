"""kridathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include

from . import views

from mini_project.views import FAQ,about,game,event,tournament,athletics,badminton,basketball,chess,cricket,football,handball,volleyball,hockey,summary,join_event,join_tournament,organize_event,organize_tournament
from mini_project.views import login

urlpatterns = [
    path('', views.index, name='index'),

    url(r'^FAQ/$', FAQ),
    url(r'^about/$', about),
    url(r'^game/$', game),
    url(r'^event/$', event),  
    url(r'^event/join_event/$', join_event),
    url(r'^event/organize_event/$', organize_event),
    url(r'^tournament/$', tournament),  
    url(r'^tournament/join_tournament/$', join_tournament),
    url(r'^tournament/organize_tournament/$', organize_tournament),
    
    url(r'^game/tournament/$', tournament),
    url(r'^game/athletics/$', athletics),
    url(r'^game/badminton/$', badminton),
    url(r'^game/basketball/$', basketball),
    url(r'^game/chess/$', chess),
    url(r'^game/cricket/$', cricket),
    url(r'^game/football/$', football),
    url(r'^game/handball/$', handball),
    url(r'^game/volleyball/$', volleyball),
    url(r'^game/hockey/$', hockey),
    url(r'^summary/$', summary),   
] 


"""
from django.conf.urls import url, include

from index import views


urlpatterns = [
    
    url(r'^index/', views.index),
    url(r'^FAQ', views.FAQ),
]
"""