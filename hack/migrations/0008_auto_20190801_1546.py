# Generated by Django 2.2.2 on 2019-08-01 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0007_auto_20190801_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='port',
            new_name='PORTFOLIO_FILES',
        ),
    ]
