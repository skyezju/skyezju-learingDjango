# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfromfile',
            fields=[
                ('issue2insert_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='upload.Issue2Insert')),
            ],
            options={
            },
            bases=('upload.issue2insert',),
        ),
        migrations.CreateModel(
            name='uploadfromtext',
            fields=[
                ('issue2insert_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='upload.Issue2Insert')),
            ],
            options={
            },
            bases=('upload.issue2insert',),
        ),
        migrations.AlterField(
            model_name='issue2insert',
            name='tqmsID',
            field=models.CharField(default=b'no issue yet', max_length=200),
            preserve_default=True,
        ),
    ]
