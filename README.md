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
  	background-color: #333;
  	height: 400px;
  flex-direction: column;
  flex-wrap: wrap;
  font-family: 'Open Sans Condensed', sans-serif;
  overflow: hidden;
}

div[class*=box] {
	height: 54%;
	width: 100%; 
  display: -webkit-box; 
  display: flex;
  justify-content: center;
  align-items: center;
}

.box { background-color: #3C3C3C; }

.butn {
	line-height: 50px;
	height: 50px;
	text-align: center;
	width: 250px;
	cursor: pointer;
}
.butn-hov {
	color: #FFF;
	transition: all 0.5s;
	position: relative;	
}
.butn-hov span {
	z-index: 2;	
	display: block;
	position: absolute;
	width: 100%;
	height: 100%;
	font-size: 15px;	
}
.butn-hov::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 1px solid rgba(255,255,255,0.2);
	background-color: rgba(255,255,255,0.1);
}
.butn-hov::after {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 1px solid rgba(255,255,255,0.2);
	background-color: rgba(255,255,255,0.1);
}
.butn-hov:hover::before {
  transform: rotate(-45deg);
  background-color: rgba(255,255,255,0);
}
.butn-hov:hover::after {
  transform: rotate(45deg);
  background-color: rgba(255,255,255,0);
}
</style>
<div class="body">
	<div class="box">
  <div class="butn butn-hov">
    <span>Object Tracker</span>
  </div>
</div>
</div>
																
<h2>
<B><I>
Object tracking is one of the trendy and under investigation topic of Computer Vision that
challenges with several issues that should be considered while creating tracking systems, such as, visual
appearance, occlusions, camera motion, and so on. In several tracking algorithms Convolutional Neural
Network (CNN) has been applied to take advantage of its powerfulness in feature extraction that convolutional
layers can characterize the object from different perspectives and treat tracking process from misclassification.
	</I></B>
</h2>
				
<style>
*{
	margin :0;
	padding:0;
}

.body {
	margin-top:8%;
  	display: flex;
  	justify-content: center;
  	align-items: center;
  	background-color: #333;
  	font-weight: bold;
  	height: 100px;
}

.load-head{
	color : #f1f1f1;
	font-family: sans-serif;
	font-size: 30px;
	margin-bottom: 1%;  
}

.loader{
	height: 30px;
	width: 300px;
	display: flex;
}

.loader span{
	width: 30px;
	height: 30px;
	background: white;
	margin: 1px; 
}

.L1{
	content: '1';
	animation: L1 1s 1;
}

.L2{
	animation: L1 1s 1;
	animation-delay: 0.2s;
}

.L3{
	animation: L1 1s 1;
	animation-delay: 0.6s;
}

.L4{
	animation: L1 1s 1;
	animation-delay: 0.9s;
}

.L5{
	animation: L1 1s 1;
	animation-delay: 1.2s;
}

.L6{
	animation: L1 1s 1;
	animation-delay: 1.5s;
}

.L7{
	animation: L1 1s 1;
	animation-delay: 1.8s;
}

.L8{
	animation: L1 1s 1;
	animation-delay: 2.1s;
}

.L9{
	animation: L1 1s 1;
	animation-delay: 2.4s;
}

@keyframes L1{
	50%{
		background-color: #dc3545;
	}
	
	100%{
		transform: rotateZ(180deg);
	}
}
</style>
<div class="body">
	<div>
		<div class="load-head">
			OPTICAL FLOW
		</div>
		<div class="loader">
			<span class="L1"></span>
			<span class="L2"></span>
			<span class="L3"></span>
			<span class="L4"></span>
			<span class="L5"></span>
			<span class="L6"></span>
			<span class="L7"></span>
			<span class="L8"></span>
			<span class="L9"></span>
		</div>
	</div>
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
tracking outcomes with integration of object detection model, rather than using tracking algorithm or filter .It is integration of 
the Region based CNN (Faster RCNN) pre-trained object detection model that the OpenCV based CSRT (Channel and Spatial Reliability Tracking) tracker has a high
chance to identifying objects features, classes and locations as well

### Multiple Instance Learning [MIL](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)
It address the problem of learning an adaptive appearance model for object tracking. In particular, a class of tracking techniques 
called “tracking by detection” give promising results at realtime speeds. These methods train a discriminative classifier in an online 
manner to separate the object from the background. This classifier bootstraps itself by using the current tracker state 
to extract positive and negative examples from the current frame. Slight inaccuracies in the tracker can therefore lead to incorrectly 
labeled training examples, which degrades the classifier and can cause further drift.
Using Multiple Instance Learning (MIL) instead of traditional supervised learning avoids these problems, and can therefore lead to a 
more robust tracker with fewer parameter tweaks.

