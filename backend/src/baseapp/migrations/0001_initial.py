# Generated by Django 3.0.6 on 2020-06-03 06:17

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('status', models.CharField(default='inQueue', max_length=256)),
                ('in_progress', models.BooleanField(default=False)),
                ('is_complete', models.BooleanField(default=False)),
                ('retry', models.PositiveSmallIntegerField(default=0)),
                ('sid', models.CharField(blank=True, max_length=256, null=True)),
                ('extra_fields', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'phonecall',
            },
        ),
    ]
