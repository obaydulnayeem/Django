# Generated by Django 4.2.3 on 2023-10-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_file',
            field=models.FileField(upload_to='study/questions/'),
        ),
    ]
