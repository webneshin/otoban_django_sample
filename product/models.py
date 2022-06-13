from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from rest_framework import serializers

from core.models import Abstract_Model


class Category(Abstract_Model):
    """
    Categories
    """
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=_('والد'),
        blank=True,
        null=True,
        related_name='subcategories',
    )
    title = models.CharField(
        _('عنوان'),
        max_length=200
    )
    description = models.CharField(
        _('توضیح'),
        max_length=1000,
        blank=True,
        null=True,
    )

    @property
    def level(self):
        if self.parent:
            return 1 + self.parent.level
        else:
            return 1


    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی')
        ordering = ['created_time']

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        if self.level > 4:
            raise serializers.ValidationError(_('دسته بندی نمی تواند بیش تر از 4 لایه باشد !'))



class Product(Abstract_Model):
    """
    Products
    """
    title = models.CharField(
        _('عنوان'),
        max_length=200,
        # help_text=_('لطفا نام کالا را وارد نمایید')
    )
    price = MoneyField(
        _('قیمت'),
        max_digits=15,
        decimal_places=0,
        default_currency='IRR',
        validators=[
            MinMoneyValidator(0),
        ]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name=_('دسته بندی'),
    )

    class Meta:
        verbose_name = _('کالا')
        verbose_name_plural = _('کالاها')
        ordering = ['-created_time']

    def __str__(self):
        return self.title


class Product_Image(Abstract_Model):
    """
    Images
    """
    product = models.ForeignKey(
        Product,
        related_name='product_images',
        on_delete=models.deletion.CASCADE
    )
    image = models.ImageField(
        _('عکس'),
        upload_to='image_product/',
    )
    sort = models.SmallIntegerField(
        _('ترتیب'),
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('product', F('sort').asc(nulls_last=True))
        verbose_name = _('عکس کالا')
        verbose_name_plural = _('عکس های کالا')
