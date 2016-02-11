# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import mptt.fields
import django.utils.timezone
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('description', models.TextField(verbose_name=b'\xec\xbb\xa4\xeb\xae\xa4\xeb\x8b\x88\xed\x8b\xb0 \xec\x84\xa4\xeb\xaa\x85')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('ups', models.IntegerField(default=0)),
                ('downs', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('raw_comment', models.TextField(blank=True)),
                ('html_comment', models.TextField(blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='main.Comment', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=250, null=True, blank=True)),
                ('video', embed_video.fields.EmbedVideoField(help_text=b'Youtube\xec\xa3\xbc\xec\x86\x8c\xeb\xa7\x8c \xec\x9e\x85\xeb\xa0\xa5\xed\x95\xb4\xec\xa3\xbc\xec\x84\xb8\xec\x9a\x94', null=True, verbose_name=b'\xeb\x8f\x99\xec\x98\x81\xec\x83\x81\xeb\xa7\x81\xed\x81\xac', blank=True)),
                ('title', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.CharField(unique=True, max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('rank_score', models.FloatField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(verbose_name=b'\xec\xbb\xa4\xeb\xae\xa4\xeb\x8b\x88\xed\x8b\xb0', to='main.Category')),
                ('moderator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_up', models.BooleanField(default=True, verbose_name=b'good')),
                ('post', models.ForeignKey(to='main.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='main.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
