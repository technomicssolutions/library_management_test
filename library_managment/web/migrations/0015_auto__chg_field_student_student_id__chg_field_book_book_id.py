# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.student_id'
        db.alter_column(u'web_student', 'student_id', self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=200))

        # Changing field 'Book.book_id'
        db.alter_column(u'web_book', 'book_id', self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=100))
    def backwards(self, orm):

        # Changing field 'Student.student_id'
        db.alter_column(u'web_student', 'student_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, null=True))

        # Changing field 'Book.book_id'
        db.alter_column(u'web_book', 'book_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, null=True))
    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'book_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.issue': {
            'Meta': {'object_name': 'Issue'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Book']", 'null': 'True', 'blank': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'return_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'books_student_has': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['web']