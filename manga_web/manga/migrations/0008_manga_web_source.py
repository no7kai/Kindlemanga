# Generated by Django 2.0.8 on 2018-12-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0007_volume_fshare_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='web_source',
            field=models.CharField(choices=[('blogtruyen', 'blogtruyen'), ('nettruyen', 'nettruyen'), ('mangaseeonline', 'mangaseeonline')], default='blogtruyen', max_length=100),
            preserve_default=False,
        ),
    ]
