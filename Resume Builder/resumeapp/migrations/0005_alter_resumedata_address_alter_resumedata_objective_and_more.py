# Generated by Django 4.1.4 on 2023-03-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_remove_resumedata_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumedata',
            name='address',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='objective',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='project',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='skill',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
