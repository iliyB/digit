# Generated by Django 2.2 on 2019-11-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20191108_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Slug',
            field=models.SlugField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]