from django.db import models

from wagtail.admin.panels import FieldPanel

from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable, ParentalKey
from wagtail.blocks import (
    RichTextBlock,
    CharBlock,
    StructBlock,
    ListBlock,
    TextBlock,
    PageChooserBlock,
    ChoiceBlock,
    BooleanBlock,
    IntegerBlock,
    DateBlock,
)

from wagtail.documents.blocks import DocumentChooserBlock
