# Generated by Django 2.2.7 on 2019-11-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0014_docinfo_uchst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docinfo',
            name='na_kakoygod',
            field=models.IntegerField(blank=True, default=2019),
        ),
        migrations.AlterField(
            model_name='docinfo',
            name='na_kakoygod1',
            field=models.IntegerField(blank=True, default=2020),
        ),
        migrations.AlterField(
            model_name='plan',
            name='dr_1_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='dr_2_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='inr_1_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='inr_2_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='nir_1_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='nir_2_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='ucheb_med_r_1_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='ucheb_med_r_2_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='vr_1_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='vr_2_p',
            field=models.CharField(choices=[('Выполнена', 'Выполнена'), ('Выполнена', 'Выполнена частично'), ('Выполнена', 'Не выполнена'), ('Выполнена', ' ')], default=' ', max_length=20),
        ),
    ]