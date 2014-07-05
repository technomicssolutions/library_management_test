# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'web_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Book'], null=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Student'], null=True, blank=True)),
            ('date_of_issue', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_of_return', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Issue'])

    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'web_issue')

    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.issue': {
            'Meta': {'object_name': 'Issue'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Book']", 'null': 'True', 'blank': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'books_student_has': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']