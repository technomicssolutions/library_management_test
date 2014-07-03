# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book_categories'
        db.create_table(u'web_book_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Student'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['Book_categories'])

        # Adding model 'Student'
        db.create_table(u'web_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['Student'])

        # Adding model 'Book'
        db.create_table(u'web_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('book_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_issue', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_of_return', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'web', ['Book'])

    def backwards(self, orm):
        # Deleting model 'Book_categories'
        db.delete_table(u'web_book_categories')

        # Deleting model 'Student'
        db.delete_table(u'web_student')

        # Deleting model 'Book'
        db.delete_table(u'web_book')

    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.book_categories': {
            'Meta': {'object_name': 'Book_categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']"})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['web']