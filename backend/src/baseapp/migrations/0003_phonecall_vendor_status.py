# Generated by Django 3.0.6 on 2020-06-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_phonecall_exotel_app_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonecall',
            name='vendor_status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
