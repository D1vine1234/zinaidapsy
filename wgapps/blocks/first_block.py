from .initialize import *


class FirstBlock(StructBlock):
    anchor_id = CharBlock(
        label="ID раздела (якорь)",
        required=False,
        help_text="Например: hero, about — используется в меню навигации",
    )
    heading = CharBlock(label="Заголовок (имя и профессия)")
    subheading = CharBlock(label="Подзаголовок (услуги)", required=False)
    description = TextBlock(label="Описание", required=False)
    button_text = CharBlock(label="Текст кнопки", required=False)
    button_link = CharBlock(label="Ссылка кнопки", required=False)
    image = ImageChooserBlock(label="Фото", required=False)

    class Meta:
        template = "blocks/first_block.html"
        label = "Первый экран (герой)"
        icon = "image"
