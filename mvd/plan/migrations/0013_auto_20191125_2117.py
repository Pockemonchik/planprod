# Generated by Django 2.2.7 on 2019-11-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0012_auto_20191125_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='docinfo',
            name='na_kakoygod1',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='docinfo',
            name='na_kakoygod',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
