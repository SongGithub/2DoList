# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.Create_date'
        db.alter_column(u'to_do_list_app_item', 'Create_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Item.Due_date'
        db.alter_column(u'to_do_list_app_item', 'Due_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Item.Create_date'
        raise RuntimeError("Cannot reverse this migration. 'Item.Create_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Item.Create_date'
        db.alter_column(u'to_do_list_app_item', 'Create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # User chose to not deal with backwards NULL issues for 'Item.Due_date'
        raise RuntimeError("Cannot reverse this migration. 'Item.Due_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Item.Due_date'
        db.alter_column(u'to_do_list_app_item', 'Due_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'to_do_list_app.category': {
            'Description_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Category'},
            'Name_category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'to_do_list_app.item': {
            'CompleteStatus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Create_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Item'},
            'Name_item': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['to_do_list_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['to_do_list_app']