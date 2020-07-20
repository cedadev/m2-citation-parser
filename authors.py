# -*- coding: utf-8 -*-
'''
Created on 9 Mar 2012

@author: mnagni
'''
# Dictionary of all known authors and co-authors:
#  Key is the name of person or organisation that might be found in MOLES2 record
#  Value is a dictionary of author details and co-authors.
#  For individuals, the author/co-author string takes the format:
#     initials_or_first_name surname[ (org_name)]
#  - so the string can be parsed to generate useful name details.
authors = {
    'Airborne Research and Survey Facility (ARSF)':
        {'type':'org', 'author':'Airborne Research and Survey Facility (ARSF)',
         'co_author_type':[],'co_author':[]},
    'Armagh Observatory (http://star.arm.ac.uk/)':
        {'type':'org', 'author':'Armagh Observatory',
         'co_author_type':[],'co_author':[]},
    'BADC':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'badc':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'badc.nerc.ac.uk':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'badc.nerc.ac.uk (British Atmospheric Data Centre)':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'Bluesky':
        {'type':'org','author':'Bluesky',
         'co_author_type':[],'co_author':[]},           
    'BORTAS project team':
        {'type':'org','author':'BORTAS project team',
         'co_author_type':[],'co_author':[]},
    'British Antartic Survey (BAS)':
        {'type':'org','author':'British Antarctic Survey (BAS)',
         'co_author_type':[],'co_author':[]},
    'CEH Wallingford':
        {'type':'org','author':'CEH Wallingford',
         'co_author_type':[],'co_author':[]},
    'Climatic Research Unit (CRU), University of East Anglia':
        {'type':'org','author':'Climatic Research Unit (CRU)',
         'co_author_type':[],'co_author':[]},
    'Council for the Central Laboratory of the Research Councils':
        {'type':'org','author':'Council for the Central Laboratory of the Research Councils',
         'co_author_type':[],'co_author':[]},
    'CRYOSTAT Campaign participants':
        {'type':'org','author':'CRYOSTAT Campaign participants',
         'co_author_type':[],'co_author':[]},
    'CULM, Cambridge Univeristy':
        {'type':'org','author':'CULM, University of Cambridge',
         'co_author_type':[],'co_author':[]},
    'CULM, University of Cambridge':
        {'type':'org','author':'CULM, University of Cambridge',
         'co_author_type':[],'co_author':[]},
    'Disaster Monitoring Constellation International Imaging (DMCII)':
        {'type':'org','author':'Disaster Monitoring Constellation International Imaging (DMCII)',
         'co_author_type':[],'co_author':[]},
    'EU FIRETRACC Campaign participants':
        {'type':'org','author':'EU FIRETRACC Campaign participants',
         'co_author_type':[],'co_author':[]},
    'EUMETSAT':
        {'type':'org','author':'EUMETSAT','co_author_type':[],'co_author':[]},
    'European Centre for Medium-Range Weather Forecasts (ECMWF)':
        {'type':'org','author':'European Centre for Medium-Range Weather Forecasts (ECMWF)',
         'co_author_type':[],'co_author':[]},
    'European Space  (ESA)':
        {'type':'org','author':'European Space Agency (ESA)',
         'co_author_type':[],'co_author':[]},
    'European Space Agency (ESA)':
        {'type':'org','author':'European Space Agency (ESA)',
         'co_author_type':[],'co_author':[]},
    'EXPORT campaign participants':
        {'type':'org','author':'EXPORT campaign participants',
         'co_author_type':[],'co_author':[]},
    'FAAM':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'FAAM, Met Office':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'FAAM, Met Office, NERC':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'FAAM, NERC':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'FAAM, NERC, Met Office':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'FAAM, NERC, Met Office, UK Royal Society, University of Oslo':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':['org','org'],'co_author':['UK Royal Society', 'University of Oslo']},
    'FAAM, UK Met Office':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'Facility for Airborne Atmospheric Measurements':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'Facility for Airborne Atmospheric Measurements (FAAM)':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'GetMapping':
        {'type':'org','author':'GetMapping','co_author_type':[],'co_author':[]},
    'GEWEX ISLSCP Project':
        {'type':'org','author':'GEWEX ISLSCP Project','co_author_type':[],'co_author':[]},
    'HiRDLS team':
        {'type':'org','author':'HiRDLS team','co_author_type':[],'co_author':[]},
    'http://www.corral.org.uk/  (CORRAL - UK Colonial Registers and Royal Navy Logbooks Project)':
        {'type':'org','author':'UK Colonial Registers and Royal Navy Logbooks Project (CORRAL)',
         'co_author_type':[],'co_author':[]},
    'http://www.metoffice.gov.uk/':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'http://www.sunderland.ac.uk/ (University of Sunderland)':
        {'type':'org','author':'University of Sunderland','co_author_type':[],'co_author':[]},
    'http://www.ukssdc.ac.uk/':
        {'type':'org','author':'UK Solar System Data Centre',
         'co_author_type':[],'co_author':[]},
    'Infrared Sea Surface Autonomous Radiometer (ISAR) Team':
        {'type':'org','author':'Infrared Sea Surface Autonomous Radiometer (ISAR) Team','co_author_type':[],'co_author':[]},
    'Infoterra':
        {'type':'org','author':'Infoterra','co_author_type':[],'co_author':[]},
    'Intermap Technologies':
        {'type':'org','author':'Intermap Technologies','co_author_type':[],'co_author':[]},
    'International Union of Pure and Applied Chemistry':
        {'type':'org','author':'International Union of Pure and Applied Chemistry',
         'co_author_type':[],'co_author':[]},
    'IOC/NERC/US-NODC':
        {'type':'org','author':'IOC','co_author_type':['org','org'],
         'co_author':['NERC','US-NODC']},
    'IPCC':
        {'type':'org','author':'IPCC','co_author_type':[],'co_author':[]},
    'ipsl':
        {'type':'org','author':'IPSL','co_author_type':[],'co_author':[]},
    'ISCCP for the World Climate Research Programme':
        {'type':'org','author':'ISCCP','co_author_type':[],'co_author':[]},
    'JAVAD GNSS Inc.':
        {'type':'org','author':'JAVAD GNSS Inc.','co_author_type':[],'co_author':[]},
    'Jet Propulsion Laboratory':
        {'type':'org','author':'NASA Jet Propulsion Laboratory',
         'co_author_type':[],'co_author':[]},
    'Landmap':
        {'type':'org','author':'Landmap',
         'co_author_type':[],'co_author':[]},           
    'Landmap; DMC International Imaging Ltd. (DMCII)':
        {'type':'org','author':'Landmap',
         'co_author_type':['org'],'co_author':['DMC International Imaging Ltd. (DMCII)']},
    'Landmap; Europeans Space Agency (ESA)':
        {'type':'org','author':'Landmap',
         'co_author_type':['org'],'co_author':['European Space Agency (ESA)']},
    'Landmap; National Aeronautics and Space Administration (NASA)':
        {'type':'org','author':'Landmap',
         'co_author_type':['org'],'co_author':['National Aeronautics and Space Administration (NASA)']},
    'Landmap; The GeoInformation Group (TGG)':
        {'type':'org','author':'Landmap',
         'co_author_type':['org'],'co_author':['The GeoInformation Group (TGG)']},
    'Leibniz Institute for Tropospheric Research (IfT), Leipzig':
        {'type':'org','author':'Leibniz Institute for Tropospheric Research (IfT)',
         'co_author_type':[],'co_author':[]},
    'Leica Geosystems':
        {'type':'org','author':'Leica Geosystems',
         'co_author_type':[],'co_author':[]},           
    'Met Office':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'Met Office and ECMWF':
        {'type':'org','author':'Met Office','co_author_type':['org'],
         'co_author':['European Centre for Medium-Range Weather Forecasts (ECMWF)']},
    'Met Office Hadley Centre':
        {'type':'org','author':'Met Office Hadley Centre','co_author_type':[],'co_author':[]},
    'Met Office Hadley Centre for Climate Change':
        {'type':'org','author':'Met Office Hadley Centre','co_author_type':[],'co_author':[]},
    'Met Office NWP':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'Met Office, Hadley Centre':
        {'type':'org','author':'Met Office Hadley Centre','co_author_type':[],'co_author':[]},
    'Molecular Spectroscopy Facility (Science and Technology Facilities Council)':
        {'type':'org','author':'Molecular Spectroscopy Facility (Science and Technology Facilities Council)',
         'co_author_type':[],'co_author':[]},
    'mst.nerc.ac.uk':
        {'type':'org','author':'Natural Environment Research Council Mesosphere Stratosphere Troposphere Radar Facility at Aberystwyth',
         'co_author_type':[],'co_author':[]},
    'NASA':
        {'type':'org','author':'National Aeronautics and Space Administration (NASA)',
         'co_author_type':[],'co_author':[]},
    'NASA Ames Research Center':
        {'type':'org','author':'NASA Ames Research Center','co_author_type':[],'co_author':[]},
    'NASA GSFC':
        {'type':'org','author':'NASA GSFC','co_author_type':[],'co_author':[]},
    'NASA Langley DAAC':
        {'type':'org','author':'NASA Langley DAAC','co_author_type':[],'co_author':[]},
    'NASA National Space Science Data Center':
        {'type':'org','author':'NASA National Space Science Data Center',
         'co_author_type':[],'co_author':[]},
    'NASA-Langley':
        {'type':'org','author':'NASA Langley DAAC','co_author_type':[],'co_author':[]},
    'National Aeronautics and Space Administration (NASA)':
        {'type':'org','author':'National Aeronautics and Space Administration (NASA)',
         'co_author_type':[],'co_author':[]},
    'National Aeronautics and Space Administration (NASA); United States Geological Survey (USGS)':
        {'type':'org','author':'National Aeronautics and Space Administration (NASA)',
         'co_author_type':['org'],'co_author':['United States Geological Survey (USGS)']},          
    'National Centre for Atmospheric Research, USA':
        {'type':'org','author':'National Centre for Atmospheric Research (NCAR)',
         'co_author_type':[],'co_author':[]},
    'National Oceanic and Atmospheric Administration':
        {'type':'org','author':'National Oceanic and Atmospheric Administration (NOAA)',
         'co_author_type':[],'co_author':[]},
    'National Oceanic and Atmospheric Administration (NOAA); EUMETSAT':
        {'type':'org','author':'National Oceanic and Atmospheric Administration (NOAA)',
         'co_author_type':['org'],'co_author':['EUMETSAT']},    
    'National Oceanography Centre, Southampton':
        {'type':'org','author':'National Oceanography Centre (NOC)',
         'co_author_type':[],'co_author':[]},
    'National Snow and Ice Data Centre':
        {'type':'org','author':'National Snow and Ice Data Centre',
         'co_author_type':[],'co_author':[]},
    'Natural Environment Research Council':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':[],'co_author':[]},
    'Natural Environment Research Council (NERC)':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':[],'co_author':[]},
    'Natural Environment Research Council (NERC), British National Space Centre, National Aeronautics and Space Administration (NASA)':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':['org','org'],'co_author':['British National Space Centre', 'National Aeronautics and Space Administration (NASA)']},
    'Natural Environmental Research Council (NERC)':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':[],'co_author':[]},
    'NCAS':
        {'type':'org','author':' National Centre for Atmospheric Science (NCAS)',
         'co_author_type':[],'co_author':[]},
    'NCAS/EUFAR':
        {'type':'org','author':' National Centre for Atmospheric Science (NCAS) ',
         'co_author_type':['org'],'co_author':['European Facility for Airborne Research (EUFAR)']},
    'NDACC':
        {'type':'org','author':'National Centers for Environmental Prediction',
         'co_author_type':['ind','ind'],'co_author':['P Newman', 'M Chipperfield']},
    'neodc.nerc.ac.uk':
        {'type':'org','author':'unknown','co_author_type':[],'co_author':[]},
    'NERC':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':[],'co_author':[]},
    'NERC – ABACUS-IPY':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':['ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind'],'co_author':['M Williams', 'R Baxter', 'E Blyth', 'M Disney', 'M.H. Garnett','P Gates', 'R Harding', 'D.W. Hopkins', 'Brian Huntley (University of Durham)', 'P. Ineson', 'P.E. Lewis', 'M Mencuccini', 'J Moncrieff', 'G.K. Phoenix', 'M.C. Press', 'M Sommerkorn', 'P.A. Wookey']},
    'NERC ACSOE campaign participants':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':['ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind'],'co_author':['B Allan', 'A Allen ', 'Brian Bandy (University of East Anglia)', 'M Bassford', 'S Bauguitte', 'K Beswick', 'C Bradbury', 'D Brassington', 'W Broadgate','R Burgess', 'J.N. Cape', 'L Cardenas', 'Lucy Carpenter (University of York)', 'A Carrick', 'Tom  W. Choularton (University of Manchester)', 'Hugh Coe (University of Manchester)', 'I.E. Consterdine', 'D.J. Creasey', 'B Davison', 'G.D. Edwards', 'M Evans', 'C Gerbig', 'T Green', 'L Grenfell', 'Dwayne E. Heard (University of Leeds)', 'J James', 'T Jickells', 'K Law', 'James D. Lee (University of York)', 'Ally C. Lewis (University of York)', 'P Lightman', 'P.S. Liss', 'N McArdle', 'G McFadyen', 'H McIntyre', 'J.B. McQuaid', 'G Mills', 'Paul S. Monks (University of Leicester)', 'G Nickless', 'S O\'Doherty', 'D Oram', 'M.J. Pilling', 'J Plane', 'John A. Pyle (University of Cambridge)', 'Claire Reeves (University of East Anglia)', 'H Richer', 'L Robertson', 'G Salisbury', 'S Schmitgen', 'Dudley Shallcross (University of Bristol)', 'P Simmonds', 'M.H. Smith', 'G Spain', 'L Spokes', 'W Sturges', 'A Thompson', 'D Tiddeman', 'Geraint Vaughan (University of Wales, Aberystwyth)', 'O Wild', 'K Wilson', 'S Yeatman', 'I Yoshiteru', 'P Zanis']},
    'NERC AMMA-UK':
        {'type':'org','author':'NERC AMMA-UK','co_author_type':[],'co_author':[]},
    'NERC CASCADE Project participants':
        {'type':'org','author':'NERC CASCADE Project participants',
         'co_author_type':[],'co_author':[]},
    'NERC CASIX':
        {'type':'org','author':'NERC CASIX','co_author_type':[],'co_author':[]},
    'NERC Climateprediction.net':
        {'type':'org','author':'NERC Climateprediction.net',
         'co_author_type':[],'co_author':[]},
    'NERC CWVC CAMRa campaign participants':
        {'type':'org','author':'NERC CWVC CAMRa campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC CWVC GRAPE campaign participants':
        {'type':'org','author':'NERC CWVC GRAPE campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC FREE Campaign participants':
       {'type':'org','author':'NERC FREE Campaign participants',
        'co_author_type':[],'co_author':[]},
    'NERC FREE Campaign Participants (Hydro-GIS Ltd)':
        {'type':'org','author':'NERC FREE Campaign participants',
         'co_author_type':['org'],'co_author':['Hydro-GIS Ltd']},
    'NERC FREE campaign participants (Susan Rennie, University of Reading)':
        {'type':'org','author':'NERC FREE Campaign participants',
         'co_author_type':['ind'],'co_author':['Susan Rennie (University of Reading)']},
    'NERC Polluted Troposphere Programme Participants':
        {'type':'org','author':'NERC Polluted Troposphere Programme Participants',
         'co_author_type':[],'co_author':[]},
    'NERC QUEST':
        {'type':'org','author':'NERC QUEST','co_author_type':[],'co_author':[]},
    'NERC URGENT GASPOL Campaign Participants':
        {'type':'org','author':'NERC URGENT GASPOL Campaign Participants',
         'co_author_type':[],'co_author':[]},
    'NERC URGENT PHYTOX Campaign participants':
        {'type':'org','author':'NERC URGENT PHYTOX Campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC URGENT PROFIL Campaign participants':
        {'type':'org','author':'NERC URGENT PROFIL Campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC URGENT PUMACO campaign participants':
        {'type':'org','author':'NERC URGENT PUMACO campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC URGENT URBMET campaign participants':
        {'type':'org','author':'NERC URGENT URBMET campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC UTLS SLIMCAT campaign participants (Leeds University)':
        {'type':'org','author':'NERC UTLS SLIMCAT campaign participants',
         'co_author_type':['org'],'co_author':['University of Leeds']},
    'NERC UTLS-Ozone ERA-40 validation campaign participants':
        {'type':'org','author':'NERC UTLS-Ozone ERA-40 validation campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC UTLS-Ozone Extension of THESEO campaign participants (NPL)':
        {'type':'org','author':'NERC UTLS-Ozone Extension of THESEO campaign participants',
         'co_author_type':['org'],'co_author':['National Physical Laboratory (NPL)']},
    'NERC UTLS-OZONE ITOP-UK campaign participants':
        {'type':'org','author':'NERC UTLS-OZONE ITOP-UK campaign participants',
         'co_author_type':[],'co_author':[]},
    'NERC UTLS-Ozone Ozone and Water vapour measurements in the tropopause region campaign participants (University of Wales, Aberystwyth)':
        {'type':'org','author':'NERC UTLS-Ozone Ozone and Water vapour measurements in the tropopause region campaign participants (University of Wales, Aberystwyth)',
         'co_author_type':[],'co_author':[]},
    'NERC-COBRA':
        {'type':'org','author':'NERC-COBRA','co_author_type':[],'co_author':[]},
    'NERC, Met Office, FAAM':
        {'type':'org','author':'Facility for Airborne Atmospheric Measurements (FAAM)',
         'co_author_type':[],'co_author':[]},
    'Network for Calibration and Validation of EO data (NCAVEO)':
        {'type':'org','author':'Network for Calibration and Validation of EO data (NCAVEO)',
         'co_author_type':[],'co_author':[]},
    'Norwegian Institute for Air Research':
        {'type':'org','author':'Norwegian Institute for Air Research',
         'co_author_type':[],'co_author':[]},
    'Program for Climate Model Diagnosis and Intercomparison (PCMDI)':
        {'type':'org','author':'Program for Climate Model Diagnosis and Intercomparison (PCMDI)',
         'co_author_type':[],'co_author':[]},
    'QinetiQ, UFAM':
        {'type':'org','author':'Qineti',
         'co_author_type':['org'],
         'co_author':['Universities Facility for Atmospheric Measurement (UFAM)']},
    'RAL Ionospheric Monitoring Group':
        {'type':'org','author':'STFC Rutherford Appleton Laboratory Ionospheric Monitoring Group',
         'co_author_type':[],'co_author':[]},
    'RapidEye':
        {'type':'org','author':'RapidEye',
         'co_author_type':[],'co_author':[]},
    'Royal Observatory Greenwich':
        {'type':'org','author':'Royal Observatory Greenwich',
         'co_author_type':[],'co_author':[]},
    'Solar Influences Data Analysis Center':
        {'type':'org','author':'Solar Influences Data Analysis Center',
         'co_author_type':[],'co_author':[]},
    'Space Weather Prediction Center':
        {'type':'org','author':'Space Weather Prediction Center',
         'co_author_type':[],'co_author':[]},
    'STFC RAL Space Remote Sensing Group':
        {'type':'org','author':'STFC RAL Space Remote Sensing Group',
         'co_author_type':[],'co_author':[]},
    'STFC Rutherford Appleton Laboratory':
        {'type':'org','author':'STFC Rutherford Appleton Laboratory',
         'co_author_type':[],'co_author':[]},
    'Science and Technology Facilities Council (STFC), Chilbolton Facility for Atmospheric and Radio Research, [S. A. Callaghan, J. Waight, C. J. Walden, J. Agnew and S. Ventouras]':
        {'type':'org','author':'Science and Technology Facilities Council (STFC)',
         'co_author_type':['org','ind','ind','ind','ind','ind'],
         'co_author':['Chilbolton Facility for Atmospheric and Radio Research (CFARR)', 'S.A. Callaghan', 'J. Waight','C.J. Walden','Judith Agnew (STFC Rutherford Appleton Laboratory)','S. Ventouras']}, 
    'Surrey Satellite Technology Ltd (SSTL)':
        {'type':'org','author':'Surrey Satellite Technology Ltd (SSTL)',
         'co_author_type':[],'co_author':[]},
    'The GeoInformation Group (TGG)':
        {'type':'org','author':'The GeoInformation Group (TGG)',
         'co_author_type':[],'co_author':[]},    
    'The International Service of Geomagnetic Indices':
        {'type':'org','author':'The International Service of Geomagnetic Indices',
         'co_author_type':[],'co_author':[]},
    'The Max-Planck-Institut fur Biogeochemie, Jena':
        {'type':'org','author':'Max-Planck-Institut fur Biogeochemie, Jena',
         'co_author_type':[],'co_author':[]},
    'UK Meteorological Office':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'UK Meteorological Office, Max Planck Institute for Meteorology, Laboratoire de Meteorologie Dynamique, Rutherford Appleton Laboratory,':
        {'type':'org','author':'Met Office',
         'co_author_type':['org','org','org'],
         'co_author':['Max Planck Institute for Meteorology', 'Laboratoire de Meteorologie Dynamique', 'Rutherford Appleton Laboratory']},
    'UK Ministry of Defense (MOD)':
        {'type':'org','author':'UK Ministry of Defense (MOD)',
         'co_author_type':[],'co_author':[]},
    'UK Multi-Mission Product Archive Facility (UK-MM-PAF)/Infoterra Ltd':
        {'type':'org','author':'UK Multi-Mission Product Archive Facility (UK-MM-PAF)',
         'co_author_type':['org'],'co_author':['Infoterra Ltd']},
    'UK Solar System Data Centre (UKSSDC)':
        {'type':'org','author':'UK Solar System Data Centre (UKSSDC)',
         'co_author_type':[],'co_author':[]},
    'Unit  for Landscape Modelling, Cambridge University':
        {'type':'org','author':'Unit for Landscape Modelling (University of Cambridge)',
         'co_author_type':[],'co_author':[]},
    'Universities Facility for Atmospheric Measurement (UFAM)':
        {'type':'org','author':'Universities Facility for Atmospheric Measurement (UFAM)',
         'co_author_type':[],'co_author':[]},
    'University of Edinburgh':
        {'type':'org','author':'University of Edinburgh','co_author_type':[],'co_author':[]},
    'University of Leeds':
        {'type':'org','author':'University of Leeds','co_author_type':[],'co_author':[]},
    'University of York':
        {'type':'org','author':'University of York','co_author_type':[],'co_author':[]},
    'Various':
        {'type':'org','author':'unknown','co_author_type':[],'co_author':[]},
    'WAO Station Manager, Mr Brian Bandy UEA':
        {'type':'ind','author':'Brian Bandy (University of East Anglia)',
         'co_author_type':[],'co_author':[]},
    'www.esa.int (European Space Agency)':
        {'type':'org','author':'European Space Agency (ESA)',
         'co_author_type':[],'co_author':[]},
    'www.eumetsat.int (EUMETSAT)':
        {'type':'org','author':'EUMETSAT','co_author_type':[],'co_author':[]},
    'www.metoffice.gov.uk':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'www.metoffice.gov.uk (Met Office)':
        {'type':'org','author':'Met Office','co_author_type':[],'co_author':[]},
    'www.msf.rl.ac.uk':
        {'type':'org','author':'Molecular Spectroscopy Facility (Science and Technology Facilities Council)',
         'co_author_type':[],'co_author':[]},
    'A Blyth':
        {'type':'ind','author':'Alan Blyth (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'A Blyth, University of Leeds':
        {'type':'ind','author':'Alan Blyth (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'A Foxton':
        {'type':'ind','author':'A Foxton','co_author_type':[],'co_author':[]},
    'A. Holt':
        {'type':'ind','author':'A.R. Holt','co_author_type':[],'co_author':[]},
    'A. Jackson':
        {'type':'ind','author':'A Jackson','co_author_type':[],'co_author':[]},
    'A. Jones':
        {'type':'ind','author':'A Jones','co_author_type':[],'co_author':[]},
    'A. Keil, PI, Met Office':
        {'type':'ind','author':'A Keil (Met Office), PI','co_author_type':[],'co_author':[]},
    'A. Lewis':
        {'type':'ind','author':'Ally C. Lewis (University of York), PI',
         'co_author_type':[],'co_author':[]},
    'A. O\'Neill':
        {'type':'ind','author':'Alan O\'Neill (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'A. Rahimi':
        {'type':'ind','author':'A Rahimi',
         'co_author_type':[],'co_author':[]},
    'A. Rankin':
        {'type':'ind','author':'A Rankin','co_author_type':[],'co_author':[]},
    'A.C. Lewis':
        {'type':'ind','author':'Ally C. Lewis (University of York), PI',
         'co_author_type':[],'co_author':[]},
    'A.J. Baran, Met Office':
        {'type':'ind','author':'A.J. Baran (Met Office)','co_author_type':[],'co_author':[]},
    'Adam Blaker':
        {'type':'ind','author':'Adam Blaker','co_author_type':[],'co_author':[]},
    'Ahmad, S':
        {'type':'ind','author':'S Ahmad','co_author_type':[],'co_author':[]},
    'Alan Blyth (University of Leeds)':
        {'type':'ind','author':'Alan Blyth (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Alan Blyth, University of Leeds':
        {'type':'ind','author':'Alan Blyth (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'A Gadian':
        {'type':'ind','author':'Alan Gadian','co_author_type':[],'co_author':[]},         
    'Alan Gadian':
        {'type':'ind','author':'Alan Gadian','co_author_type':[],'co_author':[]},
    'Alex Megann':
        {'type':'ind','author':'Alex Megann','co_author_type':[],'co_author':[]},
    'Alexander Tudhope, University of Edinburgh':
        {'type':'ind','author':'Alexander Tudhope (University of Edinburgh)',
         'co_author_type':[],'co_author':[]},
    'Amélie Kirchgaessner':
        {'type':'ind','author':'Amélie Kirchgaessner (British Antartic Survey)',
         'co_author_type':[],'co_author':[]},
    'Andrew Watson, PI, University of East Anglia':
        {'type':'ind','author':'Andrew Watson (University of East Anglia), PI',
         'co_author_type':[],'co_author':[]},
    'Andrew Willmott, PI, Proudman Oceanographic Laboratory':
        {'type':'ind','author':'Andrew Willmott (Proudman Oceanographic Laboratory), PI',
         'co_author_type':[],'co_author':[]},
    'Andy Ridout (NCEO)':
        {'type':'ind','author':'Andy Ridout (NCEO)',
         'co_author_type':[],'co_author':[]},
    'Anoop Mahajan, University of Leeds':
        {'type':'ind','author':'Anoop Mahajan (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Anu Dudhia, University of Oxford':
        {'type':'ind','author':'Anu Dudhia (University of Oxford)',
         'co_author_type':[],'co_author':[]},
    'Arking, A.':
        {'type':'ind','author':'A Arking','co_author_type':[],'co_author':[]},
    'B. Meeson':
        {'type':'ind','author':'B Meeson','co_author_type':[],'co_author':[]},
    'Babette Hoogakker':
        {'type':'ind','author':'Babette Hoogakker','co_author_type':[],'co_author':[]},
    'Bablu Sinha':
        {'type':'ind','author':'Bablu Sinha','co_author_type':[],'co_author':[]},
    'Barkstrom, BR':
        {'type':'ind','author':'B.R. Barkstrom','co_author_type':[],'co_author':[]},
    'Berrisford, P. Reading University':
        {'type':'ind','author':'Paul Berrisford (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Bozier, K':
        {'type':'ind','author':'Karen Bozier (University of Salford)','co_author_type':[],'co_author':[]},
    'Brian Hoskins, PI, Imperial College':
        {'type':'ind','author':'Brian Hoskins (Imperial College), PI',
         'co_author_type':[],'co_author':[]},
    'Brian Kerridge, RAL Space':
        {'type':'ind','author':'Brian Kerridge (RAL Space)',
         'co_author_type':[],'co_author':[]},
    'C Reeves, University of East Anglia':
        {'type':'ind','author':'Claire Reeves (University of East Anglia)',
         'co_author_type':[],'co_author':[]},
    'Charlock, T.':
        {'type':'ind','author':'T Charlock',
         'co_author_type':[],'co_author':[]},
    'Chris Merchant':
        {'type':'ind','author':'Chris Merchant',
         'co_author_type':[],'co_author':[]},
    'Claire Postlethwaite, Proudman Oceanographic Laboratory':
        {'type':'ind','author':'Claire Postlethwaite (Proudman Oceanographic Laboratory)',
         'co_author_type':[],'co_author':[]},
    'Claire Reeves, PI, University of East Anglia':
        {'type':'ind','author':'Claire Reeves (University of East Anglia), PI',
         'co_author_type':[],'co_author':[]},
    'Colin Prentice':
        {'type':'ind','author':'Colin Prentice','co_author_type':[],'co_author':[]},
    'Collier, C.G':
        {'type':'ind','author':'Chris G. Collier','co_author_type':[],'co_author':[]},
    'CSB Grimmond, King\'s College, London':
        {'type':'ind','author':'C.S.B. Grimmond (King\'s College London) ',
         'co_author_type':[],'co_author':[]},
    'D Butt':
        {'type':'ind','author':'D Butt','co_author_type':[],'co_author':[]},
    'D. Fowler (CEH Edinburgh)':
        {'type':'ind','author':'D Fowler (CEH Edinburgh)','co_author_type':[],'co_author':[]},
    'D. Heard':
        {'type':'ind','author':'Dwayne E. Heard (University of Leeds)','co_author_type':[],'co_author':[]},
    'D. Landis':
        {'type':'ind','author':'D Landis','co_author_type':[],'co_author':[]},
    'D. Pollard, Met Office':
        {'type':'ind','author':'D Pollard (Met Office)','co_author_type':[],'co_author':[]},
    'David Berry':
        {'type':'ind','author':'David Berry','co_author_type':[],'co_author':[]},
    'David Viner':
        {'type':'ind','author':'David Viner','co_author_type':[],'co_author':[]},
    'Doug Parker, University of Leeds':
        {'type':'ind','author':'Douglas Parker (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Douglas Parker, University of Leeds':
        {'type':'ind','author':'Douglas Parker (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Dr Cecilia Svensson, NERC Centre for Ecology and Hydrology (CEH)':
        {'type':'ind','author':'Cecilia Svensson (NERC Centre for Ecology and Hydrology (CEH))',
         'co_author_type':[],'co_author':[]},
    'Dr DJ Parker, University of Leeds':
        {'type':'ind','author':'Douglas Parker (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Dr Douglas Maraun, Univeristy of East Anglia':
        {'type':'ind','author':'Douglas Maraun (Univeristy of East Anglia)',
         'co_author_type':[],'co_author':[]},
    'Dr Dudley Shallcross (University of Bristol)':
        {'type':'ind','author':'Dudley Shallcross (University of Bristol)',
         'co_author_type':[],'co_author':[]},
    'Dr Dwayne Heard, PI, University of Leeds':
        {'type':'ind','author':'Dwayne E. Heard (University of Leeds), PI',
         'co_author_type':[],'co_author':[]},
    'Dr EJ Highwood, University of Reading':
        {'type':'ind','author':'Ellie J Highwood (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr H Brindley, Imperial College London':
        {'type':'ind','author':'H Brindley (Imperial College London)',
         'co_author_type':[],'co_author':[]},
    'Dr Hannah Cloke, King\'s College London':
        {'type':'ind','author':'Hannah Cloke (King\'s College London)',
         'co_author_type':[],'co_author':[]},
    'Dr L. Shafrey':
        {'type':'ind','author':'Len C. Shaffrey (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr Malcolm Roberts':
        {'type':'ind','author':'Malcolm Roberts','co_author_type':[],'co_author':[]},
    'Dr P. L. Vidale':
        {'type':'ind','author':'Pier Luigi Vidale (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr Pier Luigi Vidale':
        {'type':'ind','author':'Pier Luigi Vidale (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr Qingping Zou, University of Plymouth':
        {'type':'ind','author':'Qingping Zou (University of Plymouth)',
         'co_author_type':[],'co_author':[]},
    'Dr R Washington, University of Oxford':
        {'type':'ind','author':'R Washington (University of Oxford)',
         'co_author_type':[],'co_author':[]},
    'Dr Sarah Dance, University of Reading':
        {'type':'ind','author':'Sarah Dance (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr Suzanne Gray (PI), University of Reading':
        {'type':'ind','author':'Suzanne Gray (University of Reading), PI',
         'co_author_type':[],'co_author':[]},
    'Dr Tania Scott, University of Reading':
        {'type':'ind','author':'Tania Scott (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Dr Tim Osborn, University of East Anglia':
        {'type':'ind','author':'Tim Osborn (University of East Anglia)',
         'co_author_type':[],'co_author':[]},
    'Dr. C. Percival, University of Manchester':
        {'type':'ind','author':'C Percival (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'Dr. Sietse Los, University of Wales Swansea':
        {'type':'ind','author':'Sietse Los (University of Wales Swansea)',
         'co_author_type':[],'co_author':[]},
    'Drew Shindell (NASA GISS)':
        {'type':'ind','author':'Drew Shindell (NASA GISS)',
         'co_author_type':[],'co_author':[]},
    'E Nemitz, CEH-Billett':
        {'type':'ind','author':'E Nemitz (NERC Centre for Ecology and Hydrology)',
         'co_author_type':[],'co_author':[]},
    'E. de Colstoun':
        {'type':'ind','author':'E de Colstoun','co_author_type':[],'co_author':[]},
    'E. Wolff':
        {'type':'ind','author':'Eric Wolff (British Antarctic Survey)','co_author_type':[],'co_author':[]},
    'Elizabeth Kent':
        {'type':'ind','author':'Elizabeth Kent','co_author_type':[],'co_author':[]},
    'Ellie Highwood, University of Reading':
        {'type':'ind','author':'Ellie J Highwood (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Ellingson, R.':
        {'type':'ind','author':'R Ellingson',
         'co_author_type':[],'co_author':[]},
    'Eric Wolff, PI, British Antarctic Survey':
        {'type':'ind','author':'Eric Wolff (British Antarctic Survey), PI',
         'co_author_type':[],'co_author':[]},
    'F.G. Hall':
        {'type':'ind','author':'F.G. Hall','co_author_type':[],'co_author':[]},
    'Fay Davies, University of Salford':
        {'type':'ind','author':'Fay Davies (University of Salford)',
         'co_author_type':[],'co_author':[]},
    'Frederick Taylor, University of Oxford':
        {'type':'ind','author':'Frederick Taylor (University of Oxford)',
         'co_author_type':[],'co_author':[]},
    'Frohlich, C.':
        {'type':'ind','author':'C Frohlich','co_author_type':[],'co_author':[]},
    'G. Jennings':
        {'type':'ind','author':'G Jennings','co_author_type':[],'co_author':[]},
    'G. Mills':
        {'type':'ind','author':'G Mills','co_author_type':[],'co_author':[]},
    'G. Upton':
        {'type':'ind','author':'G Upton','co_author_type':[],'co_author':[]},
    'G. Vaughan':
        {'type':'ind','author':'Geraint Vaughan (University of Manchester)','co_author_type':[],'co_author':[]},
    'G. Vaughan, University of Manchester':
        {'type':'ind','author':'Geraint Vaughan (University of Manchester)', 'co_author_type':[],'co_author':[]},
    'Gaines, S.E., NASA Ames Research Center':
        {'type':'ind','author':'Steven E. Gaines (NASA Ames Research Center)',
         'co_author_type':[],'co_author':[]},
    'Gareth Roberts, Kings College, London':
        {'type':'ind','author':'Gareth Roberts (King\'s College, London)',
         'co_author_type':[],'co_author':[]},
    'Gary Robinson, University of Reading':
        {'type':'ind','author':'Gary Robinson (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Greg Smith, ESSC':
        {'type':'ind','author':'Greg Smith (ESSC)','co_author_type':[],'co_author':[]},
    'Grenville Lister, University of Reading':
        {'type':'ind','author':'Grenville Lister (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Guang Zeng (NIWA)':
        {'type':'ind','author':'Guang Zeng (NIWA)','co_author_type':[],'co_author':[]},
    'H. Roscoe':
        {'type':'ind','author':'Howard Roscoe (British Antarctic Survey)','co_author_type':[],'co_author':[]},
    'Harvey Rodda (Hydro-GIS Ltd))':
        {'type':'ind','author':'Harvey Rodda (Hydro-GIS Ltd)',
         'co_author_type':[],'co_author':[]},
    'Helen Snaith, SOC':
        {'type':'ind','author':'Helen Snaith (National Oceanography Centre, Southampton)',
         'co_author_type':[],'co_author':[]},
    'Hewitt, N. (University of Lancaster)':
        {'type':'ind','author':'N Hewitt (University of Lancaster)',
         'co_author_type':[],'co_author':[]},
    'Hipskind S, NASA Ames Research Center':
        {'type':'ind','author':'S Hipskind (NASA Ames Research Center)',
         'co_author_type':[],'co_author':[]},
    'Holt, A.R':
        {'type':'ind','author':'A.R. Holt','co_author_type':[],'co_author':[]},
    'Howard Roscoe, British Antarctic Survey':
        {'type':'ind','author':'Howard Roscoe (British Antarctic Survey)',
         'co_author_type':[],'co_author':[]},
    'Hrubiak, PL':
        {'type':'ind','author':'P.L. Hrubiak','co_author_type':[],'co_author':[]},
    'Hugh Coe, University of Manchester':
        {'type':'ind','author':'Hugh Coe (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'Hugh Pumphrey, University of Edinburgh':
        {'type':'ind','author':'Hugh Pumphrey (University of Edinburgh)',
         'co_author_type':[],'co_author':[]},
    'I. Renfrew':
        {'type':'ind','author':'I Renfrew','co_author_type':[],'co_author':[]},
    'Ian (Harry) Harris, CRU':
        {'type':'ind','author':'Ian Harris (University of East Anglia Climatic Research Unit (CRU))',
         'co_author_type':[],'co_author':[]},
    'Ian Harris, Climatic Research Unit (CRU)':
        {'type':'org','author':'Ian Harris (University of East Anglia Climatic Research Unit, CRU)',
         'co_author_type':[],'co_author':[]},
    'Ian Woodward':
        {'type':'ind','author':'Ian Woodward (University of Sheffield)',
         'co_author_type':[],'co_author':[]},
    'Ian Woodward, University of Sheffield':
        {'type':'ind','author':'Ian Woodward (University of Sheffield)',
         'co_author_type':[],'co_author':[]},
    'J Freer, University of Bristol':
        {'type':'ind','author':'J Freer (University of Bristol)',
         'co_author_type':[],'co_author':[]},
    'J. Lee':
        {'type':'ind','author':'James D. Lee (University of York)','co_author_type':[],'co_author':[]},
    'J.A. Holmes, PI, University College London':
        {'type':'ind','author':'J.A. Holmes (University College London), PI',
         'co_author_type':[],'co_author':[]},
    'J.D. Lee':
        {'type':'ind','author':'James D. Lee (University of York)',
         'co_author_type':[],'co_author':[]},
    'J.L. Carpenter':
        {'type':'ind','author':'J.L. Carpenter','co_author_type':[],'co_author':[]},
    'J.R. Hopkins':
        {'type':'ind','author':'James R. Hopkins (University of York)','co_author_type':[],'co_author':[]},
    'James Dorsey, University of Manchester':
        {'type':'ind','author':'James Dorsey (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'James Hopkins, University of York':
        {'type':'ind','author':'James R. Hopkins (University of York)',
         'co_author_type':[],'co_author':[]},
    'James Lee, University of York':
        {'type':'ind','author':'James D. Lee (University of York)',
         'co_author_type':[],'co_author':[]},
    'James McGregor (Met Office)':
        {'type':'ind','author':'James McGregor (Met Office)',
         'co_author_type':[],'co_author':[]},
    'JC King':
        {'type':'ind','author':'J.C. King', 'co_author_type':[],'co_author':[]},         
    'JD Lee, University of York':
        {'type':'ind','author':'James D. Lee (University of York)',
         'co_author_type':[],'co_author':[]},
    'Jean-Francois Lamarque (NCAR)':
        {'type':'ind','author':'Jean-Francois Lamarque (NCAR)',
         'co_author_type':[],'co_author':[]},
    'Jennifer Muller, University of Manchester':
        {'type':'ind','author':'Jennifer Muller (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'Jeremy Grist, National Oceanography Centre':
        {'type':'ind','author':'Jeremy Grist ( National Oceanography Centre, Southampton)',
         'co_author_type':[],'co_author':[]},
    'Jeremy Price (Met Office)':
        {'type':'ind','author':'Jeremy Price (Met Office)',
         'co_author_type':[],'co_author':[]},
    'Jim Haywood, Met Office':
        {'type':'ind','author':'Jim Haywood (Met Office)',
         'co_author_type':[],'co_author':[]},
    'Jim Whiteway, Univeristy of Wales-Aberystwyth':
        {'type':'ind','author':'Jim Whiteway (Univeristy of Wales Aberystwyth)',
         'co_author_type':[],'co_author':[]},
    'John Harries, Principal Investigator, Imperial College, London':
        {'type':'ind','author':'John Harries (Imperial College London), PI',
         'co_author_type':[],'co_author':[]},
    'John Pyle':
        {'type':'ind','author':'John A. Pyle (University of Cambridge)','co_author_type':[],'co_author':[]},
    'John Pyle, PI, University of Cambridge':
        {'type':'ind','author':'John A. Pyle (University of Cambridge), PI',
         'co_author_type':[],'co_author':[]},
    'Jonathan Bamber, PI, University of Bristol':
        {'type':'ind','author':'Jonathan Bamber (University of Bristol), PI',
         'co_author_type':[],'co_author':[]},
    'Jonathan Gregory, PI, University of Reading':
        {'type':'ind','author':'Jonathan Gregory (University of Reading) PI',
         'co_author_type':[],'co_author':[]},
    'Jonathan Taylor (Met Office)':
        {'type':'ind','author':'Jonathan Taylor (Met Office)',
         'co_author_type':[],'co_author':[]},
    'Jonathan Taylor, Met Office':
        {'type':'ind','author':'Jonathan Taylor (Met Office)',
         'co_author_type':[],'co_author':[]},
    'Josephine Brown, University of Reading':
        {'type':'ind','author':'Josephine Brown (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'K. Bower':
        {'type':'ind','author':'Keith Bower (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'K. Labitzke (Meteorological Institute, Free University Berlin)':
        {'type':'ind','author':'K Labitzke (Meteorological Institute, Free University Berlin)',
         'co_author_type':[],'co_author':[]},
    'K. Read':
        {'type':'ind','author':'K.A. Read','co_author_type':[],'co_author':[]},
    'K. Smith':
        {'type':'ind','author':'K Smith','co_author_type':[],'co_author':[]},
    'K.A. Read':
        {'type':'ind','author':'K.A. Read','co_author_type':[],'co_author':[]},
    'K.C. Clemitshaw':
        {'type':'ind','author':'K.C. Clemitshaw','co_author_type':[],'co_author':[]},
    'Kafatos, M':
        {'type':'ind','author':'M Kafatos','co_author_type':[],'co_author':[]},
    'Karen Bozier, University of Salford':
        {'type':'ind','author':'Karen Bozier (University of Salford)',
         'co_author_type':[],'co_author':[]},
    'Karl Taylor':
        {'type':'ind','author':'Karl Taylor','co_author_type':[],'co_author':[]},
    'Katharine Giles (NCEO)':
        {'type':'ind','author':'Katharine Giles (NCEO)','co_author_type':[],'co_author':[]},
    'Keith Bower, University of Manchester':
        {'type':'ind','author':'Keith Bower (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'Keith Briffa, PI, University of East Anglia':
        {'type':'ind','author':'Keith R. Briffa (University of East Anglia), PI',
         'co_author_type':[],'co_author':[]},
    'Keith Haines':
        {'type':'ind','author':'Keith Haines (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Keith Haines, PI, University of Reading':
        {'type':'ind','author':'Keith Haines (University of Reading), PI',
         'co_author_type':[],'co_author':[]},
    'Keith Shine, University of Reading':
        {'type':'ind','author':'Keith Shine (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Kevin Oliver':
        {'type':'ind','author':'Kevin Oliver','co_author_type':[],'co_author':[]},
    'Kyle, HL':
        {'type':'ind','author':'H.L. Kyle','co_author_type':[],'co_author':[]},
    'L C Shaffrey, University of Reading':
        {'type':'ind','author':'Len C. Shaffrey (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'L. Watts':
        {'type':'ind','author':'L Watts','co_author_type':[],'co_author':[]},
    'L.M. Neves':
        {'type':'ind','author':'L.M. Neves','co_author_type':[],'co_author':[]},
    'L.Thomasson (NASA)':
        {'type':'ind','author':'L Thomasson (NASA)','co_author_type':[],'co_author':[]},
    'LC Shaffrey, University of Reading':
        {'type':'ind','author':'Len C. Shaffrey (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Li, Z':
        {'type':'ind','author':'Z Li','co_author_type':[],'co_author':[]},
    'Liu, W.':
        {'type':'ind','author':'W Liu','co_author_type':[],'co_author':[]},
    'Luca Montabone':
        {'type':'ind','author':'Luca Montabone','co_author_type':[],'co_author':[]},
    'Lucy Carpenter, University of York':
        {'type':'ind','author':'Lucy Carpenter (University of York)',
         'co_author_type':[],'co_author':[]},
    'M. Gallagher (UMIST)':
        {'type':'ind','author':'Martin W. Gallagher (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'M.J. Pilling':
        {'type':'ind','author':'M.J. Pilling','co_author_type':[],'co_author':[]},
    'M.P. McCormick (NASA)':
        {'type':'ind','author':'M.P. McCormick (NASA)','co_author_type':[],'co_author':[]},
    'Manuel Barange, PI, Plymouth Marine Laboratory':
        {'type':'ind','author':'Manuel Barange (Plymouth Marine Laboratory), PI',
         'co_author_type':[],'co_author':[]},
    'Martin Wooster, Kings College, London':
        {'type':'ind','author':'Martin Wooster (King\'s College London)',
         'co_author_type':[],'co_author':[]},
    'Marvin Shaw, University of York':
        {'type':'ind','author':'Marvin Shaw (niversity of York)',
         'co_author_type':[],'co_author':[]},
    'Matthew Wild, STFC':
        {'type':'ind','author':'Matthew Wild (Science and Technology Facilities Council (STFC))',
         'co_author_type':[],'co_author':[]},
    'McCormick, MP':
        {'type':'ind','author':'M.P. McCormick (NASA)','co_author_type':[],'co_author':[]},
    'McManus, JM':
        {'type':'ind','author':'J.M. McManus','co_author_type':[],'co_author':[]},
    'Middleton, D.R':
        {'type':'ind','author':'D.R. Middleton','co_author_type':[],'co_author':[]},
    'Mike Blackburn, University of Reading':
        {'type':'ind','author':'Mike Blackburn (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Mike Mineter':
        {'type':'ind','author':'Mike Mineter','co_author_type':[],'co_author':[]},
    'Minnis, P':
        {'type':'ind','author':'P Minnis','co_author_type':[],'co_author':[]},
    'Brian Bandy (University of East Anglia (UEA))':
        {'type':'ind','author':'Brian Bandy (University of East Anglia)','co_author_type':[],'co_author':[]},
    'Nick Reynard (NERC Cente for Ecology and Hydrology)':
        {'type':'ind','author':'Mr Nick Reynard, CEH','co_author_type':[],'co_author':[]},
    'MR van den Broeke, University of Utrecht, Netherlands':
        {'type':'ind','author':'M.R. van den Broeke (University of Utrecht)',
         'co_author_type':[],'co_author':[]},
    'MW Gallagher, University of Manchester':
        {'type':'ind','author':'Martin W. Gallagher (University of Manchester)',
         'co_author_type':[],'co_author':[]},
    'Myles allen':
        {'type':'ind','author':'Myles Allen (University of Oxford)',
         'co_author_type':[],'co_author':[]},
    'Neil Wells':
        {'type':'ind','author':'Neil Wells',
         'co_author_type':[],'co_author':[]},
    'Nigel Arnell, PI, University of Reading':
        {'type':'ind','author':'Nigel Arnell (University of Reading), PI',
         'co_author_type':[],'co_author':[]},
    'Nina MacDougall, Hydro-GIS Ltd':
        {'type':'ind','author':'Nina MacDougall (Hydro-GIS Ltd)',
         'co_author_type':[],'co_author':[]},
    'Ohring, G.':
        {'type':'ind','author':'G Ohring','co_author_type':[],
         'co_author':[]},
    'Owen Embury':
        {'type':'ind','author':'Owen Embury','co_author_type':[],'co_author':[]},
    'P Monks, University of Leicester':
        {'type':'ind','author':'Paul S. Monks (University of Leicester)',
         'co_author_type':[],'co_author':[]},
    'P. Baxter':
        {'type':'ind','author':'P Baxter','co_author_type':[],'co_author':[]},
    'P.D. Bates, University of Bristol':
        {'type':'ind','author':'P.D. Bates (University of Bristol)',
         'co_author_type':[],'co_author':[]},
    'Patrick Mc Sharry (University of Oxford, Principal Investigator)':
        {'type':'ind','author':'Patrick McSharry (University of Oxford), PI',
         'co_author_type':[],'co_author':[]},
    'PD Bates, University of Bristol':
        {'type':'ind','author':'P.D. Bates (University of Bristol)',
         'co_author_type':[],'co_author':[]},
    'Pearson, G.N.':
        {'type':'ind','author':'G.N. Pearson','co_author_type':[],'co_author':[]},
    'Peter Challenor':
        {'type':'ind','author':'Peter Challenor (National Oceanography Centre, Southampton)',
         'co_author_type':[],'co_author':[]},
    'Peter challenor, PI, NOC':
        {'type':'ind','author':'Peter Challenor (National Oceanography Centre, Southampton), PI',
         'co_author_type':[],'co_author':[]},
    'Phil Brown (Met Office)':
        {'type':'ind','author':'Phil Brown (Met Office)','co_author_type':[],'co_author':[]},
    'Phil Brown, Met Office':
        {'type':'ind','author':'Phil Brown (Met Office)','co_author_type':[],'co_author':[]},
    'Phil Jones, CRU':
        {'type':'ind','author':'Phil D. Jones (Climatic Research Unit)',
         'co_author_type':[],'co_author':[]},
    'Phil Williamson, University of East Anglia':
        {'type':'ind','author':'Phil Williamson (University of East Anglia (UEA))',
         'co_author_type':[],'co_author':[]},
    'Piers Forster, University of Leeds':
        {'type':'ind','author':'Piers Forster (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Powell, K':
        {'type':'ind','author':'K Powell','co_author_type':[],'co_author':[]},
    'Prof Ally C Lewis (PI), University of York':
        {'type':'ind','author':'Ally C. Lewis (University of York), PI',
         'co_author_type':[],'co_author':[]},
    'Prof Glenn McGregor, King\'s College London':
        {'type':'ind','author':'Glenn McGregor (King\'s College London)',
         'co_author_type':[],'co_author':[]},
    'Prof Howard Wheater, Imperial College London':
        {'type':'ind','author':'Howard Wheater (Imperial College London)',
         'co_author_type':[],'co_author':[]},
    'Prof Keith Beven, Lancaster University':
        {'type':'ind','author':'Keith Beven (Lancaster University)',
         'co_author_type':[],'co_author':[]},
    'Prof Keith Shine (University of Reading)':
        {'type':'ind','author':'Keith Shine (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Prof Martin Wooster':
        {'type':'ind','author':'Martin Wooster (King\'s College London)','co_author_type':[],'co_author':[]},
    'Prof MCTodd, University of Sussex':
        {'type':'ind','author':'M.C. Todd (University of Sussex)',
         'co_author_type':[],'co_author':[]},
    'Prof PE O\'Connell, Newcastle University':
        {'type':'ind','author':'P.E. O\'Connell (Newcastle University)',
         'co_author_type':[],'co_author':[]},
    'Prof Ralf Toumi, Imperial College London':
        {'type':'ind','author':'Ralf Toumi (Imperial College London)',
         'co_author_type':[],'co_author':[]},
    'Prof. Tom Choularton (PI), University of Manchester':
        {'type':'ind','author':'Tom W. Choularton (University of Manchester), PI',
         'co_author_type':[],'co_author':[]},
    'Professor Jon Williams, University of Plymouth':
        {'type':'ind','author':'Jon Williams (University of Plymouth)',
         'co_author_type':[],'co_author':[]},
    'R Mc.Peters':
        {'type':'ind','author':'R Mc.Peters','co_author_type':[],'co_author':[]},
    'R Sokhi, University of Hertfordshire':
        {'type':'ind','author':'R Sokhi (University of Hertfordshire)',
         'co_author_type':[],'co_author':[]},
    'R. Jones (University of Cambridge)':
    {'type':'ind','author':'R Jones (University of Cambridge)',
     'co_author_type':[],'co_author':[]},
    'R. Salmon':
        {'type':'ind','author':'R Salmon','co_author_type':[],'co_author':[]},
    'Richard Siddans, RAL Space':
        {'type':'ind','author':'Richard Siddans (RAL Space)','co_author_type':[],'co_author':[]},
    'Rob Holmes':
        {'type':'ind','author':'Rob Holmes','co_author_type':[],'co_author':[]},
    'Roisin Commane, University of Leeds':
        {'type':'ind','author':'Roisin Commane (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'Roland J. Leigh and Paul S. Monks, Univeristy of Leicester':
        {'type':'ind','author':'Roland J. Leigh (Univeristy of Leicester)',
         'co_author_type':['ind'],'co_author':['Paul S. Monks (University of Leicester)']},
    'Rowan Sutton':
        {'type':'ind','author':'Rowan Sutton (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Rowan Sutton, PI, University of Reading':
        {'type':'ind','author':'Rowan Sutton (University of Reading), PI',
         'co_author_type':[],'co_author':[]},
    'Ruth Purvis, FAAM':
        {'type':'ind','author':'Ruth Purvis (Facility for Airborne Atmospheric Measurements (FAAM))',
         'co_author_type':[],'co_author':[]},
    'S. B. Vosper, Met Office':
        {'type':'ind','author':'S.B. Vosper (Met Office)','co_author_type':[],'co_author':[]},
    'S. Bauguitte':
        {'type':'ind','author':'S Bauguitte','co_author_type':[],'co_author':[]},
    'S. Hipskind':
        {'type':'ind','author':'S Hipskind (NASA Ames Research Center)','co_author_type':[],'co_author':[]},
    'S. Los':
        {'type':'ind','author':'Sietse Los (University of Wales Swansea)',
         'co_author_type':[],'co_author':[]},
    'S Mobbs':
        {'type':'ind','author':'Stephen Mobbs (University of Leeds)',
         'co_author_type':[],'co_author':[]},
    'S. Mobbs, University of Leeds':
        {'type':'ind','author':'Stephen Mobbs (University of Leeds)',
         'co_author_type':[],'co_author':[]},        
    'S. Moller':
        {'type':'ind','author':'S Moller','co_author_type':[],'co_author':[]},
    'S O\'Doherty':
        {'type':'ind','author':'S O\'Doherty','co_author_type':[],'co_author':[]},
    'S. Palmer':
    {'type':'ind','author':'S Palmer','co_author_type':[],'co_author':[]},
    'S. Walker':
        {'type':'ind','author':'S Walker','co_author_type':[],'co_author':[]},
    'S.E. Belcher, University of Reading':
        {'type':'ind','author':'Stephen E. Belcher (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'S.Gaines':
        {'type':'ind','author':'Steven E. Gaines (NASA Ames Research Center)','co_author_type':[],'co_author':[]},
    'Sam Pepler':
        {'type':'ind','author':'Sam Pepler','co_author_type':[],'co_author':[]},
    'Sandy Harrison, PI, University of Bristol':
        {'type':'ind','author':'Sandy Harrison (University of Bristol), PI',
         'co_author_type':[],'co_author':[]},
    'Schiffer, R., NASA':
        {'type':'ind','author':'R Schiffer (NASA)','co_author_type':[],'co_author':[]},
    'Schmetz, J.':
        {'type':'ind','author':'J Schmetz','co_author_type':[],'co_author':[]},
    'Seymour Laxon (NCEO)':
        {'type':'ind','author':'Seymour Laxon (NCEO)','co_author_type':[],'co_author':[]},
    'Siemen, S.':
        {'type':'ind','author':'S Siemen','co_author_type':[],'co_author':[]},
    'Simon Crowhurst':
        {'type':'ind','author':'Simon Crowhurst','co_author_type':[],'co_author':[]},
    'Simon Jennings':
        {'type':'ind','author':'Simon Jennings','co_author_type':[],'co_author':[]},
    'Simon Josey, PI, National Oceanography Centre':
        {'type':'ind','author':'Simon Josey (National Oceanography Centre, Southampton), PI',
         'co_author_type':[],'co_author':[]},
    'Simon Tett':
        {'type':'ind','author':'Simon F.B. Tett (Met Office)','co_author_type':[],'co_author':[]},
    'Sophie Szopa (LSCE)':
        {'type':'ind','author':'Sophie Szopa (LSCE)','co_author_type':[],'co_author':[]},
    'Stephens, G':
        {'type':'ind','author':'G Stephens','co_author_type':[],'co_author':[]},
    'Steve Woolnough, University of Reading':
        {'type':'ind','author':'Steve Woolnough (University of Reading)',
         'co_author_type':[],'co_author':[]},
    'Stuart Penkett, University of East Anglia':
        {'type':'ind','author':'Stuart Penkett (University of East Anglia (UEA))',
         'co_author_type':[],'co_author':[]},
    'sv':
        {'type':'ind','author':'unknown','co_author_type':[],'co_author':[]},
    'SV':
        {'type':'ind','author':'unknown','co_author_type':[],'co_author':[]},
    'T.D. Young':
        {'type':'ind','author':'T.D. Young','co_author_type':[],'co_author':[]},
    'Takafumi Hirata, NERC Centre for the observation of Air-Sea Interaction and fluXes (CASIX); Plymouth Marine Laboratory, Plymouth, UK':
        {'type':'ind','author':'Takafumi Hirata (NERC Centre for the observation of Air-Sea Interaction and fluXes (CASIX))',
         'co_author_type':['org'],'co_author':['Plymouth Marine Laboratory']},
    'Tamsin Edwards':
        {'type':'ind','author':'Tamsin Edwards','co_author_type':[],'co_author':[]},
    'Tatsuya Nagashima (NIES)':
        {'type':'ind','author':'Tatsuya Nagashima (NIES)','co_author_type':[],'co_author':[]},
    'Tim Johns':
        {'type':'ind','author':'Tim Johns','co_author_type':[],'co_author':[]},
    'Tim Lenton, PI, University of East Anglia':
        {'type':'ind','author':'Tim Lenton (University of East Anglia (UEA)), PI',
         'co_author_type':[],'co_author':[]},
    'Tim Osborn, PI, University of East Anglia':
        {'type':'ind','author':'Tim Osborn (University of East Anglia), PI',
         'co_author_type':[],'co_author':[]},
    'Tim Osborn, University of East Anglia':
        {'type':'ind','author':'Tim Osborn (University of East Anglia)',
         'co_author_type':[],'co_author':[]},
    'Tim Nightingale (RAL Space)':
        {'type':'ind','author':'Tim Nightingale (RAL Space)',
         'co_author_type':[],'co_author':[]},
    'Tim Smyth':
        {'type':'ind','author':'Tim Smyth','co_author_type':[],'co_author':[]},
    'Upton, G.':
        {'type':'ind','author':'G Upton','co_author_type':[],'co_author':[]},
    'Vaishali Naik (GFDL)':
        {'type':'ind','author':'Vaishali Naik (GFDL)','co_author_type':[],'co_author':[]},
    'Veronika Eyring (DLR)':
        {'type':'ind','author':'Veronika Eyring (Institut fuer Physik der Atmosphaere, DLR)','co_author_type':[],'co_author':[]},
    'W Bloss, University of Birmingham':
        {'type':'ind','author':'W Bloss (University of Birmingham)',
         'co_author_type':[],'co_author':[]},
    'W. Bloss':
        {'type':'ind','author':'W Bloss (University of Birmingham)',
         'co_author_type':[],'co_author':[]},
    'W. Lahoz':
        {'type':'ind','author':'W Lahoz','co_author_type':[],'co_author':[]},
    'W.P. Chu':
        {'type':'ind','author':'W.P. Chu','co_author_type':[],'co_author':[]},
    'Wendy Garland':
        {'type':'ind','author':'Wendy Garland','co_author_type':[],'co_author':[]},
    'Whitlock, C.':
        {'type':'ind','author':'C Whitlock','co_author_type':[],'co_author':[]},
    'Willetts, D.V':
        {'type':'ind','author':'D.V. Willetts','co_author_type':[],'co_author':[]},
    'William Collins (UKMO)':
        {'type':'ind','author':'William Collins (Met Office)','co_author_type':[],'co_author':[]},
    'Wolfgang Knorr':
        {'type':'ind','author':'Wolfgang Knorr','co_author_type':[],'co_author':[]},
    'Yang, R':
        {'type':'ind','author':'R Yang','co_author_type':[],'co_author':[]},
    'Young, R.I':
        {'type':'ind','author':'R.I. Young','co_author_type':[],'co_author':[]},
    'Z.L. Fleming':
        {'type':'ind','author':'Zoe L. Fleming','co_author_type':[],'co_author':[]},
    'Professor Alan Blyth, University of Leeds':
        {'type':'ind','author':'Alan Blyth (University of Leeds)','co_author_type':[],'co_author':[]},
    'Anthony Illingworth, University of Reading':
        {'type':'ind','author':'Anthony Illingworth (University of Reading)','co_author_type':[],'co_author':[]},
    'Tom Choularton, University of Manchester':
        {'type':'ind','author':'Tom W. Choularton (University of Manchester)','co_author_type':[],'co_author':[]},
    'S. O\'Doherty':
        {'type':'ind','author':'S. O\'Doherty','co_author_type':[],'co_author':[]},
    'NERC - ABACUS-IPY':
        {'type':'org','author':'Natural Environment Research Council (NERC)',
         'co_author_type':['ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind','ind'],
         'co_author':['M Williams','R Baxter','E Blyth','M Disney','M.H. Garnett','P Gates','R Harding','D.W. Hopkins','Brian Huntley (University of Durham)','P Ineson','P.E. Lewis','M Mencuccini','J Moncrieff','G.K. Phoenix','M.C. Press','M Sommerkorn' ,'P.A. Wookey']},
    'Stephan Matthiesen, University of Edinburgh':
        {'type':'ind','author':'Stephan Matthiesen (University of Edinburgh)','co_author_type':[],'co_author':[]},
    'Thomas Lafon, Fundacion Entropika,Colombia':
        {'type':'ind','author':'Thomas Lafon (Fundacion Entropika, Colombia)','co_author_type':[],'co_author':[]},
    'Nigel Crook, Oxford Brookes University, UK':
        {'type':'ind','author':'Nigel Crook(Oxford Brookes University)','co_author_type':[],'co_author':[]},
    'Robert Beale, Oxford Brookes University, UK':
        {'type':'ind','author':'Robert Beale(Oxford Brookes University)','co_author_type':[],'co_author':[]},
    'Jennifer Fowler, University of Montana, USA':
        {'type':'ind','author':'Jennifer Fowler (University of Montana)','co_author_type':[],'co_author':[]},
    'Chris Cox, Oxford Brookes University, UK':
        {'type':'ind','author':'Chris Cox (Oxford Brookes University)','co_author_type':[],'co_author':[]},
    'Mr Brian Bandy UEA':
        {'type':'ind','author':'Brian Bandy (University of East Anglia)','co_author_type':[],'co_author':[]},
    'The Stratospheric Processes And their Role in Climate (SPARC)':
        {'type':'org','author':'The Stratospheric Processes And their Role in Climate (SPARC)',
         'co_author_type':[],'co_author':[]},
    'Veronika Eyring, Institut fuer Physik der Atmosphaere, DLR':
        {'type':'ind','author':'Veronika Eyring (Institut fuer Physik der Atmosphaere, DLR)','co_author_type':[],'co_author':[]},
    'Twentieth Century Reanalysis Project Participants':
        {'type':'org','author':'Twentieth Century Reanalysis Project Participants',
         'co_author_type':[],'co_author':[]},
    'N Matsui':
        {'type':'ind','author':'N Matsui','co_author_type':[],'co_author':[]},
    'B.E. Gleason Jr':
        {'type':'ind','author':'B.E. Gleason Jr','co_author_type':[],'co_author':[]},
    'A.C. Kruger':
        {'type':'ind','author':'A.C. Kruger','co_author_type':[],'co_author':[]},
    'T.F. Ross':
        {'type':'ind','author':'T.F. Ross','co_author_type':[],'co_author':[]},
    'G.J. Marshall':
        {'type':'ind','author':'G.J. Marshall','co_author_type':[],'co_author':[]},
    'P Bessemoulin':
        {'type':'ind','author':'P Bessemoulin','co_author_type':[],'co_author':[]},
    'S.J. Worley':
        {'type':'ind','author':'S.J. Worley','co_author_type':[],'co_author':[]},
    'M Brunet':
        {'type':'ind','author':'M Brunet','co_author_type':[],'co_author':[]},
    'R.I. Crouthamel':
        {'type':'ind','author':'R.I. Crouthamel','co_author_type':[],'co_author':[]},
    'H.Y. Mok':
        {'type':'ind','author':'H.Y. Mok','co_author_type':[],'co_author':[]},
    'P.D. Jones':
        {'type':'ind','author':'Phil D. Jones (Climatic Research Unit)','co_author_type':[],'co_author':[]},
    'J.S. Whitaker':
        {'type':'ind','author':'J.S. Whitaker','co_author_type':[],'co_author':[]},
    'Ø Nordli':
        {'type':'ind','author':'Ø Nordli','co_author_type':[],'co_author':[]},
    'R.M. Trigo':
        {'type':'ind','author':'R.M. Trigo','co_author_type':[],'co_author':[]},
    'P.D. Sardeshmukh':
        {'type':'ind','author':'P.D. Sardeshmukh','co_author_type':[],'co_author':[]},
    'S Brönnimann':
        {'type':'ind','author':'S Brönnimann','co_author_type':[],'co_author':[]},
    'G Rutledge':
        {'type':'ind','author':'G Rutledge','co_author_type':[],'co_author':[]},
    'X Yin':
        {'type':'ind','author':'X Yin','co_author_type':[],'co_author':[]},
    'R.J. Allan':
        {'type':'ind','author':'R.J. Allan','co_author_type':[],'co_author':[]},
    'A.N. Grant':
        {'type':'ind','author':'A.N. Grant','co_author_type':[],'co_author':[]},
    'S.D. Woodruff':
        {'type':'ind','author':'S.D. Woodruff','co_author_type':[],'co_author':[]},
    'M Maugeri':
        {'type':'ind','author':'M Maugeri','co_author_type':[],'co_author':[]},
    'P.Y. Groisman':
        {'type':'ind','author':'P.Y. Groisman','co_author_type':[],'co_author':[]},
    'R.S. Vose':
        {'type':'ind','author':'R.S. Vose','co_author_type':[],'co_author':[]},
    'G.P. Compo':
        {'type':'ind','author':'G.P. Compo','co_author_type':[],'co_author':[]},
    'M.C. Kruk':
        {'type':'ind','author':'M.C. Kruk','co_author_type':[],'co_author':[]},
    'Greg Bodeker, Bodeker Scientific':
        {'type':'ind','author':'Greg Bodeker (Bodeker Scientific)','co_author_type':[],'co_author':[]},
    'Birgit Hassler (NOAA)':
        {'type':'ind','author':'Birgit Hassler (NOAA)','co_author_type':[],'co_author':[]},
    'Tom Lankester, Infoterra Ltd':
        {'type':'ind','author':'Tom Lankester (Infoterra Ltd.)','co_author_type':[],'co_author':[]},
    'Prof. Andrew Shepherd, University of Leeds':
        {'type':'ind','author':'Andrew Shepherd (University of Leeds)','co_author_type':[],'co_author':[]},
    'Dr Aud Sundal, University of Leeds':
        {'type':'ind','author':'Aud Sundal (University of Leeds)','co_author_type':[],'co_author':[]},
    'Bob Brewin, Plymouth Marine Laboratory':
        {'type':'ind','author':'Bob Brewin (Plymouth Marine Laboratory)','co_author_type':[],'co_author':[]},
    'Seymour Laxon, University London College':
        {'type':'ind','author':'Seymour Laxon (University London College)','co_author_type':[],'co_author':[]},
    'Katharine A. Giles, University College London':
        {'type':'ind','author':'Katharine A. Giles (University College London)','co_author_type':[],'co_author':[]},
    'Lancaster University':
        {'type':'org','author':'Lancaster University','co_author_type':[],'co_author':[]},
    'World Data Centre (WDC) at UK Solar System Data Centre (UKSSDC)':
        {'type':'org','author':'World Data Centre (WDC) at UK Solar System Data Centre (UKSSDC)',
         'co_author_type':[],'co_author':[]},
    'Radio Research Organization':
        {'type':'org','author':'Radio Research Organization',
         'co_author_type':[],'co_author':[]},
    'Radio Research Board':
        {'type':'org','author':'Radio Research Board',
         'co_author_type':[],'co_author':[]},
    'Radio Research Station':
        {'type':'org','author':'Radio Research Station',
         'co_author_type':[],'co_author':[]},
    'Radio and Space Research Station':
        {'type':'org','author':'Radio and Space Research Station',
         'co_author_type':[],'co_author':[]},
    'World Data Centre (WDC) for Geomagnetism, Copenhagen':
        {'type':'org','author':'World Data Centre (WDC) for Geomagnetism, Copenhagen',
         'co_author_type':[],'co_author':[]},
    'OMNIWeb':
        {'type':'org','author':'OMNIWeb',
         'co_author_type':[],'co_author':[]},
    'World Data Centre (WDC) for Geomagnetism, Kyoto':
        {'type':'org','author':'World Data Centre (WDC) for Geomagnetism, Kyoto',
         'co_author_type':[],'co_author':[]},
    'International Association of Geomagnetism and Aeronomy (IAGA)':
        {'type':'org','author':'International Association of Geomagnetism and Aeronomy (IAGA)',
         'co_author_type':[],'co_author':[]},
    'Space Weather Prediction Center (SWPC)':
        {'type':'org','author':'Space Weather Prediction Center (SWPC)',
         'co_author_type':[],'co_author':[]},
    'Worldwide Ionspheric Stations':
        {'type':'org','author':'Worldwide Ionspheric Stations',
         'co_author_type':[],'co_author':[]},
    'ESA':
        {'type':'org','author':'European Space Agency (ESA)',
         'co_author_type':[],'co_author':[]},
    'STEREO SECCHI Consortium':
        {'type':'org','author':'STEREO SECCHI Consortium',
         'co_author_type':[],'co_author':[]},
    'Naval Research Laboratory, Washington DC':
        {'type':'org','author':'Naval Research Laboratory, Washington DC',
         'co_author_type':[],'co_author':[]},
    'Goddard Space Flight Center':
        {'type':'org','author':'Goddard Space Flight Center',
         'co_author_type':[],'co_author':[]},
    'EISCAT Scientific Association':
        {'type':'org','author':'EISCAT Scientific Association',
         'co_author_type':[],'co_author':[]},
    'Science and Engineering Research Council (SERC)':
        {'type':'org','author':'Science and Engineering Research Council (SERC)',
         'co_author_type':[],'co_author':[]},
    'Canadian Defence Research Board':
        {'type':'org','author':'Canadian Defence Research Board',
         'co_author_type':[],'co_author':[]},
    'Swedish Board for Space Activities':
        {'type':'org','author':'Swedish Board for Space Activities',
         'co_author_type':[],'co_author':[]},
    'CHIANTI Team':
        {'type':'org','author':'CHIANTI Team',
         'co_author_type':[],'co_author':[]},
    'Massimo Landini':
        {'type':'ind','author':'Massimo Landini','co_author_type':[],'co_author':[]},
    'A.K. Bhatia':
        {'type':'ind','author':'A.K. Bhatia','co_author_type':[],'co_author':[]},
    'M.F. Gu':
        {'type':'ind','author':'M.F. Gu','co_author_type':[],'co_author':[]},
    'K.G. Widing':
        {'type':'ind','author':'K.G. Widing','co_author_type':[],'co_author':[]},
    'H.L. Zhang':
        {'type':'ind','author':'H.L. Zhang','co_author_type':[],'co_author':[]},
    'J Pelan':
        {'type':'ind','author':'J Pelan','co_author_type':[],'co_author':[]},
    'S.S. Tayal':
        {'type':'ind','author':'S.S. Tayal','co_author_type':[],'co_author':[]},
    'K Bell':
        {'type':'ind','author':'K Bell','co_author_type':[],'co_author':[]},
    'K.A. Berrington':
        {'type':'ind','author':'K.A. Berrington','co_author_type':[],'co_author':[]},
    'Helen Mason':
        {'type':'ind','author':'Helen Mason','co_author_type':[],'co_author':[]},
    'W.C. Martin':
        {'type':'ind','author':'W.C. Martin','co_author_type':[],'co_author':[]},
    'Peter Young':
        {'type':'ind','author':'Peter Young','co_author_type':[],'co_author':[]},
    'D.H. Sampson':
        {'type':'ind','author':'D.H. Sampson','co_author_type':[],'co_author':[]},
    'T Shirai':
        {'type':'ind','author':'T Shirai','co_author_type':[],'co_author':[]},
    'W.L. Wiese':
        {'type':'ind','author':'W.L. Wiese','co_author_type':[],'co_author':[]},
    'C.A. Ramsbottom':
        {'type':'ind','author':'C.A. Ramsbottom','co_author_type':[],'co_author':[]},
    'J Dubau':
        {'type':'ind','author':'J Dubau','co_author_type':[],'co_author':[]},
    'Giulio Del-Zanna':
        {'type':'ind','author':'Giulio Del-Zanna','co_author_type':[],'co_author':[]},
    'Ken Dere':
        {'type':'ind','author':'Ken Dere','co_author_type':[],'co_author':[]},
    'C Ballance':
        {'type':'ind','author':'C Ballance','co_author_type':[],'co_author':[]},
    'U.I. Safronova':
        {'type':'ind','author':'U.I. Safronova','co_author_type':[],'co_author':[]},
    'A.K. Pradhan':
        {'type':'ind','author':'A.K. Pradhan','co_author_type':[],'co_author':[]},
    'P.J. Storey':
        {'type':'ind','author':'P.J. Storey','co_author_type':[],'co_author':[]},
    'T. Kato':
        {'type':'ind','author':'T. Kato','co_author_type':[],'co_author':[]},
    'Enrico Lani':
        {'type':'ind','author':'Enrico Lani','co_author_type':[],'co_author':[]},
    'A Musgrove':
        {'type':'ind','author':'A Musgrove','co_author_type':[],'co_author':[]},
    'James Levine':
        {'type':'ind','author':'James Levine','co_author_type':[],'co_author':[]},
    'Climate Research Unit, UEA':
        {'type':'org','author':'Climate Research Unit (University of East Anglia, UEA)',
         'co_author_type':[],'co_author':[]},
    'Science and Technology Facility Council (STFC) [S.Ventouras, S.A. Calaghan, C.L. Wrench]':
        {'type':'org','author':'Science and Technology Facility Council (STFC)',
         'co_author_type':['ind','ind','ind'],'co_author':['S.Ventouras','S.A. Calaghan','C.L. Wrench']},
    'Facility for Ground based Atmospheric Measurements (FGAM)':
        {'type':'org','author':'Facility for Ground based Atmospheric Measurements (FGAM)',
         'co_author_type':[],'co_author':[]},
    'WCRP':
        {'type':'org','author':'WCRP',
         'co_author_type':[],'co_author':[]},
    'Martin Juckes':
        {'type':'ind','author':'unknown','co_author_type':[],'co_author':[]},
    'Myles Allen':
        {'type':'ind','author':'Myles Allen (University of Oxford)','co_author_type':[],'co_author':[]},
    'Emily Norton':
        {'type':'ind','author':'Emily G Norton (University of Manchester)','co_author_type':[],'co_author':[]},
    'Emily Norton (University of Manchester)':
        {'type':'ind','author':'Emily G Norton (University of Manchester)','co_author_type':[],'co_author':[]},
    'Sandy Tudhope':
        {'type':'ind','author':'Sandy Tudhope','co_author_type':[],'co_author':[]},
    'NERC - CLACE':
        {'type':'org','author':'NERC CLACE participants',
         'co_author_type':[],'co_author':[]},
    'Stephen R. Lewis':
        {'type':'ind','author':'Stephen R. Lewis','co_author_type':[],'co_author':[]},
    'Peter L. Read':
        {'type':'ind','author':'Peter L. Read','co_author_type':[],'co_author':[]},
    'Michael D. Smith':
        {'type':'ind','author':'Michael D. Smith','co_author_type':[],'co_author':[]},
    'neodc':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'Steve Donegan':
        {'type':'ind','author':'unknown','co_author_type':[],'co_author':[]},
    'Stuart MacCallum':
        {'type':'ind','author':'Stuart MacCallum','co_author_type':[],'co_author':[]},
    'National Centers for Environmental Prediction (NCEP)':
        {'type':'org','author':'National Centers for Environmental Prediction (NCEP)',
         'co_author_type':[],'co_author':[]},
    'Victoria Pope, University of Sheffield':
        {'type':'ind','author':'Victoria Pope (University of Sheffield)','co_author_type':[],'co_author':[]},
    'badc.rl.ac.uk':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'Martin':
        {'type':'ind','author':'unknown','co_author_type':[],'co_author':[]},
    'Tim Osborn':
        {'type':'ind','author':'Tim Osborn (University of East Anglia)','co_author_type':[],'co_author':[]},
    'MOHC':
        {'type':'org','author':'Met Office Hadley Centre',
         'co_author_type':[],'co_author':[]},
    'Maria Valdivieso, Keith Haines, NCEO, Reading University':
        {'type':'org','author':'Natural Environment Research Council','co_author_type':['ind','ind'],'co_author':['Maria Valdivieso (University of Reading)','Keith Haines (University of Reading)']},
    'Thomas Lafon':
        {'type':'ind','author':'Thomas Lafon (Fundacion Entropika, Colombia)','co_author_type':[],'co_author':[]},
    'Science and Technology Facilities Council (STFC), Chilbolton Facility for Atmospheric and Radio Research, [S.Ventouras, S.A.Callaghan, C.L.Wrench]':
        {'type':'org','author':'Science and Technology Facilities Council (STFC)',
         'co_author_type':['org','ind','ind','ind'],'co_author':['Chilbolton Facility for Atmospheric and Radio Research','S.Ventouras','S.A.Callaghan','C.L.Wrench']},
    'Huo Zuo, Maria Valdivieso, Keith Haines, Reading University':
        {'type':'ind','author':'Huo Zuo (University of Reading)','co_author_type':['ind','ind'],'co_author':['Maria Valdivieso (University of Reading)','Keith Haines (University of Reading)']},
    'NEODC':
        {'type':'org','author':'unknown',
         'co_author_type':[],'co_author':[]},
    'National Centre for Earth Observation (NCEO)':
        {'type':'org','author':'National Centre for Earth Observation (NCEO)',
         'co_author_type':[],'co_author':[]},
    'Nick Hardman-Mountford, Plymouth Marine Laboratory':
        {'type':'org','author':'Nick Hardman-Mountford (Plymouth Marine Laboratory)',
         'co_author_type':[],'co_author':[]},
    'Katharine A. Giles':
        {'type':'ind','author':'Katharine A. Giles','co_author_type':[],'co_author':[]},
    'Robert Brewin, Plymouth Laboratory':
        {'type':'ind','author':'Robert Brewin (Plymouth Marine Laboratory, PML)','co_author_type':[],'co_author':[]},
    'Nick J. Hardman-Mountford, Plymouth Marine Laboratory':
        {'type':'ind','author':'Nick J. Hardman-Mountford (Plymouth Marine Laboratory, PML)','co_author_type':[],'co_author':[]},
    'Shubha Sathyendranath, Plymouth Marine Laboratory':
        {'type':'ind','author':'Shubha Sathyendranath (Plymouth Marine Laboratory, PML)','co_author_type':[],'co_author':[]},
    'Samantha J. Lavender, University of Plymouth':
        {'type':'ind','author':'Samantha J. Lavender (University of Plymouth)','co_author_type':[],'co_author':[]},
    'Emmanuel Devred, Dalhousie University, Canada':
        {'type':'ind','author':'Emmanuel Devred (Dalhousie University)','co_author_type':[],'co_author':[]},
    'Stratospheric Processes And their Role in Climate (SPARC)':
        {'type':'org','author':'Stratospheric Processes And their Role in Climate (SPARC)',
         'co_author_type':[],'co_author':[]},
    'Theodore G. Shepherd, University of Toronto, Canada':
        {'type':'ind','author':'Theodore G. Shepherd (University of Toronto)','co_author_type':[],'co_author':[]},
    'Veronika Eyring, DLR-Institut für Physik der Atmosphäre, Germany':
        {'type':'ind','author':'Veronika Eyring (Institut fuer Physik der Atmosphaere, DLR)','co_author_type':[],'co_author':[]},
    'Douglas E. Kinnison, Atmospheric Chemistry Division, National Center for Atmospheric Research, Boulder, USA':
        {'type':'ind','author':'Douglas E. Kinnison (Atmospheric Chemistry Division, National Center for Atmospheric Research)','co_author_type':[],'co_author':[]},
    'World Meteorological Organisation (WMO)':
        {'type':'org','author':'World Meteorological Organisation (WMO)',
         'co_author_type':[],'co_author':[]},
    'NOAA NCEP Environmental Modeling Center (EMC)':
        {'type':'org','author':'NOAA NCEP Environmental Modeling Center (EMC)',
         'co_author_type':[],'co_author':[]},
    'Mr Nick Reynard, CEH':
        {'type':'ind','author':'Nick Reynard (Centre for Ecology and Hydrology, CEH)','co_author_type':[],'co_author':[]},
    'Nicola Warwick, University of Cambridge':
        {'type':'ind','author':'Nicola Warwick (University of Cambridge)','co_author_type':[],'co_author':[]},
    'Prof John Pyle, University of Cambridge':
        {'type':'ind','author':'John A. Pyle (University of Cambridge)','co_author_type':[],'co_author':[]},
    'Grant Allen, University of Manchester':
        {'type':'ind','author':'Grant Allen (University of Manchester)','co_author_type':[],'co_author':[]},
    'US Department of Energy':
        {'type':'org','author':'US Department of Energy',
         'co_author_type':[],'co_author':[]},
    'National Center for Computational Sciences':
        {'type':'org','author':'National Center for Computational Sciences',
         'co_author_type':[],'co_author':[]},
    'Dr James Lee':
        {'type':'ind','author':'James D. Lee (University of York)','co_author_type':[],'co_author':[]},
    'National Center for Atmospheric Research (NCAR)':
        {'type':'org','author':'National Center for Atmospheric Research (NCAR)','co_author_type':[],'co_author':[]},
    'NERC Arctic IPY':
        {'type':'org','author':'NERC Arctic IPY participants',
         'co_author_type':[],'co_author':[]},
    'Karl Taylor (PCMDI)':
        {'type':'ind','author':'Karl Taylor (PCMDI)','co_author_type':[],'co_author':[]},
    'Andrew Schurer':
        {'type':'ind','author':'Andrew Schurer','co_author_type':[],'co_author':[]},
    'PML':
        {'type':'org','author':'Plymouth Marine Laboratory (PML)',
         'co_author_type':[],'co_author':[]},    
    'A. W. Tudhope':
        {'type':'ind','author':'A.W. Tundhope',
         'co_author_type':[],'co_author':[]},
    'Alan Blyth (University of Leeds), PI':
        {'type':'ind','author':'Alan Blyth (University of Leeds)'
         ,'co_author_type':[],'co_author':[]},
    'Amélie Kirchgaessner':
            {'type':'ind','author':'Amélie Kirchgaessner',
             'co_author_type':[],'co_author':[]},
    'Andrew':
            {'type':'ind','author':'CEDA Officer',
             'co_author_type':[],'co_author':[]},
    'Andrew Schurer (University of Edinburgh)':
            {'type':'ind','author':'Andrew Schurer (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'Anthony Illingworth (University of Reading)':
            {'type':'ind','author':'Anthony Illingworth (University of Reading)',
             'co_author_type':[],'co_author':[]},
    'Brian Bandy (University of East Anglia)':
            {'type':'ind','author':'Brian Bandy (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Brian Huntley, Durham Univeristy':
            {'type':'ind','author':'Brian Huntley (University of Durham)',
             'co_author_type':[],'co_author':[]},
    'Centre for Ecology and Hydrology (CEH)':
            {'type':'org','author':'Centre for Ecology and Hydrology (CEH)',
             'co_author_type':[],'co_author':[]},
    'Chilbolton Facility for Atmospheric and Radio Research (CFARR':
            {'type':'org','author':'Chilbolton Facility for Atmospheric and Radio Research (CFARR)',
             'co_author_type':[],'co_author':[]},
    'Chris Merchant (University of Reading)':
            {'type':'ind','author':'Chris J. Merchant (University of Reading)',
             'co_author_type':[],'co_author':[]},
    'Christine Braban (Centre for Ecology and Hydrology, CEH)':
            {'type':'ind','author':'Christine Braban (Centre for Ecology and Hydrology, CEH)',
             'co_author_type':[],'co_author':[]},
    'Claire Reeves (University of East Anglia)':
            {'type':'ind','author':'Claire Reeves (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Coastal Air Pollution Project Participants':
            {'type':'org','author':'Coastal Air Pollution Project Participants',
             'co_author_type':[],'co_author':[]},
    'D.M. Schultz, University of Manchester':
            {'type':'ind','author':'David M Schultz (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'David Hooper (STFC Rutherford Appleton Laboratory)':
            {'type':'ind','author':'David Hooper (STFC Rutherford Appleton Laboratory)',
             'co_author_type':[],'co_author':[]},
    'David Oram (University of East Anglia)':
            {'type':'ind','author':'David Oram (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Davidstow Flying Club':
            {'type':'org','author':'Davidstow Flying Club',
             'co_author_type':[],'co_author':[]},
    'Dr J Hamilton, University of York':
            {'type':'ind','author':'J Hamilton (University of York)',
             'co_author_type':[],'co_author':[]},
    'Dr M Kalberer, University of Cambridge':
            {'type':'ind','author':'M Kalberer (University of Cambridge)',
             'co_author_type':[],'co_author':[]},
    'Dr N. Harris, University of Cambridge':
            {'type':'ind','author':'N. Harris (University of Cambridge)',
             'co_author_type':[],'co_author':[]},
    'Dr P Braesicke, University of Cambridge':
            {'type':'ind','author':'Peter Braesicke (University of Cambridge)',
             'co_author_type':[],'co_author':[]},
    'Dr P Stier, University of Oxford':
            {'type':'ind','author':'P Stier (University of Oxford)',
             'co_author_type':[],'co_author':[]},
    'Dr TJ Osborn, University of East Anglia':
            {'type':'ind','author':'Tim Osborn (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Dr Tom Melvin, University of East Anglia':
            {'type':'ind','author':'Tom Melvin (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Dr ZJ Ulanowski, University of Hertfordshire':
            {'type':'ind','author':'Zbigniew J Ulanowski (University of Hertfordshire)',
             'co_author_type':[],'co_author':[]},
    'Dwayne Heard (University of Leeds), PI':
            {'type':'ind','author':'Dwayne E. Heard (University of Leeds)',
             'co_author_type':[],'co_author':[]},
    'EUMETSAT (www.eumetsat.int)':
            {'type':'org','author':'EUMETSAT',
             'co_author_type':[],'co_author':[]},
    'Emily Norton (University of Wales, Abersystwyth)':
            {'type':'ind','author':'Emily Norton (University of Wales, Abersystwyth)',
             'co_author_type':[],'co_author':[]},
    'G. C. Hegerl':
            {'type':'ind','author':'Gabriele C Hegerl (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'GC Hegerl (University of Edinburgh)':
            {'type':'ind','author':'Gabriele C Hegerl (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'Geraint Vaughan (University of Manchester)':
            {'type':'ind','author':'Geraint Vaughan (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Geraint Vaughan (University of Wales, Aberystwyth)':
            {'type':'ind','author':'Geraint Vaughan (University of Wales, Aberystwyth)',
             'co_author_type':[],'co_author':[]},
    'Geraint Vaughan, University of Manchester, PI':
            {'type':'ind','author':'Geraint Vaughan (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Gerard van der Schrier':
            {'type':'ind','author':'Gerard van der Schrier (KNMI)',
             'co_author_type':[],'co_author':[]},
    'Gerard van der Schrier, KMNI':
            {'type':'ind','author':'Gerard van der Schrier (KNMI)',
             'co_author_type':[],'co_author':[]},
    'Graham Parton':
            {'type':'ind','author':'unknown',
             'co_author_type':[],'co_author':[]},
    'John Neil Cape, (Centre for Ecology and Hydrology)':
            {'type':'ind','author':'John Neil Cape (Centre for Ecology and Hydrology)',
             'co_author_type':[],'co_author':[]},
    'Judith Agnew':
            {'type':'ind','author':'Judith Agnew (STFC Rutherford Appleton Laboratory)',
             'co_author_type':[],'co_author':[]},
    'K. R. Briffa, Climatic Research Unit':
            {'type':'ind','author':'Keith R. Briffa (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'K.N. Bower, University of Manchester':
            {'type':'ind','author':'Keith N Bower (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Keith Briffa, University of East Anglia':
            {'type':'ind','author':'Keith R. Briffa (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'M. Collins':
            {'type':'ind','author':'M Collins',
             'co_author_type':[],'co_author':[]},
    'M.W. Gallagher, University of Manchester':
            {'type':'ind','author':'Martin W. Gallagher (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Michael Barkley, University of Leicester':
            {'type':'ind','author':'Michael Barkley (University of Leicester)',
             'co_author_type':[],'co_author':[]},
    'Mike Mineter (University of Edinburgh)':
            {'type':'ind','author':'Mike Mineter (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'NERC Centre for Ecology and Hydrology':
            {'type':'org','author':'Centre for Ecology and Hydrology (CEH)',
             'co_author_type':[],'co_author':[]},
    'NERC Centre for the observation of Air-Sea Interaction and fluXes (CASIX)':
            {'type':'org','author':'NERC Centre for the observation of Air-Sea Interaction and fluXes (CASIX)',
             'co_author_type':[],'co_author':[]},
    'National Centre for Atmospheric Sciences':
            {'type':'org','author':'National Centre for Atmospheric Sciences (NCAS)',
             'co_author_type':[],'co_author':[]},
    'National Centre for Earth Observation':
            {'type':'org','author':'National Centre for Earth Observation (NCEO)',
             'co_author_type':[],'co_author':[]},
    'Nick Rutter, Northumbria University':
            {'type':'ind','author':'Nick Rutter (Northumbria University)',
             'co_author_type':[],'co_author':[]},
    'P. D. Jones, Climatic Research Unit':
            {'type':'ind','author':'Phil D. Jones (Climatic Research Unit)',
             'co_author_type':[],'co_author':[]},
    'P.J. Connolly, University of Manchester':
            {'type':'ind','author':'Paul J Connolly (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Parker, D.E., Met Office':
            {'type':'ind','author':'Douglas E Parker',
             'co_author_type':['org'],'co_author':['Met Office']},
    'Peter Wynn, University of Lancaster':
            {'type':'ind','author':'Peter Wynn (University of Lancaster)',
             'co_author_type':[],'co_author':[]},
    'Plymouth Marine Laboratory':
            {'type':'org','author':'Plymouth Marine Laboratory (PML)',
             'co_author_type':[],'co_author':[]},
    'Prof JA Pyle, University of Cambridge':
            {'type':'ind','author':'John A. Pyle (University of Cambridge)',
             'co_author_type':[],'co_author':[]},
    'Professor A Blyth, University of Leeds':
            {'type':'ind','author':'Alan Blyth (University of Leeds)',
             'co_author_type':[],'co_author':[]},
    'Professor GB McFiggans, The University of Manchester':
            {'type':'ind','author':'Gordon B McFiggans (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Professor J M Haywood, University of Exeter':
            {'type':'ind','author':'Jim M Haywood (University of Exeter)',
             'co_author_type':[],'co_author':[]},
    'Professor JP Reid, University of Bristol':
            {'type':'ind','author':'Jonathan P Reid (University of Bristol)',
             'co_author_type':[],'co_author':[]},
    'Professor PS Monks, University of Leicester':
            {'type':'ind','author':'Paul S. Monks (University of Leicester)',
             'co_author_type':[],'co_author':[]},
    'QPENSO Project Team':
            {'type':'org','author':'QPENSO Project Team',
             'co_author_type':[],'co_author':[]},
    'RAL Space':
            {'type':'org','author':'RAL Space',
             'co_author_type':[],'co_author':[]},
    'Research Councils UK':
            {'type':'org','author':'Research Councils UK',
             'co_author_type':[],'co_author':[]},
    'Richard Essery, University of Edinburgh':
            {'type':'ind','author':'Richard Essery (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'Roland von Glasow (University of East Anglia)':
            {'type':'ind','author':'Roland von Glasow (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'S Brönnimann':
            {'type':'ind','author':'S Brönnimann',
             'co_author_type':[],'co_author':[]},
    'S. O’Doherty':
            {'type':'ind','author':'S. O’Doherty',
             'co_author_type':[],'co_author':[]},
    'S.F.B. Tett (University of Edinburgh)':
            {'type':'ind','author':'Simon F.B. Tett (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'SPARCY the author':
            {'type':'org','author':'unknown',
             'co_author_type':[],'co_author':[]},
    'Science and Technology Facilities Council (STFC)':
            {'type':'org','author':'Science and Technology Facilities Council (STFC)',
             'co_author_type':[],'co_author':[]},
    'Steve Dorling (University of East Anglia)':
            {'type':'ind','author':'Steve Dorling (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'T Choularton, University of Manchester':
            {'type':'ind','author':'Tom W. Choularton (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'T. Russon':
            {'type':'ind','author':'Tom Russon',
             'co_author_type':[],'co_author':[]},
    'T. Smyth':
            {'type':'ind','author':'Tim Smyth',
             'co_author_type':[],'co_author':[]},
    'T.J. Crowley (University of Edinburgh)':
            {'type':'ind','author':'Thomas J Crowley (University of Edinburgh)',
             'co_author_type':[],'co_author':[]},
    'Takafumi Hirata':
            {'type':'ind','author':'Takafumi Hirata',
             'co_author_type':[],'co_author':[]},
    'Tett, S.F.B.Met Office':
            {'type':'ind','author':'Simon F.B. Tett (Met Office)',
             'co_author_type':['org'],'co_author':['Met Office']},
    'Thorne, P.W., Met Office':
            {'type':'ind','author':'P.W. Thorne',
             'co_author_type':['org'],'co_author':['Met Office']},
    'Tom Choularton (University of Manchester)':
            {'type':'ind','author':'Tom W. Choularton (University of Manchester)',
             'co_author_type':[],'co_author':[]},
    'Tom Russon':
            {'type':'ind','author':'Tom Russon',
             'co_author_type':[],'co_author':[]},
    'University of Aberystwyth':
            {'type':'org','author':'University of Aberystwyth',
             'co_author_type':[],'co_author':[]},
    'University of Manchester':
            {'type':'org','author':'University of Manchester',
             'co_author_type':[],'co_author':[]},
    'William Sturges (University of East Anglia)':
            {'type':'ind','author':'William Sturges (University of East Anglia)',
             'co_author_type':[],'co_author':[]},
    'Ø Nordli':
            {'type':'ind','author':'Ø Nordli',
            'co_author_type':[],'co_author':[]},                                                    
        }
