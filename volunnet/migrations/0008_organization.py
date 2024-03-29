# Generated by Django 2.1.7 on 2019-04-03 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunnet', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('phone', models.IntegerField(default=1234567890)),
                ('zipcode', models.IntegerField(default=68106)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
