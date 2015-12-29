from django.test import TestCase

from cms.models import CMSPlugin

from project.models import (
    SimpleInheritancePlugin,
    AbstractInheritancePlugin,
    FKPlugin,
    FKAbstractInheritancePlugin,
)


class InheritanceTest(TestCase):

    def tearDown(self):
        SimpleInheritancePlugin.objects.all().delete()
        AbstractInheritancePlugin.objects.all().delete()
        CMSPlugin.objects.all().delete()

    def make_saving_test(self, cls, **kwargs):
        obj = cls()
        for key, value in kwargs.iteritems():
            setattr(obj, key, value)
        obj.save()
        saved_obj = cls.objects.get()
        for key, value in kwargs.iteritems():
            saved_value = getattr(saved_obj, key)
            self.assertEqual(saved_value, value)

    def test_simple(self):
        self.make_saving_test(
            SimpleInheritancePlugin,
            primary_key=1,
            title='A title'
        )

    def test_abstract(self):
        self.make_saving_test(
            AbstractInheritancePlugin,
            title='A title'
        )

    def test_fk(self):
        cmsplugin = CMSPlugin.objects.create()
        self.make_saving_test(
            FKPlugin,
            primary_key=5,
            title='A title',
            fk=cmsplugin
        )

    def test_fk_abstract(self):
        cmsplugin = CMSPlugin.objects.create()
        self.make_saving_test(
            FKAbstractInheritancePlugin,
            title='A title',
            fk=cmsplugin
        )
