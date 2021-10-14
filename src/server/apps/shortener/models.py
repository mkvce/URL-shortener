from django.db import models


# Create your models here.


class URL(models.Model):
    address = models.URLField(max_length=256, verbose_name='آدرس لینک')
    label = models.CharField(max_length=128, blank=True, verbose_name='برچسب')
    slug = models.SlugField(unique=True, max_length=8)
    visits = models.PositiveIntegerField(default=0, editable=False,
                                         verbose_name="تعداد بازدیدها")
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')

    class Meta:
        verbose_name = 'URL'

    def __str__(self):
        return self.address

    def increase_visits(self):
        self.visits += 1
        self.save()
