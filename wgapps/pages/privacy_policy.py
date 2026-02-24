from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wgapps.blocks.accordion_block import AccordionItemBlock


class PrivacyPolicyPage(Page):
    
    content = StreamField([
        ("accordion", AccordionItemBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    template = "pages/privacy_policy_page.html"

    class Meta:
        verbose_name = "Политика конфиденциальности"
