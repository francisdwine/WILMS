# Generated by Django 4.2.5 on 2023-10-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_userprofileinfo_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
