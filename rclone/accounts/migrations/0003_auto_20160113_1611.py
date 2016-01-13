# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151224_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='favourite_snack',
        ),
        migrations.AddField(
            model_name='myprofile',
            name='intro',
            field=models.CharField(default=b'Hello', max_length=5, verbose_name='intro'),
        ),
    ]
