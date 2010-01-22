from zope.component import provideUtility, getUtilitiesFor
from parser import RelTagParser, IRelTagParser

# register the rel-tag parser
provideUtility(RelTagParser,IRelTagParser,name="rel-tag")