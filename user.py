import enum_types

class User():
  def __init__(self):
    self.name = ""

class SystemUser(User):
  def __init__(self):
    self.type = enum_types.UserType.SYSTEM_USER

class Manager(User):
  def __init__(self):
    self.type = enum_types.UserType.MANAGER

class Administrator(Manager):
  def __init__(self):
    self.type = enum_types.UserType.ADMIN

