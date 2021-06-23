from django.db import models

from .tasks import task_send_email


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    extra = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Заявка создана', auto_now_add=True)
    is_processed = models.BooleanField(verbose_name='Заявка обработана', default=False)
    processed_at = models.DateTimeField(verbose_name='Когда обработана', blank=True, null=True)

    def save(self, *args, **kwargs):
        save_returned = super(ContactUs, self).save(*args, **kwargs)
        task_send_email.delay(self.name, self.phone_number, self.created_at)
        return save_returned

    class Meta:
        ordering = ('created_at', )
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'