# Generated by Django 2.2.4 on 2019-08-14 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESE', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='module',
        ),
        migrations.AddField(
            model_name='student',
            name='module',
            field=models.ManyToManyField(blank=True, related_name='module', to='ESE.Module'),
        ),
    ]
