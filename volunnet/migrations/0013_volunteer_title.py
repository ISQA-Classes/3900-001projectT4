# Generated by Django 2.0.5 on 2019-04-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunnet', '0012_volunteer_applied_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]