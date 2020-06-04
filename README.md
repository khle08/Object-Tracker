<style src="head.css"></style>

<div class="body">
	<div class="load-content">
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
		<span class="sq"></span>
	</div>
</div>

_Object tracking is one of the trendy and under investigation topic of Computer Vision that
challenges with several issues that should be considered while creating tracking systems, such as, visual
appearance, occlusions, camera motion, and so on. In several tracking algorithms Convolutional Neural
Network (CNN) has been applied to take advantage of its powerfulness in feature extraction that convolutional
layers can characterize the object from different perspectives and treat tracking process from misclassification._


<style>
@import 'https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300';

*{
	margin :0;
	padding:0;
}

.body {
	margin-top:8%;
  	display: flex;
  	justify-content: center;
  	align-items: center;
  	background-color: #000;
    flex-direction: row;
  	height: 100px;
  flex-direction: column;
  flex-wrap: wrap;
  font-family: 'Open Sans Condensed', sans-serif;
  overflow: hidden;
}

.glow-on-hover {
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}

@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>
<div class="body">
	<button class="OPTICAL FLOW" type="button">OPTICAL FLOW</button>
</div>
				

According to [Wikipedia](https://en.wikipedia.org/wiki/Optical_flow#:~:text=Optical%20flow%20or%20optic%20flow,brightness%20pattern%20in%20an%20image.): 

    Optical flow or optic flow is the pattern of apparent motion of objects, surfaces, and edges in a visual 
    scene caused by the relative motion between an observer and a scene. Optical flow can also be defined as 
    the distribution of apparent velocities of movement of brightness pattern in an image 
    
Intutively optical flow describes the shift in position of a particular pixel in successive frames . Although pixel positions 
as well as number of pixels in a frame of given size remain constant , it must be kept in mind that when we view successive 
frames the neighbouring pixels will grab its pixel intensity from a particular pixel if the intensity of original pixel changes.

Download [01_Optical_Flow.py](https://github.com/shivanshuman021/Object-Tracker/blob/master/01_Optical_Flow.py)

To obtain the optical flow in a video file :
  
    $ python 01_Optical_Flow.py
  

    
## Object Tracking Algorithms :

### Channel and Spatial Relatibility Tracking [CSRT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjes5vxnebpAhU1zTgGHTH2D3sQFjABegQIBBAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1611.08461&usg=AOvVaw1fGNV1xM1TWV7lVL0OM9Ee) 
CSRT tracker is C++ implementation of the CSR-DCF (Channel and Spatial Reliability of Discriminative Correlation Filter)
tracking algorithm in OpenCV library. Experimental results demonstrated that CSRT tracker presents better
tracking outcomes with integration of object detection model, rather than using tracking algorithm or filter 

- Multiple Instance Learning [MIL](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)

- Kernalized Correlation Filter [KCF](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjr_eCDn-bpAhVh6nMBHctkCOYQFjACegQIAxAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F10%2F2%2F713%2Fpdf&usg=AOvVaw05SOT9pM4fR68LFLr6-Cq7)
      
- Tracker Learning Detection [TLD](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiUz6WyoObpAhUD63MBHU4_C5QQFjABegQIBRAB&url=http%3A%2F%2Fvision.stanford.edu%2Fteaching%2Fcs231b_spring1415%2Fpapers%2FKalal-PAMI.pdf&usg=AOvVaw1MM92z9XpbLgUBLwy2PFjw)

- Generic Object Tracking Using Regression Networks [GOTURN](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiivYrPoebpAhWTyjgGHbvHDUwQFjABegQIAhAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1604.01802&usg=AOvVaw0BQRhbH7dA0L_H4SqyY0Ho)

- Minimum Output Sum of Squared Error [MOSSE](https://ieeexplore.ieee.org/abstract/document/5539960)

This project implements all of the tracking algorithms using [OpenCV Tracking API](https://docs.opencv.org/3.4/d9/df8/group__tracking.html) available [OpenCV contrib](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAMegQIBRAB&url=https%3A%2F%2Fdocs.opencv.org%2F3.4.10%2Fd3%2Fd81%2Ftutorial_contrib_root.html&usg=AOvVaw1-ltthwNL7WsiqFPy-cNJ7) package

<style>
@import 'https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300';

*{
	margin :0;
	padding:0;
}

.body {
	margin-top:8%;
  	display: flex;
  	justify-content: center;
  	align-items: center;
  	background-color: #000;
    flex-direction: row;
  	height: 100px;
  flex-direction: column;
  flex-wrap: wrap;
  font-family: 'Open Sans Condensed', sans-serif;
  overflow: hidden;
}

.glow-on-hover {
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}

@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>
<div class="body">
	<button class="OPTICAL FLOW" type="button">OPTICAL FLOW</button>
</div>

Download code [here](https://github.com/shivanshuman021/Object-Tracker/blob/master/05_Single_Tracking.py)

    $ python 05_Single_Tracking.py
    
_Download the video demonstration for a single object tracker [here](https://github.com/shivanshuman021/Object-Tracker/blob/master/SINGLE_Tracker.mp4)_ 
    
#### Dependencies -
- [Python](https://python.org)
- [OpenCV](https://opencv.org)
- [OpenCV contrib modules](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAAegQIARAB&url=https%3A%2F%2Fpypi.org%2Fproject%2Fopencv-contrib-python%2F&usg=AOvVaw2CmQK0gZWG751zsw_Nm6X7)
      

### Multiple Object Tracker
Download [06_Multi_Tracking.py](https://github.com/shivanshuman021/Object-Tracker/blob/master/06_Multi_Tracking.py)	

    $ python 06_Multi_Tracking.py
    
This file has some bugs ! Will be updated after fixing them


### Useful References -
- [Evaluation of Visual Tracking Algorithms for Embedded Devices](https://www.researchgate.net/profile/Francois_Christophe/publication/317803149_Evaluation_of_Visual_Tracking_Algorithms_for_Embedded_Devices/links/59a66ea4aca272895c166a6c/Evaluation-of-Visual-Tracking-Algorithms-for-Embedded-Devices.pdf)
    
- [Comparison of Tracking Techniques](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiliOuyoubpAhUCzTgGHUjuBHUQFjAEegQIBhAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F9%2F16%2F3336%2Fpdf&usg=AOvVaw31tj8iqIPZNMGKmoF1yj2y)

##### _Here is an Optical Flow tracker using [OpenCV](https://opencv.org/)_
Optical Flow:

<video width="620" height="440" src="./OPT_FLOW.mp4" type="video/mp4" controls>



<center>
<video width="500" height="400" src="./SINGLE_Tracker.mp4" type="video/mp4" controls>
    </center>


<center>
	[[embed url=https://github.com/shivanshuman021/Object-Tracker/blob/master/SINGLE_Tracker.mp4]]
