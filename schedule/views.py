# views.py   /schedule

#from django import forms
from .models import Schedule
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from .forms import ScheduleForm
#import datetime

# Create your views here.

def index(request):
    # 최근 일정 5개만 가져오기 (예시)
    recent_schedules = Schedule.objects.all().order_by('-date')[:5]
    
    context = {
        'recent_schedules': recent_schedules
    }
    return render(request, 'schedule/index.html', context)


def schedule_list(request):
    filter_date = request.GET.get('date', None)  # 필터링 날짜를 쿼리에서 가져옴
    if filter_date:
        schedules = Schedule.objects.filter(date=filter_date)
    else:
        schedules = Schedule.objects.all().order_by('date')
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules, 'filter_date': filter_date})

def schedule_detail(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    return render(request, 'schedule/schedule_detail.html', {'schedule': schedule})

def schedule_create(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule:schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedule/schedule_form.html', {'form': form})


def schedule_update(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule:schedule_detail', schedule_id=schedule.id)
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedule/schedule_form.html', {'form': form})

def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == "POST":
        schedule.delete()
        return redirect('schedule:schedule_list')
    return render(request, 'schedule/schedule_confirm_delete.html', {'schedule': schedule})

def schedule_filter_by_priority(request):
    priority = request.GET.get('priority', 'High')  # 기본값 High
    schedules = Schedule.objects.filter(priority=priority)
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules, 'filter_priority': priority})

def schedule_filter_by_date(request):
    date = request.GET.get('date')
    if date:
        schedules = Schedule.objects.filter(date=parse_date(date))
    else:
        schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules, 'filter_date': date})


