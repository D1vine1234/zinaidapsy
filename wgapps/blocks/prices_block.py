from .initialize import *


class PricesSectionBlock(StructBlock):
    anchor_id = CharBlock(
        label="ID раздела (якорь)",
        required=False,
        help_text="Например: prices — используется в меню навигации",
    )
    heading = RichTextBlock(label="Заголовок раздела", features=["bold", "italic"])
    tariffs = ListBlock(
        StructBlock([
            ("name", RichTextBlock(label="Название тарифа", features=["bold", "italic"])),
            ("price", RichTextBlock(label="Цена", features=["bold", "italic"])),
            ("extra_text", RichTextBlock(
                label="Дополнительный текст",
                required=False,
                features=["bold", "italic"],
                help_text="Например: длительность 1 час",
            )),
            ("description", RichTextBlock(label="Описание", required=False,
                                          features=["bold", "italic", "ul", "ol"])),
        ], label="Тариф"),
        label="Тарифы",
    )

    class Meta:
        template = "blocks/prices_block.html"
        label = "Форматы работы и стоимость"
        icon = "list-ul"
