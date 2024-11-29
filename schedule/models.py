from django.db import models

# Create your models here.

class Schedule(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )
    created_at = models.DateTimeField(auto_now_add=True)  # 일정 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 일정 수정 시간

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']  # 기본적으로 날짜 내림차순 정렬
