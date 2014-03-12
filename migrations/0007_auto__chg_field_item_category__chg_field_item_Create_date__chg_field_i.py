# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.category'
        db.alter_column(u'to_do_list_app_item', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['to_do_list_app.Category']))

        # Changing field 'Item.Create_date'
        db.alter_column(u'to_do_list_app_item', 'Create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 2, 25, 0, 0)))

        # Changing field 'Item.Due_date'
        db.alter_column(u'to_do_list_app_item', 'Due_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 25, 0, 0)))
        # Adding unique constraint on 'Item', fields ['slug']
        db.create_unique(u'to_do_list_app_item', ['slug'])

        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique(u'to_do_list_app_category', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique(u'to_do_list_app_category', ['slug'])

        # Removing unique constraint on 'Item', fields ['slug']
        db.delete_unique(u'to_do_list_app_item', ['slug'])


        # Changing field 'Item.category'
        db.alter_column(u'to_do_list_app_item', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['to_do_list_app.Category'], null=True))

        # Changing field 'Item.Create_date'
        db.alter_column(u'to_do_list_app_item', 'Create_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Item.Due_date'
        db.alter_column(u'to_do_list_app_item', 'Due_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    models = {
        u'to_do_list_app.category': {
            'Description_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Category'},
            'Name_category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'to_do_list_app.item': {
            'CompleteStatus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Item'},
            'Name_item': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['to_do_list_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['to_do_list_app']