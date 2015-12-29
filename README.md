# How to use inheritance with CMSPlugins

When writing a `CMSPlugin` in the DjangoCMS, it is possible to use
class inheritance. Here are a few examples with tests about how exactly
to do that.


## Overview


### CMSPlugin must be first superclass

The `CMSPlugin` class makes a few important changes in comparison to
the usual django `Model` class, like modifying the `__new__` class method.

When dealing with multiple inheritance, Python searches for inherited
attributes through the list of parent classes from left to right.

Thus, the `CMSPlugin` class **must** come first in the list of
superclasses; otherwise strange errors will occur, see the little
script `SHOW_ERROR`.


### Multiple inheritance with abstract parent model works for fields

We can define the meta option `abstract = True` in some
`AbstractModel` and then use multiple inheritance, like this:

```
class AbstractInheritancePlugin(CMSPlugin, AbstractModel):
    ...
```

Then, any fields defined in AbstractModel will be present in the child
class.


### Multi table multiple inheritance requires a primary key definition.

If we do **not** use `abstract = True` in the base class, we will have
to define some primary key for this class. Otherwise, Django will
complain about name clashing when creating a primary key.

The parent class has to look like this:

```
class SimpleModel(models.Model):
    primary_key = models.PositiveIntegerField(primary_key=True)
    ...
```

With that, we can use multiple inheritance, and the child class will
contain the fields defined in the parent class.

```
class SimpleInheritancePlugin(CMSPlugin, SimpleModel):
   ...
```


### Overriding things defined in the `CMSPlugin` class requires multilevel inheritance

Sometimes, we want to override properties that are already defined in
the `CMSPlugin` class, like the `copy_relations` method.

As we said above, when we use multiple inheritance, Python searches for
attributes in the parent classes from left to right. And: the
`CMSPlugin` class has to come first.

Thus, we cannot use multiple inheritance if we want to override
`CMSPlugin` properties for a base class. Instead, we should use
multilevel inheritance:

```
class IntermediatePluginClass(CMSPlugin):
    ...
    def copy_relations(self, old):
        ...

class MultilevelInheritancePlugin(IntermediatePluginClass):
    ...
```


## What's inside this repo

This repo defines two Django CMS projects. One is called
'the_wrong_way', the other one ist called 'the_right_way'.

In 'the_wrong_way', we define a CMSPlugin where the order of the
parent classes is wrong - nothing else.

When we initialize the test database for 'the_wrong_way', some strange
error will occur.

In 'the_right_way' we define an number of models in ways described
above and test their behaviour.

The models are located in [the_right_way/project/models.py] and the
tests in [the_right_way/project/tests.py].


## Install and test

Simply say

```
pip install -r requirements.txt
```

Then, the script `SHOW_ERROR` will show what happens if you define
parent classes in the wrong order. The script `TEST` will perform the
tests that pass.