### Kernalized Correlation Filter [KCF](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjr_eCDn-bpAhVh6nMBHctkCOYQFjACegQIAxAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F10%2F2%2F713%2Fpdf&usg=AOvVaw05SOT9pM4fR68LFLr6-Cq7)
Deep feature-based trackers that have been proposed to achieve a higher accuracy are not suitable for real-time tracking because
of an extremely slow processing speed. The slow speed is a major factor to degrade tracking accuracy under a real-time streaming 
condition since the processing delay forces skipping frames. To increase the tracking accuracy with preserving the processing speed, 
an improved kernelized correlation filter (KCF)-based tracking method that integrates three functional modules:
- tracking failure detection 
- re-tracking using multiple search windows 
- motion vector analysis to decide a preferred search window.

### Tracker Learning Detection [TLD](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiUz6WyoObpAhUD63MBHU4_C5QQFjABegQIBRAB&url=http%3A%2F%2Fvision.stanford.edu%2Fteaching%2Fcs231b_spring1415%2Fpapers%2FKalal-PAMI.pdf&usg=AOvVaw1MM92z9XpbLgUBLwy2PFjw)
In this the positions of objects are determined in first frame and then in successive frame it is tracked if it is present in next 
frame. TLD explicitly decomposes the long-term tracking task into tracking, learning and detection. The tracker follows the object 
from frame to frame. The detector localizes all appearances that have been observed so far and corrects the tracker if necessary. The 
learning estimates detector’s errors and updates it to avoid these errors in the future

### Generic Object Tracking Using Regression Networks [GOTURN](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiivYrPoebpAhWTyjgGHbvHDUwQFjABegQIAhAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1604.01802&usg=AOvVaw0BQRhbH7dA0L_H4SqyY0Ho)
In GOTURN a neural network for tracking does task in an entirely offline manner. At test time, when tracking novel objects, the network 
weights are frozen, and no online fine-tuning required (as shown in Figure 1). Through the offline training procedure, the tracker 
learns to track novel objects in a fast, robust, and accurate manner

### Minimum Output Sum of Squared Error [MOSSE](https://ieeexplore.ieee.org/abstract/document/5539960)
The MOSSE tracker calculates the minimum output sum of square error to find out the most possible location of the tracking object. The 
benefits of using a correlation filter make the MOSSE tracker more robust to the problems of scaling, rotation, deformation, and 
occlusion compared to traditional approaches. Also MOSSE is more flexible than other correlation-filter-based trackers because the 
target is not required to be in the center of the image in the beginning of tracking


#### This project implements all of the tracking algorithms using [OpenCV Tracking API](https://docs.opencv.org/3.4/d9/df8/group__tracking.html) available under [OpenCV contrib](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAMegQIBRAB&url=https%3A%2F%2Fdocs.opencv.org%2F3.4.10%2Fd3%2Fd81%2Ftutorial_contrib_root.html&usg=AOvVaw1-ltthwNL7WsiqFPy-cNJ7) package

<style>
*{
	margin :0;
	padding:0;
}

.body {
	margin-top:8%;
  	display: flex;
  	justify-content: center;
  	align-items: center;
  	background-color: #333;
  	font-weight: bold;
  	height: 100px;
}

.load-head{
	color : #f1f1f1;
	font-family: sans-serif;
	font-size: 30px;
	margin-bottom: 1%;  
}

.loader{
	height: 30px;
	width: 300px;
	display: flex;
}

.loader span{
	width: 30px;
	height: 30px;
	background: white;
	margin: 1px; 
}

.L1{
	content: '1';
	animation: L1 1s 1;
}

.L2{
	animation: L1 1s 1;
	animation-delay: 0.2s;
}

.L3{
	animation: L1 1s 1;
	animation-delay: 0.6s;
}

.L4{
	animation: L1 1s 1;
	animation-delay: 0.9s;
}

.L5{
	animation: L1 1s 1;
	animation-delay: 1.2s;
}

.L6{
	animation: L1 1s 1;
	animation-delay: 1.5s;
}

.L7{
	animation: L1 1s 1;
	animation-delay: 1.8s;
}

.L8{
	animation: L1 1s 1;
	animation-delay: 2.1s;
}

.L9{
	animation: L1 1s 1;
	animation-delay: 2.4s;
}

@keyframes L1{
	50%{
		background-color: #dc3545;
	}
	
	100%{
		transform: rotateZ(180deg);
	}
}
</style>
<div class="body">
	<div>
		<div class="load-head">
			Single Object Tracker
		</div>
		<div class="loader">
			<span class="L1"></span>
			<span class="L2"></span>
			<span class="L3"></span>
			<span class="L4"></span>
			<span class="L5"></span>
			<span class="L6"></span>
			<span class="L7"></span>
			<span class="L8"></span>
			<span class="L9"></span>
		</div>
	</div>
