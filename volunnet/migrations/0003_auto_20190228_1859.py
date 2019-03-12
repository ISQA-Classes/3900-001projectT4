# Generated by Django 2.0.5 on 2019-02-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunnet', '0002_auto_20190228_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('Service Learning', 'Service Learning'), ('Assisting Developing Country', 'Assisting Developing Country'), ('Virtual', 'Virtual'), ('Community', 'Community'), ('Environmental', 'Environmental'), ('Emergency Service', 'Emergency Service'), ('Educational', 'Educational'), ('Corporate', 'Corporate'), ('Event', 'Event'), ('Social/Welfare', 'Social/Welfare')], max_length=30),
        ),
    ]