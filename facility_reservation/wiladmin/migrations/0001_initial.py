# Generated by Django 4.2.1 on 2023-10-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AdminReportLogsModel',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('referenceid', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('starttime', models.CharField(max_length=20)),
                ('endtime', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WalkinBookingModel',
            fields=[
                ('bookingid', models.AutoField(primary_key=True, serialize=False)),
                ('referenceid', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('schedule', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]