#  urls.py    /config
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from schedule import views as schedule_views  # schedule 앱의 뷰를 가져옴
from django.conf import settings
#from . import views as schedule_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schedule_views.schedule_list, name="home"),  # 홈 경로를 schedule_list 뷰로 지정
    path("schedule/", include("schedule.urls")),  # schedule 앱의 URLs 포함
]
                                    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),  # 4 debug_toolbar URL 설정
    ] + urlpatterns
