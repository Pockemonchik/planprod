# Generated by Django 2.2.7 on 2019-11-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0013_auto_20191125_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='docinfo',
            name='uchst',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]