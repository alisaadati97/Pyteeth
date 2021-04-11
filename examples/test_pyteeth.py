import os 

import cv2 

import pyteeth

class EditTestTop():
    def __init__(self,image):

        self.circles = []
        self.show_edit = False

        self.teeth_detector = pyteeth.Teeth()

        self.orginal_image = cv2.imread(f"./test_images/{image}")
        self.img = self.orginal_image.copy()
        self.temp_image = self.img.copy()
        self.edited_img = self.img.copy()

        self.top_six()
    
    def draw_circle(self,event,x,y,flags,param):
        if event == 0 :
            self.edited_img = self.temp_image.copy()
            cv2.line(self.edited_img, (0, y), (self.edited_img.shape[1], y), (0, 255, 0), thickness=2)
            cv2.line(self.edited_img, (x, 0), (x, self.edited_img.shape[0]), (0, 255, 0), thickness=2)
        if event == 1 :           
            self.circles.append((x,y))
            print(self.circles)
            cv2.circle(self.edited_img,(x,y), 10, (0,0,255), -1)
            self.temp_image  = self.edited_img.copy()

    def top_six(self):
        self.img = self.teeth_detector.detect_top_six_teeth_for_edit(self.img)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.draw_circle)
        while(1):  
            if self.show_edit :
                cv2.imshow('image',self.edited_img)
            elif not self.show_edit  :
                cv2.imshow('image',self.img)
            
            k = cv2.waitKey(1)
            if k == 27:
                print(self.circles)
                break
            elif k == ord("e"):
                self.show_edit = not self.show_edit
            elif k == ord("d"):
                self.coords = [self.circles[0][0] , self.circles[0][1] , self.circles[-1][0] , self.circles[-1][1]]
                break

class EditTestEach():
    def __init__(self,image,coords):
        self.c = []
        self.coords = coords
        self.tooth_data = []
        self.circles = []
        self.show_edit = False

        self.teeth_detector = pyteeth.Teeth()

        self.orginal_image = cv2.imread(f"./test_images/{image}")
        self.img = self.orginal_image.copy()
        self.temp_image = self.img.copy()
        self.edited_img = self.img.copy()

        self.each_six()
    
    def draw_circle(self,event,x,y,flags,param):
        if event == 0 :
            self.edited_img = self.temp_image.copy()
            cv2.line(self.edited_img, (0, y), (self.edited_img.shape[1], y), (0, 255, 0), thickness=2)
            cv2.line(self.edited_img, (x, 0), (x, self.edited_img.shape[0]), (0, 255, 0), thickness=2)
        if event == 1 :           
            self.circles.append((x,y))
            print(self.circles)
            cv2.circle(self.edited_img,(x,y), 10, (0,0,255), -1)
            self.temp_image  = self.edited_img.copy()

    def each_six(self):
        self.img = self.teeth_detector.detect_each_tooth_for_edit(self.img , self.coords)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.draw_circle)
        while(1):  
            if self.show_edit :
                cv2.imshow('image',self.edited_img)
            elif not self.show_edit  :
                cv2.imshow('image',self.img)
            
            k = cv2.waitKey(1)
            if k == 27:
                print(self.circles)
                break
            elif k == ord("e"):
                self.show_edit = not self.show_edit
            elif k == ord("n"):
                self.edited_img = self.orginal_image.copy()
                self.temp_image  = self.orginal_image.copy()
            
            elif k == ord("d"):
                cv2.setMouseCallback('image', lambda *args : None)
                self.edited_img = self.orginal_image.copy()
                for i in range(len(self.circles)//4):
                    
                    data = self.circles[4*i:4*(i+1)]
                    x = data[0][0]
                    y = data[0][1]
                    xb = data[-1][0]
                    yb = data[-1][1]

                    w = xb-x
                    h = yb-y
                    
                    cv2.line(self.edited_img, ((x+xb)//2, y), ((x+xb)//2,yb), (0, 255, 0), thickness=2)
                    cv2.line(self.edited_img, (x, (y+yb)//2 ), (xb,(y+yb)//2), (0, 0, 255), thickness=2)
                    cv2.circle(self.edited_img,((x+xb)//2, (y+yb)//2), 6, (255,0,0), -1)
                    
       

if __name__ == "__main__":
    images = os.listdir("test_images/")
    for image in images:
        edit_obj = EditTestTop(image)
        edit_obj_each = EditTestEach(image ,edit_obj.coords) 

    