# Generated by Django 2.2.2 on 2019-08-23 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0020_auto_20190823_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='hackathon_applicants',
        ),
    ]