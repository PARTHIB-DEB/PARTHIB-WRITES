# Generated by Django 4.1.5 on 2023-02-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0007_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
