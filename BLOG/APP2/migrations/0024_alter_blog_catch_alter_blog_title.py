# Generated by Django 4.1.5 on 2023-02-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0023_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='catch',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
