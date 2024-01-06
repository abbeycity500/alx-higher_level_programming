#!/usr/bin/python3
  """Defines a LockedClass"""
def LockedClass:
    """
    Precent user from instantiating a new LockedClass attribute for anything but
    attribute called first_name
    """
    __slots__ = ["first_name"]
