# Generated by Django 4.2.1 on 2023-10-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_attendance_signouttime_alter_booking_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
