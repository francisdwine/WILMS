# Generated by Django 4.2.1 on 2023-09-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_reference_assignedarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]