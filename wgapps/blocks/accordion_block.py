from .initialize import *


class AccordionItemBlock(StructBlock):

    heading = RichTextBlock(label="Заголовок", required=False)
    
    points = ListBlock(
        StructBlock([
            ("heading", RichTextBlock(label="Заголовок", required=False)),
            ("contents", RichTextBlock(label="Содержимое", required=False)),
        ])
    )

    class Meta:
        template = "blocks/accordion_block.html"
        label = "Пункты"
        icon = "list-ul"
