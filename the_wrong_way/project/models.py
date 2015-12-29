from django.db import models

from cms.models import CMSPlugin


class SomeModel(models.Model):
    # If we don't define this field, a SystemCheckError will say: The field
    # 'id' from parent model 'project.somemodel' clashes with the field
    # 'id' from parent model 'cms.cmsplugin'.
    primary_key = models.PositiveIntegerField(primary_key=True)


class SomeCMSPlugin(SomeModel, CMSPlugin):
    pass
