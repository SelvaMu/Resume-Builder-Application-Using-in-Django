# Generated by Django 4.1.4 on 2023-03-24 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resumedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('objective', models.TextField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
            ],
        ),
    ]
