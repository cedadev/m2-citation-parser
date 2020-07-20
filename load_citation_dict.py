from parse_citations import *
import re
from pprint import pprint

citation_dict = m2CitationDictReturn

def testAuthorsForCommas(d):
  for r in d.values():
    ali = r["authorList"]
    for au in ali:
        if au[0].find(",") > -1 or au[1].find(",") > -1: print au

def testPublishedDates(d):
  pattn = re.compile("^(\d{4})-?(\d{4})?$")
  for (key, r) in d.items(): 
    pd = r["publishedDate"]
    if len(pd) not in (4, 5, 9) or not pattn.match(pd):
        print pd
    try:
        year = int(r["publishedDate"].strip().replace("-", "")[:4])
    except:
        raise Exception("YEAR: |%s| %s" % (r["publishedDate"], key))


d = citation_dict

do_test = False
#do_test = True
if do_test:
    print "Running checks..."
    testPublishedDates(d)
    testAuthorsForCommas(d)
