# Generated by Django 4.0.6 on 2022-07-14 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_rename_data_transacao_data_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data_transacao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
