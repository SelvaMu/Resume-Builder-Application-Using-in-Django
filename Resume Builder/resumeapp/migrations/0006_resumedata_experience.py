# Generated by Django 4.1.4 on 2023-03-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0005_alter_resumedata_address_alter_resumedata_objective_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='experience',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
