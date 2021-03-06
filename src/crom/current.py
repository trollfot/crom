# -*- coding: utf-8 -*-

from .registry import Registry
from .directives import implements
from .interfaces import ICurrent


@implements(ICurrent)
class Current(object):

    def __init__(self):
        self.teardown()

    def setup(self):
        self.registry = Registry()
        self.lookup = self.registry

    def teardown(self):
        self.registry = None  # FailingRegistry()
        self.lookup = None  # self.registry


current = Current()
