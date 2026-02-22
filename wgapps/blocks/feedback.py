from .initialize import *


class FeedbackBlock(StructBlock):
    anchor_id = CharBlock(
        label="ID раздела (якорь)",
        required=False,
        help_text="Например: feedback, contact — используется в меню навигации",
    )
    heading = CharBlock(label="Заголовок")

    class Meta:
        template = "blocks/feedback_block.html"
        label = "Форма обратной связи"
        icon = "mail"
