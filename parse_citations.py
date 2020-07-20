import sys, re, collections
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.ERROR) #WARN)

class CitationUnpacker(object):
        """
        Class that takes in a MOLES2 citation string and returns various items.
        It carries out this task by firstly checking that it's not just a blank entry of some sort and
        then working backwards through the string. This approach was chosen as a full stop is used to split 
        the main components in the MOLES2 citations, but the author part can also use full stops after any
        initials and can be of arbitary lenght.
        
        Thus, once it has obtained the URI part it then strips out publication details.
        Next it obtains the title as used in the MOLES2 citation string (which won't necessarily be the same 
        as that in the MOLES2 record title field due to the changes made in the NERC Metadata checking that took place 
        in 2013-14).
        Finally, all that should be left is the string of authors. These are then assessed to first pull out any known 
        organisations, then it attempts to cope with the myriad of ways the authors names may have been given... and cope
        with the various ways that each author has been deliniated from one another - e.g. use of semi-colon or just a colon.
        """
        
        def __init__(self,m2string):
            """
            The initiallising step for the object
            """
                       
            self.etAlFlag = 0
            self.editorFlag = 0
            self.authorList = []
            self.authorDict = {}
            self.publishedDate = 'undefined'
            self.title = 'undefined'
            self.publisher = 'Undefined publisher'
            self.url = 'undefined'
            self.doiDate = ''
            
            # the following are useful lists/dictionaries used elsewhere in the citation string parsing.
            
            self.publisherDict = {'NCAS British Atmospheric Data Centre': 'NCAS British Atmospheric Data Centre (NCAS BADC)'
                                  ,'NERC British Atmospheric Data Centre': 'NCAS British Atmospheric Data Centre (NCAS BADC)'
                                  ,'NERC Earth Observation Data Centre': 'NERC Earth Observation Data Centre (NEODC)'
                                  ,'NCEO Earth Observation Data Centre': 'NERC Earth Observation Data Centre (NEODC)'
                                  ,'UK Solar System Data Centre': 'UK Solar System Data Centre (UKSSDC)'
                                  ,'UK Solar System Data Centre (UKSSDC)' : 'UK Solar System Data Centre (UKSSDC)'
                                  ,'IPCC Data Distribution Centre' : 'IPCC Data Distribution Centre (IPCC DDC)'
                                  ,'Infrared Sea Surface Autonomous Radiometer (ISAR) Team' : 'Infrared Sea Surface Autonomous Radiometer (ISAR) Team'
                                  ,'SPARC Data Centre' : 'SPARC Data Centre'
                                  ,'Langley Distributed Active Archive Center':'NASA Langley Research Center Distributed Active Archive Center (LaRC DAAC)'
                                  ,'NASA Langley DAAC':'NASA Langley Research Center Distributed Active Archive Center (LaRC DAAC)'
                                  ,'NASA Distributed Active Archive Center (DAAC)':'NASA Distributed Active Archive Center (DAAC)'
                                  ,'NASA Langley Research Center (DAAC)':'NASA Langley Research Center Distributed Active Archive Center (LaRC DAAC)' 
                                  ,'Goddard Distributed Active Archive Center (GDAAC)': 'Goddard Space Flight Center Distributed Active Archive Center (GSFC DAAC)'
                                  ,'Physical Oceanography Distributed Active Archive Center':'Physical Oceanography Distributed Active Archive Center (PO DAAC)'
                                  ,'Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC)':'Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC)'
                                  ,'National Snow and Ice Data Centre' : 'National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC)'
                                  ,'National Aeronautics and Space Administration': 'National Aeronautics and Space Administration (NASA)'
                                  ,'European Space Agency':'European Space Agency (ESA)'
                                  ,'Norwegian Institute for Air Research':'Norwegian Institute for Air Research'
                                  ,'Meteorological Institute, Free University Berlin':'Meteorological Institute, Free University Berlin'
                                  ,'STFC Rutherford Appleton Laboratory': 'STFC Rutherford Appleton Laboratory'# suspect this is incorrect - should be BADC
                                  ,'British Ocenanographic Data Centre': 'NERC British Ocenanographic Data Centre' # need to check if we're actually holding these data..
                                  }

            # this string is used to cope with lots of prefixes to surnames that exist
            self.surnamePrefixes = u"Mc\.?|Mac|[ODd]'|del|do|el|van\s[dD]er|[Vv]an|[dD]u|[Dd]e\s[l|L]a|[Dd]e|ter"
            
            
            # this is used to cope with unicode instances in the author names
            self.lowerUnis = u"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc"
            #self.lowerUnis = u"\xc3\xe0\xc3\xe1\xc3\xe2\xc3\xe3\xc3\xe4\xc3\xe5\xc3\xe6\xc3\xe7\xc3\xe8\xc3\xe9\xc3\xea\xc3\xeb\xc3\xec\xc3\xed\xc3\xee\xc3\xef\xc3\xf0\xc3\xf1\xc3\xf2\xc3\xf3\xc3\xf4\xc3\xf5\xc3\xf6\xc3\xf8\xc3\xf9\xc3\xfa\xc3\xfb\xc3\xfc"
            
            self.upperUnis = u"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
            
            # this needs to be ordered as the matching carried out against this list will work it's way through the list... thus a fuller name
            # with an element such as NASA has to be checked ahead of just NASA on it's own, otherwise we end up splitting up an organisation's full
            # name into different organisations.
            
            self.orgDict = collections.OrderedDict([('National Aeronautics and Space Administration, Langley','NASA Langley Research Center (NASA Langley)')
                            ,('National Aeronautics and Space Administration, Goddard Space Flight Center','NASA Goddard Space Flight Center (NASA Goddard)')
                            ,('NASA Goddard Space Flight Center','NASA Goddard Space Flight Center (NASA Goddard)')
                            ,('NASA Goddard Institute for Space Studies','NASA Goddard Institute for Space Studies (NASA GISS)')
                            ,('Goddard Institute for Space Studies', 'NASA Goddard Institute for Space Studies (NASA GISS)')
                            ,('National Aeronautics and Space Administration (NASA)','National Aeronautics and Space Administration (NASA)')
                            ,('National Aeronautics and Space Administration', 'National Aeronautics and Space Administration (NASA)')
                            ,('National Oceanic and Atmospheric Administration','National Oceanic and Atmospheric Administration (NOAA)')
                            ,('NASA Ames Research Center','NASA Ames Research Center')
                            ,('NASA Ames','NASA Ames Research Center')
                            ,('NASA Jet Propulsion Laboratory','NASA Jet Propulsion Laboratory (NASA JPL')
                            ,('NASA Langley','NASA Langley Research Center (NASA Langley)')
                            ,("NASA's Land Surface Hydrology program",'NASA Land Surface Hydrology Program')
                            ,('NASA', 'National Aeronautics and Space Administration (NASA)')
                            ,('National Centers for Environmental Prediction','National Centers for Environmental Prediction')
                            ,('United States Geological Survey','United States Geological Survey (USGS)')
                            ,('Jet Propulsion Laboratory','NASA Jet Propulsion Laboratory (NASA JPL)')
                            ,('the Higher Education Funding Council for Wales (HEFCW)','the Higher Education Funding Council for Wales (HEFCW)')
                            ,('Science and Technology Facilities Council, Rutherford Appleton Laboratory, Molecular Spectroscopy Facility', 'STFC Rutherford Appleton Laboratory Molecular Spectroscopy Facility (MSF)')
                            ,('Science and Technology Facilities Council (STFC)', 'Science and Technology Facilities Council (STFC)')
                            ,('Science and Technology Facilities Council', 'Science and Technology Facilities Council (STFC)')
                            ,('STFC Rutherford Appleton Laboratory', 'STFC Rutherford Appleton Laboratory (STFC RAL)')
                            ,('Council for the Central Laboratory of the Research Councils (CCLRC)','Council for the Central Laboratory of the Research Councils (CCLRC)')
                            ,('CCLRC','Council for the Central Laboratory of the Research Councils (CCLRC)')
                            ,('Rutherford Appleton Laboratory','Rutherford Appleton Laboratory')
                            ,('Chilboloton Observatory', 'Chilbolton Facility for Atmospheric and Radio Research (CFARR)')
                            ,('Chilbolton Observatory', 'Chilbolton Facility for Atmospheric and Radio Research (CFARR)')
                            ,('Chilbolton Facility for Atmospheric and Radio Research', 'Chilbolton Facility for Atmospheric and Radio Research (CFARR)')
                            ,('Molecular Spectroscopy Facility (MSF)','STFC Rutherford Appleton Laboratory Molecular Spectroscopy Facility (MSF)')
                            ,('Science and Engineering Research Council (SERC)','Science and Engineering Research Council (SERC)')
                            ,('Natural Environment Research Council, Centre for Ecology and Hydrology, Wallingford','NERC Centre for Ecology and Hydrology Wallingford (CEH Wallingford)')
                            ,('Natural Environment Research Council, Aberystwyth Radar Facility','Natural Environment Research Council Mesosphere-Stratosphere-Troposphere Radar Facility (MSTRF)')
                            ,('Natural Environment Research Council, National Centre for Earth Observation', 'NERC National Centre for Earth Observation (NCEO)')
                            ,('Natural Environment Research Council (NERC)', 'Natural Environment Research Council (NERC)')
                            ,('Natural Environment research Council (NERC)','Natural Environment Research Council (NERC)')
                            ,('Natural Environment Research Council', 'Natural Environment Research Council (NERC)')
                            ,('Natural Environment Research Council Airborne Research and Survey Facility','NERC Airborne Research and Survey Facility (ARSF)')
                            ,('NERC', 'Natural Environment Research Council (NERC)')
                            ,('British Antarctic Survey','British Antarctic Survey (BAS)')
                            ,('NCAS British Atmospheric Data Centre','NCAS British Atmospheric Data Centre (NCAS BADC)')
                            ,('National Centre for Atmospheric Sciences','National Centre for Atmospheric Sciences (NCAS)')
                            ,('NCAS-CGAM (Centre for Global Atmospheric Modelling)','NCAS Centre for Global Atmospheric Modelling (NCAS-CGAM )')
                            ,('Universities Facility for Atmospheric Measurement (UFAM)', 'Universities Facility for Atmospheric Measurement (UFAM)')
                            ,('FAAM', 'Facility for Airborne Atmospheric Measurements (FAAM)')
                            ,('World Data Centre (WDC) at UK Solar System Data Centre (UKSSDC)','World Data Centre (WDC) at UK Solar System Data Centre (UKSSDC)')
                            ,('UK Solar System Data Centre (UKSSDC)','UK Solar System Data Centre (UKSSDC)')
                            ,('EISCAT Scientific Association','EISCAT Scientific Association')
                            ,('Worldwide Ionospheric Stations','Worldwide Ionospheric Stations')
                            ,('The Stratospheric Processes And their Role in Climate (SPARC)','The Stratospheric Processes And their Role in Climate (SPARC)')
                            ,('CHIANTI Team','CHIANTI Team')
                            ,('Norwegian Institute for Air Research','Norwegian Institute for Air Research NILU)')
                            ,('European Centre for Medium-Range Weather Forecasts (ECMWF)', 'European Centre for Medium-Range Weather Forecasts (ECMWF)')
                            ,('European Centre for Medium-Range Weather Forecasts', 'European Centre for Medium-Range Weather Forecasts (ECMWF)')
                            ,('European Centre Medium Range Weather Forecasting', 'European Centre for Medium-Range Weather Forecasts (ECMWF)')
                            ,('European Centre for Medium Range Weather Forecasting','European Centre for Medium-Range Weather Forecasting (ECMWF)')
                            ,('ECMWF', 'European Centre for Medium-Range Weather Forecasts (ECMWF)')
                            ,('UK Meteorological Office, Hadley Centre','Met Office Hadley Centre')
                            ,('UK Meteorological Office, Remote Sensing Branch, Farnborough','Met Office Remote Sensing Branch Farnborough (Met Office RSI)')
                            ,('UK Meteorological Office', 'Met Office')
                            ,('Meteorological Office','Met Office')
                            ,('Met Office, Hadley Centre', 'Met Office Hadley Centre')
                            ,('Met Office Hadley Centre', 'Met Office Hadley Centre')
                            ,('Hadley Centre', 'Met Office Hadley Centre')
                            ,('Met Office, Cardington','Met Office Meteorological Research Unit Cardington')
                            ,('Met Office', 'Met Office')
                            ,('CSIRO (Scientific and Industrial Research for Australia), Australia','The Commonwealth Scientific and Industrial Research Organisation (CSIRO, Australia)')
                            ,('and NIWA (National Institute of Water and Atmospheric Research), New Zealand','National Institute of Water and Atmospheric Research (NIWA, New Zealand)')
                            ,('National Institute of Water and Atmospheric Research, New Zealand','National Institute of Water and Atmospheric Research (NIWA, New Zealand)')
                            ,('QinetiQ','QinetiQ')
                            ,('Environmental Systems Science Centre (ESSC)', 'Environmental Systems Science Centre (ESSC)')
                            ,('Twentieth Century Reanalysis Project Participants', 'Twentieth Century Reanalysis Project Participants')
                            ,('AMAZONICA', 'AMAZONICA')
                            ,('Royal Netherlands Meteorological Institute (KNMI)', 'Royal Netherlands Meteorological Institute (KNMI)')
                            ,('EUMETSAT', 'EUMETSAT')
                            ,('(DEFRA)','Department for Environment, Food and Rural Affairs (DEFRA)')
                            ,('European Space Agency','European Space Agency (ESA)')
                            ,('ESA','European Space Agency (ESA)')
                            ,('International Satellite Cloud Climatology Project (ISCCP)', 'International Satellite Cloud Climatology Project (ISCCP)')
                            ,('University of East Anglia Climatic Research Unit (CRU)', 'University of East Anglia Climatic Research Unit (CRU)')
                            ,('National Centre for Earth Observation', 'National Centre for Earth Observation (NCEO)')
                            ,('Coastal Air Pollution Project Participants', 'Coastal Air Pollution Project Participants')
                            ,('Weybourne Atmospheric Observatory','Weybourne Atmospheric Observatory')
                            ,('UK Royal Society','UK Royal Society')
                            ,('Royal Observatory Greenwich','Royal Observatory Greenwich')
                            ,('University of Oslo','University of Oslo')
                            ,('University of Oxford Atmospheric, Oceanic and Planetary Physics','University of Oxford Atmospheric Oceanic and Planetary Physics (AOPP)')
                            ,('University of Oxford','University of Oxford')
                            ,('University of Edinburgh','University of Edinburgh')
                            ,('University of Sunderland','University of Sunderland')
                            ,('The Open University','The Open University')
                            ,('British National Space Centre','British National Space Centre (BNSC)')
                            ,('Intergovernmental Oceanographic Commission (IOC)','Intergovernmental Oceanographic Commission (IOC)')
                            ,('Armagh Observatory','Armagh Observatory')
                            ,('Fundacion Entropika','Fundacion Entropika')
                            ,('Lancaster University','Lancaster University')
                            ,('Canadian Defence Research Board','Canadian Defence Research Board')
                            ,('Committee on Space Research (COSPAR)','Committee on Space Research (COSPAR)')
                            ,('Swedish Board for Space Activities','Swedish Board for Space Activities')
                            ,('Max Planck Institute for Meteorology','Max Planck Institute for Meteorology (MPI-M)')
                            ,('Laboratoire de Meteorologie Dynamique','Laboratoire de Meteorologie Dynamique (LMD)')
                            ,("Laboratoire des Sciences du Climat et de l'Environnement","Laboratoire des Sciences du Climat et de l'Environnement")
                            ,('Bodeker Scientific','Bodeker Scientific')
                            ,('Centre for International Climate and Environment Research - Oslo (CICERO)','Centre for International Climate and Environment Research - Oslo (CICERO)')
                            ,('Intermap Technologies','Intermap Technologies')
                            ,('Landmap','Landmap')
                            ,('The GeoInformation Group','The GeoInformation Group (TGG)')
                            ,('Bluesky','Bluesky')
                            ,('GetMapping','GetMapping')
                            ,('RapidEye','RapidEye')
                            ,('Infrared Sea Surface Temperature Autonomous Radiometer (ISAR) Team','Infrared Sea Surface Temperature Autonomous Radiometer (ISAR) Team')
                            ,('UK Multi-Mission Product Archive Facility (UK-MM-PAF)/Infoterra Ltd','UK Multi-Mission Product Archive Facility (UK-MM-PAF)/Infoterra Ltd')
                            ,('UK Multi-Mission Product Archive Facility (UK-MM-PAF)/Astrium GEO-Information Services','UK Multi-Mission Product Archive Facility (UK-MM-PAF)/Astrium GEO-Information Services')
                            ,('Disaster Monitoring Constellation International Imaging','DMC International Imaging Ltd. (DMCII)')
                            ,('DMC International Imaging Ltd','DMC International Imaging Ltd. (DMCII)')
                            ,('Canadian Centre for Climate Modelling and Analysis computing facility','Canadian Centre for Climate Modelling and Analysis computing facility (CCCma)')                      
                            ,('the Center for International Climate and Environmental Research - Oslo (CICERO)','the Center for International Climate and Environmental Research - Oslo (CICERO)')
                            ,('DLR German Institute for Atmospheric Physics','DLR German Institute for Atmospheric Physics')
                            ,('Geophysical Fluid Dynamics Laboratory (GFDL)','Geophysical Fluid Dynamics Laboratory (GFDL)')
                            ,('Lawrence Livermore National Laboratory','Lawrence Livermore National Laboratory (NCAR LLNL)')
                            ,('Meteo-France','Meteo-France')
                            ,('MeteoFrance','Meteo-France')
                            ,('Atmospheric Chemistry and Climate Model Intercomparison Project Participants','Atmospheric Chemistry and Climate Model Intercomparison Project Participants')
                            ,('International Union of Pure and Applied Chemistry','International Union of Pure and Applied Chemistry')
                            ,('Centre for Climate System Research / National Institute for Environmental Studies, Japan','Centre for Climate System Research / National Institute for Environmental Studies, Japan')
                            ,('Program for Climate Model Diagnosis and Intercomparison','Program for Climate Model Diagnosis and Intercomparison (PCMDI)')
                            ,('Meteorological Institute, Free University Berlin','Meteorological Institute Free University Berlin')]
                            )
            
            
            
            self.m2string = m2string[0]
            self.m2url = m2string[1]

            # first up - do a quick tidy up of the string to remove/replace bad characters that could make parsing difficult otherwise...

            self.m2string = self.stringTidy(self.m2string)

            self.initialCheck()
            # now carring out that first check to ensure that we've for a valid citation string to parse...
            # otherwise return blank entries
            
            if not self.ignore == 1:
                
                # we're going to do the actual parsing here...
                try:
