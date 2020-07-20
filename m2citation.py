'''
Created on Feb 6, 2014

@author: qxt64851
'''
def checkParsing(inDir):
    
    if inDir['publisher'].strip() not in ['NCAS British Atmospheric Data Centre'
                                  ,'NERC Earth Observation Data Centre'
                                  ,'UK Solar System Data Centre'
                                  ,'IPCC Data Distribution Centre'
                                  ,'SPARC Data Centre'
                                  ]:
        print inDir['publisher']
        #sys.exit()


if __name__ == '__main__':
    
    inFile = 'c:/Users/qxt64851/Desktop/citation_table.html'
    outFile = 'c:/Users/qxt64851/Desktop/m2citations'
    
    import os
    import re
    
    a = open(inFile,'r')
    b = a.readlines()
    moles2Citations = []
    for i in range(1,len(b)):#range(2,len(b),6):
        if b[i].strip() != '{insert content here}':
            moles2string = b[i].strip('  <td>').strip('p> </p>').strip(' </td>\n').strip('</div>').strip('</p')
            if 'center> <table bgcolor="#d0e0ff"><tbody><tr><td>  <b> ' in moles2string:
                moles2string = moles2string[len('center> <table bgcolor="#d0e0ff"><tbody><tr><td>  <b> '):]
            moles2Citations.append(moles2string)
    counter = 0    
    for line in moles2Citations:
        counter +=1
        if line == '': continue
        if line == '{insert content here}': continue
        if line == 'n/a': continue
        
        # first spot and remove that last full stop that is sometimes there
        if line[-1:] == '.':
            line = line[:-1]
            
        # now lets remove bits at a time... working backwards!
        # 1st part URL extraction:
        
        authorList = None
        title = None
        publisher = None
        publishDate = None
        url = None 
        line = line.rstrip()
        lineParts = line.split(".")
        if 'Available from' in lineParts[-1]:
            url = lineParts[-1].split('Available from')
            #need to tidy URL is we want to use it... probably not though
        elif 'doi:' in lineParts[-1] :
            url = lineParts[-1].split('doi:')
            url = 'doi:' + url
            print 'doi: ', url
        elif 'DOI:' in lineParts[-1]:
            url - line.split('DOI:')
            url = 'DOI:' + url
            print 'DOI: ', url
        line = ".".join(lineParts[:-1])
        if 'Date of citation' not in line[-30:]:
            continue
        if line[-1] == '.': line = line[:-1]
        #print line.split('.')[-1:][0].split(',')
        pubBits =  line.split('.')[-1:][0].split(',')
#        if len(pubBits) < 3:
#            pubBits = ', '.join(line.split('.')[-2:])
#            pubBits = pubBits.split(',')
#        if len(pubBits) == 4 and pubBits[3] == '<i>':
#            pubBits = pubBits[0:2]
#        if len(pubBits) == 4:
#            bits = line.split('.')[0:1]
#            pubBits = [','.join(bits[0:1])].append(bits[2:3])
        publisher,publishDate = pubBits[0:2]
        #print publisher.strip(), publishDate
        if publisher.strip() == 'British Atmospheric Data Centre':
                publisher = 'NCAS ' + publisher.strip()
                
        if publisher.strip() not in ['NCAS British Atmospheric Data Centre'
                                  ,'NERC Earth Observation Data Centre'
                                  ,'UK Solar System Data Centre'
                                  ,'IPCC Data Distribution Centre'
                                  ,'SPARC Data Centre'
                                  ,'Langley Distributed Active Archive Center'
                                  ,'National Aeronautics and Space Administration'
                                  ,'European Space Agency'
                                  ,'Norwegian Institute for Air Research'
                                  ,'NCEO Earth Observation Data Centre'
                                  , 'Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC)'
                                  , 'Meteorological Institute, Free University Berlin'
                                  ]:
            continue #print line, publisher.strip()
        
        print counter    
        print publisher
   #     if 'citation' in pubBits[-1]:
   #         print pubBits[0].split(',')
       # if 'British Atmospheric Data Centre' not in line:
       #     print line
            
        # now to get publihser and publication dates
        
        
        
#        citeParts = line[::-1].split('.')
#        print citeParts
#        
#        authorList = citeParts[3][::-1].split(';')
#        title = citeParts[2][::-1].split('[Internet]')[0]
#        publisher,publishDate = citeParts[1][::-1].split(',')[0:2]
#        moreStuff = citeParts[1][::-1].split(',')
#        url = 'needed'
#        if len(citeParts) == 4: 
#            url = citeParts[0][::-1]
#        
#        print 'author:', authorList
#        print 'title:', title
#        print 'publisher:', publisher
#        print 'publish date:', publishDate
#        #print moreStuff
#        print 'url:', url
#        parsedCitation = {'authorList':authorList
#                        ,'title':title
#                        ,'publisher':publisher
#                        ,'publishDate': publishDate
#                        ,'url':url
#                         }
#        if checkParsing(parsedCitation) == 0:
#            print 'oo dear: check record: ', parsedCitation
#        
#        
#        #print 'line is:', line, counter
#        #print moles2Citations[counter-1]
        
    
    