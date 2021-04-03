import enum_type
import mydate
import custodian

class PropertyAddress():
  def __init__(self):
    self.buildingName = ""
    self.buldingNumber = ""
    self.thoroughfareName = ""

class Property():
  def __init__(self):
    self.propertyType = enum_type.PropertyType.NONE
    self.houseHolds = []
    self.propertyAddress = PropertyAddress()
    self.owner = custodian.Custodian()
    self.completionDate = mydate.Date()
    
