# Generated by Django 4.1.4 on 2023-07-31 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.FloatField(),
        ),
    ]
