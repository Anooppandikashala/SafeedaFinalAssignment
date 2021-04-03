import enum

# creating enumerations using class
class UserType(enum.Enum):
  SYSTEM_USER = 1
  MANAGER = 2
  ADMIN = 3


# creating enumerations using class
class HouseType(enum.Enum):
  FLAT = 1
  HOUSE = 2
  NONE = 3

class PropertyType(enum.Enum):
  DETACHED = 1
  SEMI_DETACHED = 2
  TERRACE = 3
  FLATS = 4
  NONE = 5