# Generated by Django 3.0.6 on 2020-06-03 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_broadcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonecall',
            name='broadcast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseapp.Broadcast'),
            preserve_default=False,
        ),
    ]
