# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.interface.interfaces import ComponentLookupError

from .registry import Registry
from .lookup import ChainedLookup, LookupContext, LookupChainLink
from .interfaces import IRegistry, ILookup, ILookupsChain

from .directives import sources, target, name, implements, order
from .grokkers import (
    component, component_factory, adapter, subscription, registry)

from .implicit import implicit
from .config import grok, configure

# we do the absolutely compatible monkey patches , not breaking
# the __call__ behavior of interface in any possible way as we don't touch it
# to change the __call__ behavior use crom.monkey.compat() instead (or in
# addition)
from . import monkey
monkey.safe()

__all__ = ["Interface", "ComponentLookupError",
           "Registry", "ListLookup", "ChainLookup",
           "sources", "target", "name", "registry", "implements", "order",
           "component", "adapter", "subscription",
           "implicit", "setup", "teardown", "grok", "configure"]
