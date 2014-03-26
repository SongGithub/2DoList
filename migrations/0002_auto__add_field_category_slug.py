# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.slug'
        db.add_column(u'to_do_list_app_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.slug'
        db.delete_column(u'to_do_list_app_category', 'slug')


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
            'Create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Item'},
            'Name_item': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Item_set'", 'to': u"orm['to_do_list_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['to_do_list_app']