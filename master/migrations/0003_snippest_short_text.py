# Generated by Django 3.2.10 on 2021-12-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_rename_tag_name_tags_tag_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippest',
            name='short_text',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
