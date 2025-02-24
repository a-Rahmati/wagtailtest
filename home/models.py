from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from wagtail.models import Page
from wagtail.images.models import Image


class HomePage(Page):
    max_count = 1

    banner_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [FieldPanel('banner_image'), FieldPanel('description')]




    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
