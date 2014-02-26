import datetime

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


PRIORITY_CHOICES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
)

CompleteStatus_CHOICES = (
    (False, 'Not Yet'),
    (True, 'Completed')
)


class Category(models.Model):
    slug = models.SlugField(unique=True)
    Name_category = models. CharField(max_length=20)
    Description_category = models. CharField(max_length=100)

    def save(self, *args, **kwargs):
        """
        Self Naming Function_for 'Slug'
        """
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.Name_category)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.Name_category

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    # category=models.ForeignKey(Category,blank=True,null=True)
    category = models.ForeignKey('to_do_list_app.Category')
    slug = models.SlugField(unique=True)
    Name_item = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    Create_date = models.DateTimeField('date created', null=True, blank=True)
    Due_date = models.DateTimeField('date due', null=True, blank=True)
    Priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    CompleteStatus = models.BooleanField(
        choices=CompleteStatus_CHOICES,
        default=False
    )

    class Meta:
        verbose_name_plural = 'Items'

    # #Self Naming Function_for 'Slug'
    def save(self, *args, **kwargs):
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.Name_item)
        self.Create_date = timezone.now()
        super(Item, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.Name_item
