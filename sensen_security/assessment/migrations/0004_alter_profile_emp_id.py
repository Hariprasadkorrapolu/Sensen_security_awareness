# Generated by Django 4.2.21 on 2025-06-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_profile_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emp_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
