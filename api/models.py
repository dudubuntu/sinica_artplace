from django.db import models


class Item(models.Model):
    articul = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    action = models.BooleanField(default=False)
    previous_price = models.FloatField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('articul',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
