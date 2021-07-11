# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-11 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0004_auto_20210711_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaapp.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaapp.Profile')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]