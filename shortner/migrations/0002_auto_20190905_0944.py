# Generated by Django 2.2.5 on 2019-09-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urldetails',
            name='is_published',
        ),
        migrations.AddField(
            model_name='urldetails',
            name='shorturl',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