#                    if 'Natural Environment Research Council, [Bower, K.; Butt ,D; Foxton, A.]' in self.m2string:
#                        log.info('check')
                    
                    
                    
                    self.getPubNUrl()  # this bit gets the publication URL/DOI part and then the publication details
                    self.getTitle() # then we get the title string back
                    self.getAuthors() # finally we attempt to sort out the remaining text to get some authors back
                    
                except:
                    # but, woe... if there is some problem with the above the script will throw a wobbly,
                    # so we capture that issue bu flagging up it's MOLES2 URL to be checked out...
                    log.info("MOLES2 URL: %s" % self.m2url)
                    
        def initialCheck(self): 
            '''
            does a quick check for common empty MOLES2 citations
            '''
            self.ignore = 0
            
            if '{insert content here}' in self.m2string:
                print self.m2string
                print 'stop'
            if self.m2string.strip() in [''
                       ,'{insert content here}'
                       ,'n/a'
                       ,'Please contact the <a href="http://badc.nerc.ac.uk/help/contact.html">CEDA Helpdesk for details'
                       ,'Please contact the <a href="http://badc.nerc.ac.uk/help/contact.html">CEDA Helpdesk</a> for details.'
                       ,'Please contact the <a href="mailto:badc@rl.ac.uk">BADC help desk.'
                       ,'Please contact the <a href="mailto:badc@rl.ac.uk">BADC help desk'
                       ,'Please contact BADC for details'
                       ,'TBC']:
                self.ignore = 1
             
               
        def stringTidy(self,objectToTidy):
            '''
            Now we can quickly remove some pesky little tagging that has sneaked in
            '''
            
            # first let's make some lists of common items to strip out...
            thingsToRemove = ['<td>','</td>','<TD>','</TD>'
                              ,'<tr>','</tr>','<TR>','</TR>'
                              ,'<p>','</p>','<p />','<P>','</P>','<P />'
                              ,'\n'
                              ,'<div>','</div>'
                              ,'<b>','</b>','<B>','</B>'
                              ,'<center>','</center>','<CENTER>','</CENTER>'
                              ,'</a>','</A>'
                              ,'<ul>','</ul>','<UL>','</UL>'
                              ,'<li>','</li>'
                              ,'<font>','</font>','<FONT>','</FONT>'
                              ,'<tbody>','</tbody>','<TBODY>','</TBODY>'
                              ,'<blockquote>','</blockquote>'
                              ,'<table bgcolor=#d0e0ff>','<font color=#0000aa>','<table bgcolor="#d0e0ff">']
            # and dictionary of items to replace and what with..... which will help with parsing later on..                
            thingsToReplace = [('<em>','<i>')
                                ,('</em>','</i>')
                                ,('. [Internet]',', [Internet]')
                                ,(', available from','. Available from')
                                ,('INTERNET','Internet')
                                ,(',<i> [Internet]', '<i>, [Internet]')
                                ,('DOI:','doi:')
                                ,('of citation.</i>','of citation</i>.')
                                ,('Please contact the <a href="mailto:badc@rl.ac.uk">BADC help desk</a>.','Undefined')
                                ,('.  [Internet].',', [Internet].')
                                ,('Data Centre.','Data Centre,')
                                ,('Date of citation,','Date of citation')
                                ,('Met. Research Flight','Met.Research Flight')
                                ,('c  Data Centre, CORRAL','c Data Centre. CORRAL')
                                ,('[Internet] NCAS','[Internet]. NCAS')
                                ,('Research Center, DAAC. 1993,','Research Center (DAAC), 1993,')]
            # then do the stripping out step...
            for item in thingsToRemove:
                objectToTidy = objectToTidy.replace(item, '')
            # and the replacement step...
            for key,item in thingsToReplace:
                objectToTidy = objectToTidy.replace(key,item)
            
            # but we've also got some pernickerty bits that we need to pick and deal with in another way....
            objectToTidy = re.sub("<a href='(?P<uriType>http:|doi:)(?P<uriString>\/\/.*[\r\n])*'",'', objectToTidy)
            objectToTidy = re.sub("(?!\,)(<\/i> \[Internet\])",'</i>, [Internet]',objectToTidy)
            #need to remove instances of <a href=""> and </a>
            
            # and remove anything other blank spaces at the start or end...
            
            objectToTidy = objectToTidy.strip()

            # and because of inconsistency of having a full stop at the end or not:
            if objectToTidy[-1:] == '.':
                objectToTidy = objectToTidy[:-1]
            return objectToTidy

        # the next lot of def statements are dealing with the citation string parsing itself
        
        def getPubNUrl(self):
            '''
            The first parsing step after the initial clean up,
            It remove different bits at a time from the string, working backwards as the 
            author list could be all over the shop!
            First up - the URI string - to get either the DOI or the http link
            and so deal with these as appropriate...
            
            '''
            
            # so.. let's get the URI string
            uriSearchString = '(?P<uriString>(http|doi)(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?)'#'(?P<uriString>(http|doi):(\/{1,2}).*)'
            url = re.search(uriSearchString,self.m2string)
            
            if url != None:

                # having found the URI string we'll pop that into an object's attribute list to return later on..
                self.url = url.groupdict()['uriString']
                
                # and strip that out from the string we'll be parsring as we go along
                self.m2string = self.m2string.replace(self.url, '') 
                
                
            else :
                # but if there isn't one found then we'll simply use the moles2 URL that we've got from elsehwere...

                self.url = self.m2url
            
            # time to tidy up the citation string ...
            # first let's strip out the following text off the end (if it is there...)
            availableSearch = '.\s?(Available|Availbable) from'
            
            
            if re.search(availableSearch,self.m2string.strip()):
                self.m2string = re.sub(availableSearch,'',self.m2string.strip()).strip()
                #self.m2string = self.m2string.replace('. Available from', '').strip()
            
            # and remove a trailing full stop if it is hangling about...
            if self.m2string.strip()[-1] == '.':
                self.m2string = self.m2string.strip()[:-1]
            
            # Now to get the publication details, but 
            # we'll handle things slightly differently depending on whether or not
            # we're dealing with a DOI-ed dataset or not...
            
            # by this point the last section of the citation string should have 
            # the publication details in it...


            # so again, dealing with content from the end of the citation string... split it  to pull back the publication bits

            pubBits =  self.m2string.split('.')[-1:][0].split(',')

            # now to handle things differnetly for the DOI-ed data...
            
            if 'doi' in self.url:
                # for DOI-ed data we've not got a "date of citation" to cope with... 
                # instead we'll have a DOI publication date !
                # and in some cases we'll still have that all inportant publication year to get back too
                    
                if len(pubBits) == 2:
                    # there might be a lack of publication year - someone stripped it out in the past, so we've lost it... or the 
                    # publiation info wasn't deliniated properly with commas...
                    self.doiDate = pubBits[1]
                    # so instead we'll attempt to pull this back from re-joining the publication string
                    # and searching for a year there.. this will cope with either a missing publication year 
                    # OR the string wasn't properly delinated...
                    self.publishedDate = re.search('19|20\d{2}',', '.join(pubBits)).group()
                
                if len(pubBits) == 3:
                    # but in these cases we DO have the publication year - hurrah! so this is straight forward
                    self.doiDate = pubBits[2]
                    self.publishedDate = pubBits[1]    

                # and the first bit should, in theory, be the publisher.. 
                self.publisher = pubBits[0].strip()

            
            # now, for all the other non DOI-ed cases we'll do the following...
            # first check to see if we've a "data of citation" bit in there.. otherwise we'll handle things differnetly
                
            elif re.search('(D|d)at(e|a) of (C|c)itation',self.m2string):

                if len(pubBits) == 3:
                    # simply collate the bits of info needed as this conforms to what we're expecting   
                    self.publisher,self.publishedDate = pubBits[0:2]
                
                else:
                    # but this case doesn't!!!
                    
                    log.warn('Need to check this sort of line by hand: %s' % self.m2string)
                    
                    self.publisher = pubBits[0].strip()
                    if pubBits[0].strip() ==  'Meteorological Institute' and pubBits[1].strip() == 'Free University Berlin':
                        self.publisher = 'Meteorological Institute, Free University Berlin'
            else:
                log.warn('record without date of citation: %s %s' % (self.m2url, self.m2string))
            
            # now do some checks on the publisher
            
            if self.publisher.strip() == 'British Atmospheric Data Centre':
                self.publisher = 'NCAS ' + self.publisher.strip()
            
            self.publisher = self.publisher.strip()
            # and some tidying up of problem publishers...
            if self.publisher in ['NCAS - British Atmospheric Data Centre','NCAS-British Atmospheric Data Centre','NCAS British Atmopspheric Data Centre']:
                self.publisher = 'NCAS British Atmospheric Data Centre'

            # if it's not a publisher that we're expecting... we use this step to capture it.        
            
            if self.publisher.strip() not in self.publisherDict.keys():
                log.warn('New publisher to check: %s'% self.publisher)
                print self.publisher
                self.publisher = 'Undefined publisher' 
                
            # and now were going to standardise some of the publishers using the publisherDict dictionary: 

            self.publisher = self.publisherDict[self.publisher]
            
            # and tify up the publication date
            self._tidyPublishedDate()
            
            # and return the rest of the citation string for parsing in the next step...
            
            self.m2string = ".".join(self.m2string.split('.')[:-1])
            
            
            
            
        def _tidyPublishedDate(self):
            """
            Cleans up the published date.
            """
            pd = self.publishedDate
            if pd.strip() == "": pd = "undefined"
            if pd == "undefined": return

            pd = pd.replace(" ", "").strip()
            self.publishedDate = pd


            
        def getTitle(self):
            '''
            This step will parse the citation string to extract the title from it
            Again, working backwards to avoid the issue of the author list
            
            '''
            splitTitleOn = '.'
            
            # done this as have to cope with titles with dots in there - e.g. CRU data v 8.9 or Jan.1989
            # Hopefully MOLES2 citations have been altered to cope with this fact now.
            
            titleSplitter = re.search('\.\s',self.m2string) 
            
            if titleSplitter:
                splitTitleOn = '. '
            
            # so now to get the title string back...
            titleString = self.m2string.split(splitTitleOn)[-1].replace("[Internet]",'')    
            
            # and tidy it up a bit...
            self.title = self.stringTidy(titleString).replace('<i>','').replace('</i>','')
            if self.title[-1] == ',':
                self.title = self.title[:-1]
            
            
            # and return what is left ready for author parsing
            self.m2string = ".".join(self.m2string.split(splitTitleOn)[:-1])
            self.startingAuthorString = self.m2string
            

            
        def getAuthors(self):
            '''
            Finally, parsing what's left of the citation string
            which should now be the author list 
            things we need to cope with are:
            1) use of [] for list of named individuals 
            2) use of "et al."
            3) use of "eds" for an indication of editors used in the citation
            4) use of individual names and organisation names
            5) use of acronyms
            6) mixture of "," and ';' to separate each author
            
            '''
                
            # clean up the list first of all

            authorString = self.stringTidy(self.m2string).replace('<i>',' ').replace('</i>','').strip()
           
           
            authorString = authorString.replace('Nordli A;','Nordli O')
           
            # now do some checks for how it's structured to see if there are commas, semi-colons or square brackets present
            if 'Citation: Natural Environment Research Council' in authorString:
                print 'STOP'
            semiColonSplitter = re.search(';',authorString)
            squareSplitter = re.search('\[.*',authorString)
            commaSplitter = re.search(',',authorString)
            
            subAuthorString = ''
            
            # and checking for "et al." and "eds" as special cases
            
            etAlAuthor = re.search('(\.|\s)et\.?\s?al',authorString)
            editorAuthor = re.search('\seds\.', authorString)
            self.etAlFlag = 0
            self.editorFlag = 0
            self.authorList = []
            self.authorDict = {}
            
            
            if etAlAuthor:
                # et. al will be last named author in the list, but we'll pull it out here
                # so that it doesn't interfere with later parsing
                
                self.etAlFlag = 1
                # with a high location number will definitely be at the end.
                self.authorDict['9999'] = ('','et. al','ind')
                 
                authorString = re.sub('\set\.?\s?al', '', authorString)
            if editorAuthor:
                # et. al will be last named author in the list, but we'll pull it out here
                # so that it doesn't interfere with later parsing
                
                self.editorFlag = 1
                # with a high location number will definitely be at the end.
                self.authorDict['99999'] = ('','editors','ind')
                 
                authorString = re.sub('\seds\.', '', authorString)

            if not (semiColonSplitter or squareSplitter or commaSplitter):
                # simple case of just one named author
                self.prepareAuthDict(authorString)
                
                
            else:
                # So, it looks like it's not just one author, so we'll need to start doing something a little more complex...
                
                # first let's pull out known orgs first here and strip from string to limit interference
            
                
                for key in self.orgDict.keys():
                    if key in authorString:
                        self.prepareAuthDict(key)
                        key = key.replace('(','\(').replace(')','\)')
                        
                        authorString = re.sub(key+'(P:;|,|\.|\s)?','',authorString).strip()
            
            # now go on to parse what is left        
            
                if semiColonSplitter:
                    # if there is semi-colons used to deliniate the authors.....
                    
                    #originalAuthorString = authorString
                
                    if squareSplitter:
                        # and there might be a list in square brackets too...
                        
                        authorStringBits = authorString.split('[')
                        authorString = authorStringBits[0].strip()
                        subAuthorString = authorStringBits[1].strip(']')

                    if authorString.strip() != '':
                        #we'll always attempt to do this if we have anything left after stripping the organisations out....
                        #first some tidying up....
                        
                        if authorString[-1] == ';':
                            authorString = authorString[:-1]

                        if authorString.strip() == 'and':
                            authorString = ''  
                        # now to handle the remaining text and look for authors...
                        
                        if authorString.strip() != '' :
                            # as we may not have a consistent approach we'll still check for semi-colons or colons as deliniators:
                            if re.search(';',authorString):
                                self.authorList.extend(authorString.strip().split(';'))
                            elif re.search(',', authorString):
                                self.authorList.extend(self.handleCommaSplits(authorString))
                            else:
                                # and a flag in case there's some other issue!!!
                                print 'main author string needs alt splitting!: ', authorString, self.m2string
                                # this next bit is a hang over from earlier scripts, but we'll leave it just in case there are still some odd records...
                                if 'Internet' in authorString :
                                        authorString = 'incorrect'
                                
                    if squareSplitter:
                        # now to deal with any list of authors given in square brackets...
                        if re.search(';',subAuthorString):
                            self.authorList.extend(subAuthorString.split(';'))
                        elif re.search(',',subAuthorString):
                            self.authorList.extend(self.handleCommaSplits(subAuthorString))
                        elif 'Internet' in subAuthorString :
                                    subAuthorString = 'incorrect'
                        else:
                            # and if none of the above we'll assume it's one named author...
                            log.info('Assuming just one author!: %s %s' % (subAuthorString, self.m2string))
                            self.authorList.append(subAuthorString)
                
                else:
                    # if no splitting apparent then we can safely assume it's just one author:
                    if not re.search(',',authorString) and not squareSplitter:
                        self.authorList.append(authorString)
                    else:

                        # first lets pull apart the sub-list of authors....

                        if squareSplitter:
                            authorStringBits = authorString.split('[')
                            authorString = authorStringBits[0].strip()
                            subAuthorString = authorStringBits[1].strip(']')
                            # pass out the sub list to the function to handle comma split authors...
                            self.authorList.extend(self.handleCommaSplits(subAuthorString))
                        
                        # and now for those authors before the square brackets.... if any...    
                        if authorString != '':
                            if authorString[-1] == ',':
                                authorString = authorString[:-1]
                            # again throwing out to the function handling comma split authors...
                            self.authorList.extend(self.handleCommaSplits(authorString))
                # need to parse these lists now
                # once we've got out authors split out we'll then try and parse them through one more function to get them ready for the author dictionary...
                for author in self.authorList:
                    if author.strip() != '':
                        self.prepareAuthDict(author.strip())

        def handleCommaSplits(self,listToDo):
            '''
            an attempt to parse strings with comma as field splitter 
            when it might also be used to split last name, initials
            This is done first by looking for names ordered as Firstname lastname, firstname lastname
            Then the more complex case of Lastname, I, Lastname, II
            In both cases they have to deal with various issues:
            1) firstname can be Graham Alexander: Graham A: GA G.A. etc etc. and hypenated names
            2) lastname might also have other components such as prefixes (de, Van der, Mc, O' etc), Hyphenated names and suffixes (e.g. Ewell III)
            '''
            indiSearch1 = u"(?<![A-Z\.]{1})(?:(?:(?:(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]{2,}(?:\s[A-Z"+ self.upperUnis + u"]{1}\.?)+\s)|(?:[A-Z"+ self.upperUnis + u"]{1}\.?){1,3}))\s*(?:(?:"+ self.surnamePrefixes + u")?\s?(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]+\-?){1,2}(?:\s[JS]r\.?)?(?<![A-Z"+ self.upperUnis + u"]{2})))"
            indiSearch2 =u"(?:(?:" + self.surnamePrefixes + u")?\s?(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]+\-?){1,2}(?:\sJr)?(?:[\s,]{0,3})(?:[A-Z"+ self.upperUnis + u"]{1}\.?){1,3}(?![a-z"+ self.lowerUnis + u"]+))"
                   
            foundList = []
            firstTest = re.findall(re.compile(indiSearch1,re.UNICODE),listToDo)
            # so we do the first test...
            if firstTest != []:
                foundList.extend(firstTest)
            # and if that fails to find anything we pass to the second test...
            elif re.search(indiSearch2,listToDo):
                secondTest = re.findall(re.compile(indiSearch2,re.UNICODE),listToDo)
                foundList.extend(secondTest)
                
            # and if that fails then we're just going to split what remains to get something back....
            else:
                foundList.extend(listToDo.split(','))
            
