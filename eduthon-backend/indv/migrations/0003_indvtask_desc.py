# Generated by Django 3.0.8 on 2020-09-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indv', '0002_progressmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='indvtask',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]