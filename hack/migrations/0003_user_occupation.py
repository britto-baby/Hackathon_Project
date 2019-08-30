# Generated by Django 2.2.2 on 2019-07-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_remove_user_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='OCCUPATION',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('student-teacher', 'Student-teacher'), ('professor', 'Professor')], default='registered', max_length=120, null=True),
        ),
    ]