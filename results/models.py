from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from registrations.models import Registration  # امپورت کردن مدل ثبت‌نام

class Result(models.Model):
    class Status(models.TextChoices):
        PASSED = "passed", "Passed"
        FAILED = "failed", "Failed"
        PENDING = "pending", "Pending"

    # هر ثبت‌نام فقط می‌تواند یک کارنامه یا نتیجه داشته باشد
    registration = models.OneToOneField(
        Registration,
        on_delete=models.CASCADE,
        related_name="result",
        verbose_name="ثبت‌نام مربوطه"
    )
    
    # نمره بین ۰ تا ۱۰۰
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        blank=True,
        null=True,
        verbose_name="نمره/امتیاز"
    )
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="وضعیت نهایی"
    )
    
    remarks = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات و بازخورد استاد"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Result for {self.registration.participant.email} - {self.registration.event.title}"