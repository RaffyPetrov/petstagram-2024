# Generated by Django 4.2.3 on 2024-08-27 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petstagramuser',
            options={},
        ),
        migrations.RemoveField(
            model_name='petstagramuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='petstagramuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='petstagramuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='petstagramuser',
            name='last_name',
        ),
    ]
