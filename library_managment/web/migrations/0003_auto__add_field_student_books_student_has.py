# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.books_student_has'
        db.add_column(u'web_student', 'books_student_has',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Student.books_student_has'
        db.delete_column(u'web_student', 'books_student_has')

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
            'books_student_has': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['web']