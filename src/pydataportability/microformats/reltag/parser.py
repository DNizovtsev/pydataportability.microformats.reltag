from zope.interface import implements
from pydataportability.microformats.base.interfaces import IMicroformatsParser, IHTMLNode

from urlparse import urlparse
import urllib
import re

class IRelTagParser(IMicroformatsParser):
    """a rel-tag implementation
    Specification  here: http://microformats.org/wiki/rel-tag
    """
    
    
class RelTag(object):
    
    FIELDS = ['tag', 'url']
    
    def __init__(self,tag,url):
        self.data = {'tag': tag, 'url': url}
    
    def __setitem__(self,name,value):
        """store an item in the dict"""
        if name not in self.FIELDS:
            raise KeyError, "'%s' is not a valid key, please use one of %s" %(name,", ".join(self.FIELDS))
        self.data[name]=value

    def __getitem__(self,name):
        """return an item from the dict"""
        if name not in self.FIELDS:
            raise KeyError, "'%s' is not a valid key, please use one of %s" %(name,", ".join(self.FIELDS))
        return self.data.get(name,u'')

    def __str__(self):
        """return a texture representation"""
        return """RelTag for %s: %s""" %(self.data['url'],self.data['tag'])

    
class RelTagParser(object):
    
    implements(IRelTagParser)
    
    def parseNode(self,node):
        """parse a subtree"""
        u = urlparse(node.attrib['href'])
        m = re.search('/([^/]+)/?$', u.path)
        tag = m.group(1)
        if tag:
            return RelTag(urllib.url2pathname(tag).replace('+',u' ').lower(),node.attrib['href'])
        
    def checkNode(self,node):
        """check a node if rel-tag might be inside"""
        if node.tag == 'a':
            rels = node.attrib.get('rel','').split()
            return 'tag' in rels
        
