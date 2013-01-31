#!/usr/bin/env python

STANDARDNAME="./cf-standard-name-table.xml"
AREATYPES="./area-type-table.xml"
CFVersions=['CF-1.0','CF-1.1','CF-1.2','CF-1.3','CF-1.4','CF-1.5']
Versions=[1.0,1.1,1.2,1.3,1.4,1.5]

#======================
# Checking class
#======================
class CFChecker:
    
  def __init__(self, uploader=None, useFileName="yes", badc=None, coards=None, cfStandardNamesXML=None, cfAreaTypesXML=None, udunitsDat=None, version=Versions[-1]):
      self.uploader = uploader
      self.useFileName = useFileName
      self.badc = badc
      self.coards = coards
      self.standardNames = cfStandardNamesXML
      self.areaTypes = cfAreaTypesXML
      self.udunits = udunitsDat
      self.version = version
      self.err = 0
      self.warn = 0
      self.info = 0

  def checker(self, file):
    
      htmlblock = []

      htmlblock.append('CHECKING NetCDF FILE: %s' %file)
      htmlblock.append("=====================")
      htmlblock.append("Using CF Checker Version 2.0.4")
      htmlblock.append("Using Standard Name Table Version 21 (2013-01-12T13:23:06Z)")
      htmlblock.append("Using Area Type Table Version 1 (5 December 2008)")
      htmlblock.append(" ")
      htmlblock.append("------------------")
      htmlblock.append("Checking variable: latitude")
      htmlblock.append("------------------")
      htmlblock.append("INFO: attribute 'scale_factor' is being used in a non-standard way")
      htmlblock.append("INFO: attribute 'add_offset' is being used in a non-standard way")
      htmlblock.append(" ")
      htmlblock.append("------------------")
      htmlblock.append("Checking variable: aerosol_optical_thickness_550_land_ocean_best_estimate")
      htmlblock.append("------------------")
      htmlblock.append(" ")
      htmlblock.append("------------------")
      htmlblock.append("Checking variable: longitude")
      htmlblock.append("------------------")
      htmlblock.append("INFO: attribute 'scale_factor' is being used in a non-standard way")
      htmlblock.append("INFO: attribute 'add_offset' is being used in a non-standard way")
      htmlblock.append(" ")
      htmlblock.append("ERRORS detected: 0")
      htmlblock.append("WARNINGS given: 0")
      htmlblock.append("INFORMATION messages: 4")
      htmlblock.append(" ")
      
      return htmlblock
