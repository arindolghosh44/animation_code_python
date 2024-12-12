from inspect import Attribute
import turtle as tu
import cv2
from  svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm
class sketch_from_svg:
    def __init__(self,path,scale=30,x_offset=400,y_offset=400):
        self.path=path
        self.x_offset=x_offset
        self.y_offset=y_offset
        self.scale=scale
    def hex_to_rgb(self,string):
        strlen=len(string)
        if string.startswith("0"):
            if strlen==7:
                r=string[1:3]
                g=string[3:5]
                b=string[5:7]
            elif strlen==4:
                r=string[1:2]*2
                g=string[2:3]*2
                b=string[3:4]*2
            elif strlen==3:
                r=string[0:1]*2
                g=string[2:4]*2
                b=string[4:6]*2
            else:
                r=string[0:2]
                g=string[2:4]
                b=string[4:6]

            return int (r,16)/255,int (g,16)/255,int (b,16)/255
    def load_svg(self):
        print("loading data")
        paths.attributes.svg_att=svg2paths2(self.height,self.width)
        h=svg_att["height"]
        w=svg_att["width"]
        self.height=int(h[:h.find(".")])
        self.width=int(w[:w.find(".")])
        rse=[]
        for i in tqdm(Attribute):
            path=parse_path(i["d"])
            co=i['fill']
            col=self.hex_to_rgb(co)
            n=len(list(path))+2
            pts=[((int((p.real/self.width))))]




            


    
