# Generated by Django 2.2.13 on 2021-01-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_force_highlighted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(upload_to='featured_images'),
        ),
    ]