</div>
Download code [here](https://github.com/shivanshuman021/Object-Tracker/blob/master/05_Single_Tracking.py)

    $ python 05_Single_Tracking.py
    
_Download the video demonstration for a single object tracker [here](https://github.com/shivanshuman021/Object-Tracker/blob/master/SINGLE_Tracker.mp4)_ 
    
#### Dependencies -
- [Python](https://python.org)
- [OpenCV](https://opencv.org)
- [OpenCV contrib modules](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAAegQIARAB&url=https%3A%2F%2Fpypi.org%2Fproject%2Fopencv-contrib-python%2F&usg=AOvVaw2CmQK0gZWG751zsw_Nm6X7)
      

<style>
*{
	margin :0;
	padding:0;
}

.body {
	margin-top:8%;
  	display: flex;
  	justify-content: center;
  	align-items: center;
  	background-color: #333;
  	font-weight: bold;
  	height: 100px;
}

.load-head{
	color : #f1f1f1;
	font-family: sans-serif;
	font-size: 30px;
	margin-bottom: 1%;  
}

.loader{
	height: 30px;
	width: 300px;
	display: flex;
}

.loader span{
	width: 30px;
	height: 30px;
	background: white;
	margin: 1px; 
}

.L1{
	content: '1';
	animation: L1 1s 1;
}

.L2{
	animation: L1 1s 1;
	animation-delay: 0.2s;
}

.L3{
	animation: L1 1s 1;
	animation-delay: 0.6s;
}

.L4{
	animation: L1 1s 1;
	animation-delay: 0.9s;
}

.L5{
	animation: L1 1s 1;
	animation-delay: 1.2s;
}

.L6{
	animation: L1 1s 1;
	animation-delay: 1.5s;
}

.L7{
	animation: L1 1s 1;
	animation-delay: 1.8s;
}

.L8{
	animation: L1 1s 1;
	animation-delay: 2.1s;
}

.L9{
	animation: L1 1s 1;
	animation-delay: 2.4s;
}

@keyframes L1{
	50%{
		background-color: #dc3545;
	}
	
	100%{
		transform: rotateZ(180deg);
	}
}
</style>
<div class="body">
	<div>
		<div class="load-head">
			Multiple Object Tracker
		</div>
		<div class="loader">
			<span class="L1"></span>
			<span class="L2"></span>
			<span class="L3"></span>
			<span class="L4"></span>
			<span class="L5"></span>
			<span class="L6"></span>
			<span class="L7"></span>
			<span class="L8"></span>
			<span class="L9"></span>
		</div>
	</div>
</div>

Download [06_Multi_Tracking.py](https://github.com/shivanshuman021/Object-Tracker/blob/master/06_Multi_Tracking.py)	

    $ python 06_Multi_Tracking.py
    
This file has some bugs ! Will be updated after fixing them

### Animation Credit
[Sufiyan Ansari](https://suffisme.github.io/Snippets/index.html)

### Useful References -
- [Evaluation of Visual Tracking Algorithms for Embedded Devices](https://www.researchgate.net/profile/Francois_Christophe/publication/317803149_Evaluation_of_Visual_Tracking_Algorithms_for_Embedded_Devices/links/59a66ea4aca272895c166a6c/Evaluation-of-Visual-Tracking-Algorithms-for-Embedded-Devices.pdf)
    
- [Comparison of Tracking Techniques](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiliOuyoubpAhUCzTgGHUjuBHUQFjAEegQIBhAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F9%2F16%2F3336%2Fpdf&usg=AOvVaw31tj8iqIPZNMGKmoF1yj2y)

<style>

.body{
	margin-top:8%;
	background: #333;
	height: 100px;
	justify-content: center;
	align-items: center;
	display: flex;
}
.load-body{
	position: absolute;
	top :50%;
	left : 50%;
	transform: translate(-50%,-50%);
}

.load-body span{
	width: 40px;
	height: 40px;
	border-radius: 50%;
	display: inline-block;
	margin : 0 6px;
}

.circle1{
	background: #e74c3c;
	animation: circle1 1s infinite;
}
.circle2{
	background: #3498db;
	animation: circle2 1s infinite;
}
.circle3{
	background: #27ae60;
	animation: circle3 1s infinite;
}

@keyframes circle1{
	25%{
		transform: scale(1);
	}
	50%{
		transform: scale(1.3);
	}
	75%{
		transform: scale(1);
	}
	100%{
		transform: scale(1);
	}
}
@keyframes circle2{
	25%{
		transform: scale(1);
	}
	50%{
		transform: scale(1);
	}
	75%{
		transform: scale(1.3);
	}
	100%{
		transform: scale(1);
	}
}
@keyframes circle3{
	25%{
		transform: scale(1);
	}
	50%{
		transform: scale(1);
	}
	75%{
		transform: scale(1);
	}
	100%{
		transform: scale(1.3);
	}
}
</style>
<div class="body">
	<div class="load-body">
		<span class="circle1"></span>
		<span class="circle2"></span>
		<span class="circle3"></span>
	</div>
</div>
				


##### _Here is an Optical Flow tracker using [OpenCV](https://opencv.org/)_
The video below might not be played on mobile browser . Either view it in a Desktop Browser or download them here
- [OPTICAL FLOW 4.7 MB](https://github.com/shivanshuman021/Object-Tracker/raw/master/OPT_FLOW.mp4)
- [Object Tracker 9.55 MB](https://github.com/shivanshuman021/Object-Tracker/raw/master/SINGLE_Tracker.mp4)


<video width="620" height="440" src="./SINGLE_Tracker.mp4" type="video/mp4" controls>
