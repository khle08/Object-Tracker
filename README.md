# Object-Tracker
## It is an Open Source Object-Tracking system that can be used to track objects in videos . With some modifications it can also be applied to make a real time system 

## Optical Flow
According to Wikipedia: 
  Optical flow or optic flow is the pattern of apparent motion of objects, surfaces, and edges in a visual 
  scene caused by the relative motion between an observer and a scene. Optical flow can also be defined as 
  the distribution of apparent velocities of movement of brightness pattern in an image.
    
Intutively optical flow describes the shift in position of a particular pixel in successive frames . Although pixel positions 
as well as number of pixels in a frame of given size remain constant , it must be kept in mind that when we view successive 
frames the neighbouring pixels will grab its pixel intensity from a particular pixel if the intensity of original pixel changes.

More information on optical flow can be obtained from [here](https://en.wikipedia.org/wiki/Optical_flow#:~:text=Optical%20flow%20or%20optic%20flow,brightness%20pattern%20in%20an%20image.)


Here is an Optical Flow tracker using [OpenCV](https://opencv.org/)

<video width="620" height="440" src="OPT_FLOW.mp4" type="video/mp4" controls>
  
To obtain the optical flow
  $ python 01_Optical_Flow.py
  

## Object Tracking Algorithms :

1) Channel and Spatial Relatibility Tracking [CSRT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjes5vxnebpAhU1zTgGHTH2D3sQFjABegQIBBAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1611.08461&usg=AOvVaw1fGNV1xM1TWV7lVL0OM9Ee)

2) Multiple Instance Learning [MIL](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)

3) Kernalized Correlation Filter [KCF](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjr_eCDn-bpAhVh6nMBHctkCOYQFjACegQIAxAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F10%2F2%2F713%2Fpdf&usg=AOvVaw05SOT9pM4fR68LFLr6-Cq7)
      
4) Tracker Learning Detection [TLD](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiUz6WyoObpAhUD63MBHU4_C5QQFjABegQIBRAB&url=http%3A%2F%2Fvision.stanford.edu%2Fteaching%2Fcs231b_spring1415%2Fpapers%2FKalal-PAMI.pdf&usg=AOvVaw1MM92z9XpbLgUBLwy2PFjw)

5) Generic Object Tracking Using Regression Networks [GOTURN](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiivYrPoebpAhWTyjgGHbvHDUwQFjABegQIAhAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1604.01802&usg=AOvVaw0BQRhbH7dA0L_H4SqyY0Ho)

6) Minimum Output Sum of Squared Error [MOSSE](https://ieeexplore.ieee.org/abstract/document/5539960)

This project implements all of the tracking algorithms using [OpenCV Tracking API](https://docs.opencv.org/3.4/d9/df8/group__tracking.html) available [OpenCV contrib](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAMegQIBRAB&url=https%3A%2F%2Fdocs.opencv.org%2F3.4.10%2Fd3%2Fd81%2Ftutorial_contrib_root.html&usg=AOvVaw1-ltthwNL7WsiqFPy-cNJ7) package

1) <B><I>Single Object Tracker</I></B>
    $ python 05_Single_Tracking.py
    
    Dependencies -
      [Python](https://python.org)
      [OpenCV](https://opencv.org)
      [OpenCV contrib modules](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAAegQIARAB&url=https%3A%2F%2Fpypi.org%2Fproject%2Fopencv-contrib-python%2F&usg=AOvVaw2CmQK0gZWG751zsw_Nm6X7)
      
<video width="620" height="440" src="SINGLE_Tracker.mp4" type="video/mp4" controls>


2) 1) <B><I>Multiple Object Tracker</I></B>
    $ python 06_Multi_Tracking.py
    
    This file has some bugs ! Will be updated after fixing them

### Useful References -
  - [Evaluation of Visual Tracking Algorithms for Embedded Devices](https://www.researchgate.net/profile/Francois_Christophe/publication/317803149_Evaluation_of_Visual_Tracking_Algorithms_for_Embedded_Devices/links/59a66ea4aca272895c166a6c/Evaluation-of-Visual-Tracking-Algorithms-for-Embedded-Devices.pdf)
    
  - [Comparison of Tracking Techniques](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiliOuyoubpAhUCzTgGHUjuBHUQFjAEegQIBhAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F9%2F16%2F3336%2Fpdf&usg=AOvVaw31tj8iqIPZNMGKmoF1yj2y)


