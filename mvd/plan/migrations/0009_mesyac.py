# Generated by Django 2.2.7 on 2020-01-24 17:26

from django.db import migrations, models
import django.db.models.deletion
import plan.models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20191211_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesyac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('leccii', models.FloatField(blank=True, default=0, null=True, validators=[plan.models.validate_decimals])),
                ('seminar', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('practici_v_gruppe', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('practici_v_podgruppe', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('krugliy_stol', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('konsultacii_pered_ekzamenom', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('tekushie_konsultacii', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('vneauditor_chtenie', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('rucovodstvo_practikoy', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('rucovodstvo_VKR', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('rucovodstvo_kursovoy', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('proverka_auditor_KR', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('proverka_dom_KR', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('proverka_practicuma', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('proverka_lab', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('priem_zashit_practic', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('zacheti_ust', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('zacheti_pism', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('priem_vstupit', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('ekzamenov', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('priem_GIA', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('priem_kandidtskih', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('rucovodstvo_adunctami', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('ucheb_nagruzka', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('auditor_nagruzka', models.FloatField(blank=True, default=0, validators=[plan.models.validate_decimals])),
                ('year', models.IntegerField(blank=True, default=2019)),
                ('polugodie', models.IntegerField(blank=True, default=1)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mes', to='plan.Kafedra')),
                ('prepodavatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mes', to='plan.Profile')),
            ],
        ),
    ]
