# Generated by Django 2.1.7 on 2019-04-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunnet', '0009_organization_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address2',
        ),
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(default='Omaha', max_length=50),
        ),
        migrations.AddField(
            model_name='organization',
            name='state',
            field=models.CharField(default='NE', max_length=2),
        ),
    ]
