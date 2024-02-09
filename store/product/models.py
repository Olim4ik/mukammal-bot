from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("Product name"), max_length=255)
    photo = models.CharField(_("Rasm link"), max_length=255)
    price = models.DecimalField(_("Price"), max_digits=8, decimal_places=2)
    description = models.TextField(_("Description"), null=True, blank=True)

    category_code = models.CharField(verbose_name="Category code", max_length=20)
    category_name = models.CharField(verbose_name="Categoryname", max_length=30)
    subcategory_code = models.CharField(verbose_name="Subcategory code", max_length=20)
    subcategory_name = models.CharField(verbose_name="Subcategory name", max_length=30)

    def __str__(self):
        return f"№{self.id} - {self.title}"
