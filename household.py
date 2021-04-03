import enum_types
import custodian

class Household():
  def __init__(self):
    self.houseNumber = 0
    self.houseName = ""
    self.custodian = custodian.Custodian()
    self.houseType =enum_types.HouseType.NONE
  
