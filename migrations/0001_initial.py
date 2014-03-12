# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'to_do_list_app_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name_category', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('Description_category', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'to_do_list_app', ['Category'])

        # Adding model 'Item'
        db.create_table(u'to_do_list_app_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Item_set', to=orm['to_do_list_app.Category'])),
            ('Name_item', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('CompleteStatus', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'to_do_list_app', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'to_do_list_app_category')

        # Deleting model 'Item'
        db.delete_table(u'to_do_list_app_item')


    models = {
        u'to_do_list_app.category': {
            'Description_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Category'},
            'Name_category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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