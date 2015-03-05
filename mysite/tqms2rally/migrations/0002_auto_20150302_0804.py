# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tqms2rally', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue2insert',
            name='navigation',
            field=models.ForeignKey(default=datetime.datetime(2015, 3, 2, 8, 4, 59, 850380, tzinfo=utc), to='tqms2rally.viewNavigation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewnavigation',
            name='viewID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
