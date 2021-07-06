import pya
import math

def arc_clockwise(r, tet1, tet2, N):
  tet1 = 2*math.pi*tet1/360
  tet2 = 2*math.pi*tet2/360
  dtet = tet2 - tet1
  theta_range = range(N,-1,-1)
  out = list(theta_range)
  i = 0
  for tr in theta_range:
    ang = tet1 + tr*dtet/N
    out[i] = pya.Point(r*math.cos(ang), r*math.sin(ang))
    i = i+1  
  return out


def don(r_in, r_ou, tet1, tet2, N):
  tet1 = 2*math.pi*tet1/360
  tet2 = 2*math.pi*tet2/360
  dtet = tet2 - tet1
  theta_range = range(N, -1,-1)
  out = 2*list(theta_range)
  i = 0
  for tr in theta_range:
    ang = tet1 + tr*dtet/N
    out[i] = pya.Point(r_ou*math.cos(ang), r_ou*math.sin(ang))
    out[2*N +1 -i] = pya.Point(r_in*math.cos(ang), r_in*math.sin(ang))
    i = i+1
          
  return out
  