# Generated by Django 4.2.3 on 2024-08-09 13:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import petstagram.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.common.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.common.validators.only_letters_validator])),
                ('picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Do not show', max_length=11, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
