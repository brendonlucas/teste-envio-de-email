# Generated by Django 2.2.2 on 2019-06-30 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gg', '0003_linksrecuperacao_data2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linksrecuperacao',
            name='data2',
        ),
    ]