# Generated by Django 2.2.4 on 2019-08-14 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ESE', '0003_auto_20190814_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='competency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ESE.Competency'),
        ),
    ]
