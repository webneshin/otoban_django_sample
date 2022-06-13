import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Abstract_Model(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )
    created_time = models.DateTimeField(
        _('زمان ایجاد'),
        auto_now_add=True,
        db_index=True
    )
    edited_time = models.DateTimeField(
        _('زمان ویرایش'),
        auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


# in admin and drf cleaning data always
@receiver(pre_save)
def pre_save_handler(sender, instance, *args, **kwargs):
    if sender._meta.app_label != 'sessions':
        instance.full_clean()