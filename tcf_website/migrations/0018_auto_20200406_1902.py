# Generated by Django 3.0.5 on 2020-04-06 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tcf_website', '0017_auto_20200406_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
