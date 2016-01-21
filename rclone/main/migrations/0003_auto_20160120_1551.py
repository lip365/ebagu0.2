# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(null=True, upload_to=b'images', blank=True),
        ),
    ]
