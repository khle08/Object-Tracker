#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[4]:


import cv2
import numpy as np


# ### Define our tracker

# In[5]:


def ask_for_tracker():
    print("select Tracker API to use ")
    print("enter 0 for BOOSTING ")
    print("enter 1 for MIL  ")
    print("enter 2 for KCF ")
    print("enter 3 for TLD ")
    print("enter 4 for MEDIANFLOW ")
    print("enter 5 for GOTURN ")
    print("enter 6 for MOSSE ")
    print("enter 7 for CSTR ")
    
    choice = input("select tracker : ")
    if choice == '0':
        tracker=cv2.TrackerBoosting_create()
    if choice == '1':
        tracker=cv2.TrackerMIL_create()        
    if choice == '2':
        tracker=cv2.TrackerKCF_create()        
    if choice == '3':
        tracker=cv2.TrackerTLD_create()
    if choice == '7':
        tracker=cv2.TrackerCSRT_create()        
    if choice == '4':
        tracker=cv2.TrackerMedianFlow_create()        
    if choice == '5':
        tracker=cv2.TrackerGOTURN_create()        
    if choice == '6':
        tracker=cv2.TrackerMOSSE_create()        
        
        
    return tracker


# ### It's a Kind of Magic

# In[7]:


# Tracker
tracker = ask_for_tracker()

# Tracker name
tracker_name = str(tracker).split()[0][1:]

# Capture the Video
cap = cv2.VideoCapture("./Video/Vehicles.mp4")

# Read the first frame
ret , frame = cap.read()

# Select our ROI
roi = cv2.selectROI(frame,False)

# Initialize tracker
ret = tracker.init(frame,roi)


# while Loop

while True:
    # Read the capture
    ret, frame = cap.read()
    
    # update tracker
    success,roi = tracker.update(frame)
    
    # roi -> from tuple to int
    (x,y,w,h) = tuple(map(int,roi))
    
    # Draw rects as tracker moves
    if success:
        
        # Sucess on tracking
        pts1 = (x,y)
        pts2 = (x+w,y+h)
        cv2.rectangle(frame,pts1,pts2,(255,125,25),3)
        
    # else
    else:
    
        # Failure on tracking
        cv2.putText(frame,"Fail to track object",(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(25,125,255),3)
        
    # Display Tracker
    cv2.putText(frame,tracker_name,(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
    
    # Display result
    cv2.imshow(tracker_name,frame)
        
    # Exit with Esc button
    if cv2.waitKey(50)&0xFF==27:
        break
    
    
# Release the Capture & Destroy All Windows
cap.release()
cv2.destroyAllWindows()



# In[ ]:




