# Generated by Django 2.2.2 on 2019-07-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0005_auto_20190726_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='REMARKS_ADMIN',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='REMARKS',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
