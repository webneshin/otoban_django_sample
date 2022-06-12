import uuid

from django.db import models
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
