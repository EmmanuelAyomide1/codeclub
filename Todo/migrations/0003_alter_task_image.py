# Generated by Django 4.2 on 2023-10-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_task_description_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='pics'),
        ),
    ]