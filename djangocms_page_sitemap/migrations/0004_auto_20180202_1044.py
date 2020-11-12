# Generated by Django 1.10.8 on 2018-02-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_page_sitemap", "0003_auto_20151018_1612"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagesitemapproperties",
            name="noarchive",
            field=models.BooleanField(
                default=False,
                help_text="Add meta tag robots with value noarchive",
                verbose_name="Mark as no archive",
            ),
        ),
        migrations.AddField(
            model_name="pagesitemapproperties",
            name="noindex",
            field=models.BooleanField(
                default=False,
                help_text="Add meta tag robots with value noindex",
                verbose_name="Mark as no index",
            ),
        ),
        migrations.AddField(
            model_name="pagesitemapproperties",
            name="robots_extra",
            field=models.CharField(
                default="",
                help_text="Extra values for robots meta tag",
                max_length=200,
                verbose_name="Extra robots value",
            ),
        ),
    ]
