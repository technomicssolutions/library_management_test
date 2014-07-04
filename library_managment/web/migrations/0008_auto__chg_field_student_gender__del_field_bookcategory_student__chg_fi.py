# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.gender'
        db.alter_column(u'web_student', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1))
        # Deleting field 'BookCategory.student'
        db.delete_column(u'web_bookcategory', 'student_id')


        # Changing field 'Book.date_of_issue'
        db.alter_column(u'web_book', 'date_of_issue', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Book.date_of_return'
        db.alter_column(u'web_book', 'date_of_return', self.gf('django.db.models.fields.DateTimeField')(null=True))
    def backwards(self, orm):

        # Changing field 'Student.gender'
        db.alter_column(u'web_student', 'gender', self.gf('django.db.models.fields.CharField')(max_length=6))
        # Adding field 'BookCategory.student'
        db.add_column(u'web_bookcategory', 'student',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Student'], null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Book.date_of_issue'
        raise RuntimeError("Cannot reverse this migration. 'Book.date_of_issue' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Book.date_of_return'
        raise RuntimeError("Cannot reverse this migration. 'Book.date_of_return' and its values cannot be restored.")
    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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