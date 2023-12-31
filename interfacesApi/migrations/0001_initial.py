# Generated by Django 4.0 on 2023-07-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('file_url', models.URLField(null=True)),
                ('file_name', models.CharField(max_length=200, null=True)),
                ('file_extention', models.CharField(max_length=200, null=True)),
                ('deleted', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
