# Generated by Django 4.2.3 on 2023-10-29 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='task_photos/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='task.task')),
            ],
        ),
    ]
