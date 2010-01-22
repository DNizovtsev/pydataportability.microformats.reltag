from zope.component import getUtility, getUtilitiesFor
from pkg_resources import resource_string
import pydataportability.microformats.reltag

from pydataportability.microformats.base.htmlparsers.etree import ElementTreeHTMLParser
from pydataportability.microformats.base.interfaces import IHTMLParser,IMicroformatsParser


#parser = getUtility(IHTMLParser,name="elementtree")()
parser = getUtility(IHTMLParser,name="beautifulsoup")()
parsers = getUtilitiesFor(IMicroformatsParser)
for p in parsers:
    print p

data = resource_string(__name__, 'blog_technorati_com.html')
#data = resource_string(__name__, 'mrtopf.html')
mf = parser.fromString(data)
mf.parse()

for name,result in mf.microformats.items():
    print "**",name,"**"
    print result[0]
    for r in result:
        print r
