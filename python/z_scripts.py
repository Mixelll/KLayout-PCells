import pya
#from pya import *

def Negative_ebeam_script(options = None):
  if options is None:
    options = {'layers':[1], 'etch_frame_um':1.0, 'frame_mode':5, 'folder_path':"C:/Users/sz1x3/Google Drive/EE MSc/KLayout/GDS/Dor"}
    return options
  layers = options['layers']
  etch_frame = options['etch_frame_um']
  frame_mode = options['frame_mode']
  dpath = options['folder_path']
  layout0 = pya.CellView.active().layout()
  lay_dbu = layout0.dbu
  et = int(round(etch_frame/lay_dbu))
  layout = pya.Layout()
  top = layout.create_cell("TOP")
  name = pya.CellView.active().name
  name = name[0:len(name)-4]
  for l in layers:
    l = int(l)
    find_l = layout0.find_layer(l,0)
    if find_l is not None:
      layer = layout.layer(l, 0)
      region0 = pya.Region(layout0.begin_shapes(layout0.top_cell(), find_l))
      region = region0.dup()
      region.size(et,frame_mode)
      region.merge()
      region_diff = region-region0
    top.shapes(layer).insert(region_diff)
  layout.write(dpath + "/" + name +"_Negative_L="+str(layers)+"_frame="+str(etch_frame)+"um.gds")
  
def Capping_script(options = None):
  if options is None:
    options = {'cap layer':4,'layers to cap':[1], 'cap frame um':1.0, 'frame mode':5, 'folder path':"C:/Users/admin2/Google Drive/EE MSc/KLayout/GDS/Collection",'addname':'Capped'}
    return options
  layers = options['layers to cap']
  cap_frame = options['cap frame um']
  frame_mode = options['frame mode']
  dpath = options['folder path']
  addname = options['addname']
  name = pya.CellView.active().name
  name = name[0:len(name)-4]
  layout0 = pya.CellView.active().layout()
  layout = layout0.dup()
  top = layout.top_cell()
  et = int(round(cap_frame/layout0.dbu))
  cap_layer  = layout.layer(options['cap layer'], 0)
  region_final = pya.Region()
  for l in layers:
    find_l = layout0.find_layer(int(l),0)
    if find_l is not None:
      region = pya.Region(layout0.begin_shapes(top, find_l))
      region.size(et,frame_mode)
      region_final = region_final+region
  region_final.merge()
  top.shapes(cap_layer).insert(region_final)
  layout.write(dpath + "/" + name + " " + addname +".gds")