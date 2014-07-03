# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Student.sex'
        db.delete_column(u'web_student', 'sex')

        # Adding field 'Student.gender'
        db.add_column(u'web_student', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=50),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Student.sex'
        raise RuntimeError("Cannot reverse this migration. 'Student.sex' and its values cannot be restored.")
        # Deleting field 'Student.gender'
        db.delete_column(u'web_student', 'gender')

    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']"})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'books_student_has': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['web']