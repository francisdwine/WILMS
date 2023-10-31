# Generated by Django 4.2.5 on 2023-10-24 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_rename_points_to_add_userprofileinfo_points_to_give'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPointAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_awarded', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_awarded', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_point_awards', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_received_point_awards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
