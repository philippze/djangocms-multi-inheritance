from django.db import models

from cms.models import CMSPlugin


class SimpleModel(models.Model):
    # If we don't define this field, a SystemCheckError will say: The field
    # 'id' from parent model 'project.somemodel' clashes with the field
    # 'id' from parent model 'cms.cmsplugin'.
    primary_key = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=10)


class AbstractModel(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        abstract = True


class SimpleInheritancePlugin(CMSPlugin, SimpleModel):
    pass


class AbstractInheritancePlugin(CMSPlugin, AbstractModel):
    pass


class FKModel(models.Model):
    # If we don't define this field, a SystemCheckError will say: The field
    # 'id' from parent model 'project.somemodel' clashes with the field
    # 'id' from parent model 'cms.cmsplugin'.
    primary_key = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=10)
    fk= models.ForeignKey(CMSPlugin)

class FKPlugin(CMSPlugin, FKModel):
    pass


class FKAbstractModel(models.Model):
    title = models.CharField(max_length=10)
    fk= models.ForeignKey(CMSPlugin, related_name='abstract_fk_model')

    class Meta:
        abstract = True


class FKAbstractInheritancePlugin(CMSPlugin, FKAbstractModel):
    pass
