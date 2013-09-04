# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'frontend_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('mode', self.gf('django.db.models.fields.CharField')(default='school mode', max_length=256)),
            ('level', self.gf('django.db.models.fields.CharField')(default='Beginner', max_length=256)),
        ))
        db.send_create_signal(u'frontend', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'frontend_student')


    models = {
        u'frontend.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'frontend.student': {
            'Meta': {'object_name': 'Student'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'Beginner'", 'max_length': '256'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'school mode'", 'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['frontend']