# Generated by Django 2.2.2 on 2019-06-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linksrecuperacao',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
