# Generated by Django 4.1.5 on 2023-01-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(height_field='height', upload_to='static/APP/', width_field='width'),
        ),
    ]
