# Generated by Django 2.2 on 2019-11-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_books_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Cost',
            field=models.IntegerField(),
        ),
    ]