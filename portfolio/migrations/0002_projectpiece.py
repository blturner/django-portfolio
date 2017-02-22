# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(db_index=True)),
                ('object_type', models.ForeignKey(related_name='related_projectpiece', to='contenttypes.ContentType')),
                ('project', models.ForeignKey(related_name='pieces', to='portfolio.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
