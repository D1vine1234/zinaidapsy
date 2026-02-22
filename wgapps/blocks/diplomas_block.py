from .initialize import *


class DiplomaSectionBlock(StructBlock):
    anchor_id = CharBlock(
        label="ID раздела (якорь)",
        required=False,
        help_text="Например: education — используется в меню навигации",
    )
    heading = CharBlock(label="Заголовок раздела", required=False)
    diplomas = ListBlock(ImageChooserBlock(), label="Дипломы")

    class Meta:
        template = "blocks/diplomas_block.html"
        label = "Дипломы (слайдер)"
        icon = "pick"