#            foundList = re.findall(commaSearch,listToDo)
            
            
            log.info('list is: %s' % str(foundList))
            return foundList 

            
        def prepareAuthDict(self,author):

            """
            # Now to prepare items for the author dictionary....
            
            first take the author's name and check to see if it is a known organisation - this step will also translate it over to a standardised name
            
            then we attemp to to parse the name to work out what order it is... it could be First name, last name or last name, first name
            In both cases they have to deal with various issues:
            1) firstname can be Graham Alexander: Graham A: GA G.A. etc etc. and hypenated names
            2) lastname might also have other components such as prefixes (de, Van der, Mc, O' etc), Hyphenated names and suffixes (e.g. Ewell III)
            
            as part of the preparation for the author list it will idenity the first and last parts of the name, the type of record - org/ind - and 
            where in the string it appears... this latter info will be used to then order the list later on when it is returned.
            
            """            
            
            #quickly set up some extra dictionaries of unusual cases we'll hanlde in a bespoke fashion...
            self.jrDict = collections.OrderedDict([('Gleason Jr BE',['BE','Gleason Jr'])])
            
            #Hernandez\s|de\sFatima
            self.oddNamesDict = collections.OrderedDict([('Hernandez Gonzales, F.',['F.','Hernandez Gonzales'])
                                                         #,('Br\xc3',['S', 'Br\xc3\xb6nnimann'])
                                                         #,('Nordli \xc3',['\xc3\x98','Nordli'])
                                                         ,('Br\xc3',['Ag', 'LookAtThis1'])
                                                         ,('Nordli \xc3',['Ag','LookAtThis2'])
                                                         ,('de Fatima Jardim, M.',['M.','de Fatima Jardim'])])
            
            
            # now to handle those odd names...
            if self.oddNamesDict.has_key(author):
                originalAuthor = author.replace('(','\(').replace(')','\)')
                authType = 'ind'
                firstname = self.oddNamesDict[author][0]
                lastname = self.oddNamesDict[author][1]
                matchedName = re.search(originalAuthor,self.startingAuthorString)
                
            
            elif self.jrDict.has_key(author):
                originalAuthor = author.replace('(','\(').replace(')','\)')
                authType = 'ind'
                firstname = self.jrDict[author][0]
                lastname = self.jrDict[author][1]
                matchedName = re.search(originalAuthor,self.startingAuthorString)
                
            # having handled those odd instances we'll check for known organisations..
                
            elif self.orgDict.has_key(author):
                authType = 'org'
                originalAuthor = author.replace('(','\(').replace(')','\)')
                lastname = self.orgDict[author]
                firstname = ''
                matchedName = re.search(originalAuthor,self.startingAuthorString)

            else:
                matchedName = re.search(author.replace('(','\(').replace(')','\)'),self.startingAuthorString)
            
                # now lets work out the location so we can determine order later on    
            
                # will use the location as the key as then we can order on this easily later on
                # to then construct the final list to feed back to Ag
                
                # this first search looks for First Name then Lastname ordering
                # the second search looks for Lastname, Firstname ordering
                
                    
                indiSearch1 = u"(?<![A-Z\.]{1})(?P<firstname>(?:(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]{2,})|(?:[A-Z"+ self.upperUnis + u"]{1}\.?){1,3}))\s*(?P<lastname>(?:" + self.surnamePrefixes + u")?\s?(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]+\-?){1,2}(?![A-Z]{1}))"
                    
                indiSearch2 = u"(?P<lastname>(?:" + self.surnamePrefixes + u")?\s?(?:[A-Z"+ self.upperUnis + u"]{1}[a-z"+ self.lowerUnis + u"]+\-?){1,2}(?:\sJr)?)[\s,]{0,3}(?P<firstname>(?:[A-Z"+ self.upperUnis + u"]{1}[\.\-]?){1,3}(?![a-z"+ self.lowerUnis + u"]+))"
                
                nameTest = re.search(re.compile(indiSearch1, re.UNICODE),author)
                
                if not nameTest:
                    nameTest = re.search(re.compile(indiSearch2, re.UNICODE),author)
                
                # and if neither of those tests work we'll assume it's an organistion...
                
                if not nameTest:
                    if len(author.strip().split(' ')) != 2:
                        authType = 'org'
                        firstname = ''
                        lastname = author
                else:
                    # if either DID work, though, then we've got the parts of the name we want ... for an individual!! Hurrah!
                    
                    firstname = nameTest.groupdict()['firstname']
                    lastname = nameTest.groupdict()['lastname']
                    authType = 'ind'
        
            if authType == 'org' and re.search(',', lastname) and not re.search('\(',lastname) and not self.orgDict.has_key(author):
                # but just in case we've made one slip up earlier on, we'll quickly check those orgs again....
                ### check about free uni, berlin thingy....
                print lastname
                if firstname == '':
                    lastname,firstname = lastname.split(',')
                    authType = 'ind'
            
            
                
                
            # do a bit of tidying up...
            firstname = firstname.strip()
            lastname = lastname.strip()
            # and get the location of the autor in the citation string for later ordering...
            keyString = matchedName.start() 

            # now to add those details in to the author dictionary... which shoudl be unique... 
            if not self.authorDict.has_key(keyString):
                self.authorDict[keyString] = (firstname,lastname,authType)
            else:
                # and a warning if it's not unique...
                log.warn('Why is there a duplicate??? %s' % self.m2url)
        
            
                
