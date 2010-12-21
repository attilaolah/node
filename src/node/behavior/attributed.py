from zope.interface import implements
from node.interfaces import IAttributed
from node.base import OrderedNode
from node.meta import (
    behavior,
    before,
    after,
    BaseBehavior,
)
from node.utils import AttributeAccess


class NodeAttributes(OrderedNode):
    """Semantic object.
    """
    def __init__(self, context):
        OrderedNode.__init__(self)
        self.allow_non_node_childs = True
        self.context = context
        # BBB
        self._node = context


class Attributed(BaseBehavior):
    
    implements(IAttributed)

    attributes_factory = NodeAttributes
    attribute_aliases = None

    def __init__(self, context):
        super(Attributed, self).__init__(context)
        self.attribute_access_for_attrs = False
    
    def _get_attribute_access_for_attrs(self):
        #import pdb;pdb.set_trace()
        val = object.__getattribute__(self, '_attribute_access_for_attrs')
        #print 'get ' + str(val)
    
    def _set_attribute_access_for_attrs(self, val):
        #import pdb;pdb.set_trace()
        #print 'set ' + str(val)
        object.__setattr__(self, '_attribute_access_for_attrs', val)
    
    attribute_access_for_attrs = property(_get_attribute_access_for_attrs,
                                          _set_attribute_access_for_attrs)
    
    @property
    def attrs(self):
        try:
            attrs = self.context.nodespaces['__attrs__']
        except KeyError:
            attrs = self.context.nodespaces['__attrs__'] = \
                self.attributes_factory(self)
            attrs.__name__ = '__attrs__'
            attrs.__parent__ = self.context
        if object.__getattribute__(self, '_attribute_access_for_attrs'):
            import pdb;pdb.set_trace()
            return AttributeAccess(attrs)
        return attrs

    # BBB
    attributes = attrs