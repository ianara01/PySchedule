from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('schedule/create/', views.schedule_create, name='schedule_create'),
    path('schedule/<int:schedule_id>/', views.schedule_detail, name='schedule_detail'),
    path('schedule/<int:schedule_id>/edit/', views.schedule_update, name='schedule_update'),
    path('schedule/<int:schedule_id>/delete/', views.schedule_delete, name='schedule_delete'),
    path('filter/date/', views.schedule_filter_by_date, name='schedule_filter_by_date'),
    path('filter/priority/', views.schedule_filter_by_priority, name='schedule_filter_by_priority'),
]
