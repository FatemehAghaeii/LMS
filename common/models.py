from django.db import models

class BaseModel(models.Model):
    """
    یک مدل پایه انتزاعی که فیلدهای زمان ایجاد و آپدیت رو 
    به طور خودکار به تمام مدل‌های ارث‌بری کننده اضافه میکنه.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین به‌روزرسانی")

    class Meta:
        abstract = True  # این خط باعث میشه جنگو جدولی برای این مدل نسازه