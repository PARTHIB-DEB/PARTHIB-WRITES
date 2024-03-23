# Generated by Django 5.0.2 on 2024-03-23 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articleCreateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('catchline', models.TextField(max_length=60, unique=True)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('script', models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='articleViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField()),
                ('total_likes', models.IntegerField(default=0)),
                ('total_comments', models.IntegerField(default=0)),
                ('per_comment', models.CharField(blank=True, null=True)),
                ('per_like', models.IntegerField(blank=True, choices=[('LIKE', 1), ('-----', 0)], default=0, null=True)),
                ('username', models.CharField(blank=True, null=True)),
                ('btitle_id', models.ForeignKey(blank=True, db_column='btitle_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.articlecreatemodel')),
            ],
        ),
    ]
