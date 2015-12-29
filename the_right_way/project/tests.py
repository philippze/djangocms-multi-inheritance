from django.test import TestCase

from cms.models import CMSPlugin

from project.models import (
    SimpleInheritancePlugin,
    AbstractInheritancePlugin,
    MultilevelInheritancePlugin,
    DesiredMethodCalled,
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

    def test_multilevel_inheritance(self):
        self.make_saving_test(
            MultilevelInheritancePlugin,
            title='A title',
        )

    def test_copy_relations_called(self):
        obj = MultilevelInheritancePlugin(title='A title')
        with self.assertRaises(DesiredMethodCalled):
            obj.copy_relations('Some argument required')
