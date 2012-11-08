# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectPiece'
        db.create_table('portfolio_projectpiece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_projectpiece', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pieces', to=orm['portfolio.Project'])),
        ))
        db.send_create_signal('portfolio', ['ProjectPiece'])


    def backwards(self, orm):
        # Deleting model 'ProjectPiece'
        db.delete_table('portfolio_projectpiece')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.client': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolio.discipline': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'portfolio.medium': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Medium'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'portfolio.project': {
            'Meta': {'ordering': "('-completion_date', 'name')", 'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['portfolio.Client']"}),
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'disciplines': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['portfolio.Discipline']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ongoing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'media': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['portfolio.Medium']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'overview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'project_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('portfolio.models.StatusField', [], {'default': '1', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'portfolio.projectpiece': {
            'Meta': {'object_name': 'ProjectPiece'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_projectpiece'", 'to': "orm['contenttypes.ContentType']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pieces'", 'to': "orm['portfolio.Project']"})
        },
        'portfolio.testimonial': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Testimonial'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'testimonials'", 'to': "orm['portfolio.Client']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('portfolio.models.StatusField', [], {'default': '1', 'db_index': 'True'}),
            'testimonial': ('django.db.models.fields.TextField', [], {}),
            'witness': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'witness_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']