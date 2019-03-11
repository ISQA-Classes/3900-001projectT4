# Generated by Django 2.0.5 on 2019-02-28 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('volunnet', '0003_auto_20190228_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='date',
        ),
        migrations.AlterField(
            model_name='activity',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
