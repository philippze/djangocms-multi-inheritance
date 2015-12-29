from django.db import models

from cms.models import CMSPlugin


class DesiredMethodCalled(Exception):
    """Used to test if the current method was called."""
    pass


class SimpleModel(models.Model):
    # If we don't define this field, a SystemCheckError will say: The field
    # 'id' from parent model 'project.somemodel' clashes with the field
    # 'id' from parent model 'cms.cmsplugin'.
    primary_key = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=10)

    def copy_relations(self, old):
        raise DesiredMethodCalled


class SimpleInheritancePlugin(CMSPlugin, SimpleModel):
    pass


class AbstractModel(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def copy_relations(self, old):
        raise DesiredMethodCalled


class AbstractInheritancePlugin(CMSPlugin, AbstractModel):
    pass


class IntermediatePluginClass(CMSPlugin):
    title = models.CharField(max_length=10)

    def copy_relations(self, old):
        raise DesiredMethodCalled


class MultilevelInheritancePlugin(IntermediatePluginClass):
    pass
