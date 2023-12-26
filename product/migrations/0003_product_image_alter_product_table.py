# Generated by Django 5.0 on 2023-12-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_product_options_alter_product_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=1, upload_to="product_images", verbose_name="Фото"
            ),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name="product",
            table=None,
        ),
    ]