#############################################################################
#
# All the above does the actual parsing... the stuff below is the __main__ call!
#
##############################################################################

import codecs, os

# import the citations list from Ag...

f = codecs.open("citations.txt", "r", "utf-8")

cedaMolesURL = 'http://cidev1.jc.rl.ac.uk/ceda_moles_django/'
#cedaMolesURL = "http://localhost:8000"

molesCiteDict = {}

doiCiteDict = {}

# build up the content to parse...
for line in f:
    (a, b, c) = [(u'%s' % i).encode("utf-8") for i in line.strip().split("||")]
    molesCiteDict[os.path.join(cedaMolesURL,a)] = [b, c]
    
"""
 get dictionary of:

 {'<uuid>': [<MOLES2 citation string>, '<MOLES2URL>']}

"""

# set up some lists/dictioanaries to hold info...

fallsOverDict = {}
singleAuthorList = []
counter = 0
m2CitationDictReturn = {}
counterList = []

titleChecks = []

import pprint

# and away we go!! time to go parsing!!

for key,item in molesCiteDict.items():
    print item[0]
    #oldList = [34, 198,223, 224,223, 224,]

    
    if key in ['/uuid/4be22f465e970f2ef8423bcaf3272bf6'
               ,'/uuid/e3a65c1b11972f7b291f1ed4397e77c8'
               ,'/uuid/4264875db3d6b70acd34b63781a349d4'
               ,'/uuid/4e059bb552c99e9f62b03a0976b0482b'
               ,'/uuid/59aac4c218cf35755c371b62b2821e90']:
        print 'Check for Ag'
        print 'Put in breaks'
