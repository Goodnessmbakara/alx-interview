#!/usr/bin/python3
"""lockboxes"""

def canUnlockAll(boxes):
  """
  Determine if all the boxes can be opened then
  Return
    True
  otherwise
  Return
    False

  """

  for i in range(len(boxes)):
    for j in range(i):
      if boxes[i][j] == index(boxes[i][j+1]):
        return True
      else:
        return False

