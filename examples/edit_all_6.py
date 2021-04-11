import os 

import cv2 

import pyteeth


def draw_circle(event,x,y,flags,param):
    if event == 0 :
        global img 
        global org
        img = org.copy()
        cv2.line(img, (0, y), (img.shape[1], y), (0, 255, 0), thickness=2)
        cv2.line(img, (x, 0), (x, img.shape[0]), (0, 255, 0), thickness=2)
        #print(f"x {x} y {y} flags {flags} param {param} {img.shape[1]}")
    if event == 1 :
        img = org.copy()
        cv2.circle(img,(x,y), 10, (0,0,255), -1)
        org  = img.copy()
        circles.append([x,y])
        print(f"x {x} y {y} flags {flags} param {param} {img.shape[1]}")


def main():
    images = os.listdir("test_images/")
    for image in images:
        img = cv2.imread(f"./test_images/{image}")
        teeth_detector = pyteeth.Teeth()
        img = teeth_detector.detect_top_six_teeth_for_edit(img)


        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)


        while(1):
            cv2.imshow('image',img)
            k = cv2.waitKey(1)
            if k == 27:
                print(circles)
                break
        
        


if __name__ == "__main__":
    main()