#    if counter+1 in [355,424,493,502,527]:
    if counter+1 in [584]:
        log.info('check')
        if ' British Antarctic Survey, Data from the BAS Masin Twin-Otter aircraft' in item[0]:
            item[0] = item[0].replace(' British Antarctic Survey, Data from the BAS Masin Twin-Otter aircraft ', 'British Antarctic Survey. Data from the BAS Masin Twin-Otter aircraft ')
    counter +=1
    log.info("Counter: %s" % counter)
    if 'VALOR' in item[0]:
        print item
        print 'stop'
    item1= CitationUnpacker(item)
    try :
#        
        sortedAuthorList = []
        authKeys = sorted(item1.authorDict.keys())
        for authorEntry in authKeys:
            sortedAuthorList.append(item1.authorDict[authorEntry])
            if sortedAuthorList == []:
                print item, counter
        print '.'.join(item[0].split('itation')[0].split('.')[:-3])
        pprint.pprint(sortedAuthorList)
        #  print sortedAuthorList, item1.etAlFlag, item1.publishedDate, item1.publisher, item1.title, item1.url
        m2CitationDictReturn[key] = {'authorList':sortedAuthorList,'etAlFlag':item1.etAlFlag, 'editorFlag':item1.editorFlag,'doiDate':item1.doiDate,'publishedDate':item1.publishedDate,'publisher': item1.publisher, 'title':item1.title, 'url':item1.url, 'm2url':item[1]}    

        titleChecks.append((str(counter),item1.title,item1.m2url,item[0]))
    
    
    except:
        fallsOverDict[key]= item
        counterList.append(counter)

#import pprint
#pprint.pprint(m2CitationDictReturn)
       
       
print  m2CitationDictReturn
print "Resolved as: m2CitationDictReturn"
        
publisherList = []

for item in m2CitationDictReturn.items():
    publisherList.append(item[1]['publisher'])

print set(publisherList)    
#import csv
#    
#titleListFile = open('titleList.txt','wb')
#titlewriter = csv.writer(titleListFile, delimiter = ',')
#
#for title in titleChecks:
#    print title
#    titlewriter.writerow(title)

