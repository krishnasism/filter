
def applyFilter(filename):    
    try:
        import cv2
        import numpy as np
        from PIL import Image
        import os
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path=BASE_DIR+'\\static\\images\\'+filename
    
        image = cv2.imread(filename)
        print("\n\n\n\nUPLOADED")
        print(image)
        print("\n\n\n\n\n"+filename)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        
        filename1 = BASE_DIR+'\\static\\images\\1.jpg'.format(os.getpid())
        print("\n\n\n\nUPLOADED")
        print("\n\n\n\n\n"+filename)
        
        cv2.imwrite(filename1,gray)
        
        
        
        im1 = Image.open(filename)
        pixelMap1 = im1.load()
        
        img1 = Image.new( im1.mode, im1.size)
        pixelsNew1 = img1.load()
        
        im2 = Image.open(filename1)
        pixelMap2 = im2.load()
        
        img2 = Image.new(im2.mode,im2.size)
        pixelsNew2=img2.load()
        
        for i in range(img2.size[0]):
            for j in range(img2.size[1]):
                
                if pixelMap2[i,j] in range(0,25):
                    pixelMap1[i,j] = (0,0,0,255)
                else:
                    pixelsNew1[i,j] = pixelMap1[i,j]
        #img1.show()
        
        filename=filename[filename.rfind('/'):len(filename)]
        img1.save(BASE_DIR+"\\static\\images\\"+filename)
        return(filename)
    except Exception as e:
        print(e.__cause__)
        return(e)
    
