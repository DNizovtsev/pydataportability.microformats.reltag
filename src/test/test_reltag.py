import unittest

from zope.component import getUtility, getUtilitiesFor
from pkg_resources import resource_string
import pydataportability.microformats.reltag

from pydataportability.microformats.base.htmlparsers.etree import ElementTreeHTMLParser
from pydataportability.microformats.base.interfaces import IHTMLParser,IMicroformatsParser

class Test(unittest.TestCase):


    def testRelTag(self):
        parser = getUtility(IHTMLParser,name="beautifulsoup")()
        data = resource_string(__name__, 'blog_technorati_com.html')
        mf = parser.fromString(data)
        mf.parse()
        self.failUnless(mf.microformats.has_key('rel-tag'), 'rel-tag microformat not found')
        a = [ rt['tag'] for rt in mf.microformats['rel-tag']]
        print a
        self.failUnless(u'blogging' in [ rt['tag'] for rt in mf.microformats['rel-tag']], 'blogging tag not found')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()