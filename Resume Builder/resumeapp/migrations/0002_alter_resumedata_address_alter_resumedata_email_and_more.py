# Generated by Django 4.1.4 on 2023-03-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumedata',
            name='address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='institution',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='objective',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='percentage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='project',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='qualification',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='skill',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
