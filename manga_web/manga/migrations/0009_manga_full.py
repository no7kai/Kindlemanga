# Generated by Django 2.0.8 on 2018-12-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0008_manga_web_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
