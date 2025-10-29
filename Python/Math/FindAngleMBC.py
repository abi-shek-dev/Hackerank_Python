import math

def round_half_up(n):
  return int(n + 0.5)

try:
  ab = float(input())
  bc = float(input())

  ratio = ab / bc
  
  angle_rad = math.atan(ratio)
  
  angle_deg = math.degrees(angle_rad)
  
  rounded_angle = round_half_up(angle_deg)
  
  print(rounded_angle,end='')
  print('\u00B0')

except EOFError:
  pass
except ValueError:
  pass
except ZeroDivisionError:
  print(90,end='')
  print('\u00B0')
