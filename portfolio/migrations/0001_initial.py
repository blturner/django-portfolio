# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('url', models.URLField(verbose_name='URL', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'verbose_name': 'discipline',
                'verbose_name_plural': 'disciplines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'verbose_name': 'medium',
                'verbose_name_plural': 'media',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('project_url', models.URLField(verbose_name='project URL')),
                ('completion_date', models.DateField(null=True, verbose_name='completion date', blank=True)),
                ('is_ongoing', models.BooleanField(verbose_name='is ongoing')),
                ('summary', models.TextField(verbose_name='summary', blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('overview_image', models.ImageField(upload_to=portfolio.models._get_upload_to_path, verbose_name='overview image', blank=True)),
                ('detail_image', models.ImageField(upload_to=portfolio.models._get_upload_to_path, verbose_name='detail image', blank=True)),
                ('status', portfolio.models.StatusField(default=1, db_index=True, verbose_name='status', choices=[(1, 'drafted'), (2, 'published'), (3, 'removed')])),
                ('client', models.ForeignKey(related_name='projects', verbose_name='client', to='portfolio.Client')),
                ('disciplines', models.ManyToManyField(related_name='projects', verbose_name='disciplines', to='portfolio.Discipline')),
                ('media', models.ManyToManyField(related_name='projects', verbose_name='media', to='portfolio.Medium')),
            ],
            options={
                'ordering': ('-completion_date', 'name'),
                'get_latest_by': 'completion_date',
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('witness', models.CharField(max_length=255, verbose_name='witness', blank=True)),
                ('witness_desc', models.CharField(help_text='Describe their position or relationship.', max_length=255, verbose_name="witness' position", blank=True)),
                ('date', models.DateField(verbose_name='date')),
                ('testimonial', models.TextField(verbose_name='testimonial')),
                ('status', portfolio.models.StatusField(default=1, db_index=True, verbose_name='status', choices=[(1, 'drafted'), (2, 'published'), (3, 'removed')])),
                ('client', models.ForeignKey(related_name='testimonials', verbose_name='client', to='portfolio.Client')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'testimonial',
                'verbose_name_plural': 'testimonials',
            },
            bases=(models.Model,),
        ),
    ]
