# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AulthorID', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.DateField(auto_now_add=True)),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=30)),
                ('Publisher', models.CharField(max_length=50)),
                ('PublishDate', models.DateField(auto_now_add=True)),
                ('Price', models.FloatField(max_length=10)),
                ('AulthorID', models.ForeignKey(related_name='ID', to='library.Author')),
            ],
        ),
    ]
