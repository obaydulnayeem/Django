# Generated by Django 4.2.3 on 2023-12-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='photo',
        ),
        migrations.AddField(
            model_name='task',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
