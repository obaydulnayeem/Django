# Generated by Django 4.2.3 on 2023-10-26 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0010_question_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_file',
            field=models.FileField(upload_to='study/questions/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.pdf', '.jpg', '.png', '.jpeg'])]),
        ),
    ]
