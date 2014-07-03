# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Student.student_id'
        db.delete_column(u'web_student', 'student_id')

        # Adding field 'Student.stud_id'
        db.add_column(u'web_student', 'stud_id',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Student.gender'
        db.alter_column(u'web_student', 'gender', self.gf('django.db.models.fields.CharField')(max_length=6))
        # Deleting field 'BookCategory.category'
        db.delete_column(u'web_bookcategory', 'category')

        # Adding field 'BookCategory.book_category'
        db.add_column(u'web_bookcategory', 'book_category',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Book.book_category'
        db.add_column(u'web_book', 'book_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.BookCategory'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Book.book_name'
        db.alter_column(u'web_book', 'book_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Book.book_id'
        db.alter_column(u'web_book', 'book_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Student.student_id'
        raise RuntimeError("Cannot reverse this migration. 'Student.student_id' and its values cannot be restored.")
        # Deleting field 'Student.stud_id'
        db.delete_column(u'web_student', 'stud_id')


        # Changing field 'Student.gender'
        db.alter_column(u'web_student', 'gender', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'BookCategory.category'
        raise RuntimeError("Cannot reverse this migration. 'BookCategory.category' and its values cannot be restored.")
        # Deleting field 'BookCategory.book_category'
        db.delete_column(u'web_bookcategory', 'book_category')

        # Deleting field 'Book.book_category'
        db.delete_column(u'web_book', 'book_category_id')


        # User chose to not deal with backwards NULL issues for 'Book.book_name'
        raise RuntimeError("Cannot reverse this migration. 'Book.book_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Book.book_id'
        raise RuntimeError("Cannot reverse this migration. 'Book.book_id' and its values cannot be restored.")
    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_of_issue': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_return': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']"})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'books_student_has': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stud_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']