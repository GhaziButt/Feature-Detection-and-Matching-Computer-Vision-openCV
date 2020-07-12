import cv2
import numpy as np



pics = ["Eiffel.jpg","khalifa.jpg","minar.jpg","pisa.jpg","book.jpg","book2.jpg"]
results = []

for i in pics:
         
         count = 0 
   
         img1 = cv2.imread("pisa3.jpg", cv2.IMREAD_GRAYSCALE)
         img2 = cv2.imread( i , cv2.IMREAD_GRAYSCALE)
# Sift Detector
         sift = cv2.xfeatures2d.SIFT_create()
         keyP1, descriptor1 = sift.detectAndCompute(img1, None)
         keyP2, descriptor2 = sift.detectAndCompute(img2, None)
# Brute Force Matching
         BForce = cv2.BFMatcher(cv2.NORM_L2 , crossCheck = True)
         hits = BForce.match(descriptor1 , descriptor2)

         results.append(len(hits))
         count= count +1

print(results)         

# Highest number of matches     
ind = 0
max = 0

for o in results:
   if o > max:
     max = o
     ind = results.index(o)
     continue
   else:
     continue

# Print the query image and the most matched image.
IMG1 = cv2.imread("pisa3.jpg")
IMG2 = cv2.imread(pics[ind])

    
cv2.imshow("Img1", IMG1)
cv2.imshow("Img2", IMG2)

cv2.waitKey(0)
cv2.destroyAllWindows()