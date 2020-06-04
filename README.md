
<style>
.load-body{
	margin : 0;
	padding: 0;
	background: #34495E;
	height: 350px;
	display: flex;
	align-items: center;
	justify-content: center;
	font-family: "montserrat", sans-serif;
}

.loading{
	width:120px;
	height: 120px;
	box-sizing: border-box;
	border-radius: 50%; 
	border-top : 10px solid #e74c3c;
	position: relative;
	animation: load 2s linear infinite;
}

.loading::before,.loading::after{
content : '';
width: 120px;
height: 120px;
position: absolute;
left: 0;
top: -10px;
box-sizing : border-box;
border-radius: 50%;
}

.loading::before{
	border-top:10px solid #e67e22;
	transform: rotate(120deg);
}

.loading::after{
	border-top:10px solid #e67eff;
	transform: rotate(240deg);
}

.loading span{
	position: absolute;
	width: 120px;
	height: 120px;
	color: #fff;
	text-align: center;
	line-height: 120px;
	position: fixed;
	animation: antiload 2s linear infinite;
}

@keyframes load{
	to{
		transform: rotate(360deg);
	}
}

@keyframes antiload{
	to{
		transform: rotate(-360deg);
	}
}
</style>
<div class="load-body">
	<div class="loading">
		<span><h2>AM</h2></span>
	</div>
</div>
				
<B><I>
Object tracking is one of the trendy and under investigation topic of Computer Vision that
challenges with several issues that should be considered while creating tracking systems, such as, visual
appearance, occlusions, camera motion, and so on. In several tracking algorithms Convolutional Neural
Network (CNN) has been applied to take advantage of its powerfulness in feature extraction that convolutional
layers can characterize the object from different perspectives and treat tracking process from misclassification.
	</I></B>

				
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
  	height: 200px;
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
tracking outcomes with integration of object detection model, rather than using tracking algorithm or filter 

- Multiple Instance Learning [MIL](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)

- Kernalized Correlation Filter [KCF](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjr_eCDn-bpAhVh6nMBHctkCOYQFjACegQIAxAB&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F10%2F2%2F713%2Fpdf&usg=AOvVaw05SOT9pM4fR68LFLr6-Cq7)
      
- Tracker Learning Detection [TLD](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiUz6WyoObpAhUD63MBHU4_C5QQFjABegQIBRAB&url=http%3A%2F%2Fvision.stanford.edu%2Fteaching%2Fcs231b_spring1415%2Fpapers%2FKalal-PAMI.pdf&usg=AOvVaw1MM92z9XpbLgUBLwy2PFjw)

- Generic Object Tracking Using Regression Networks [GOTURN](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiivYrPoebpAhWTyjgGHbvHDUwQFjABegQIAhAB&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1604.01802&usg=AOvVaw0BQRhbH7dA0L_H4SqyY0Ho)

- Minimum Output Sum of Squared Error [MOSSE](https://ieeexplore.ieee.org/abstract/document/5539960)

This project implements all of the tracking algorithms using [OpenCV Tracking API](https://docs.opencv.org/3.4/d9/df8/group__tracking.html) available [OpenCV contrib](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIhcL0pebpAhUexjgGHQ7wAuUQFjAMegQIBRAB&url=https%3A%2F%2Fdocs.opencv.org%2F3.4.10%2Fd3%2Fd81%2Ftutorial_contrib_root.html&usg=AOvVaw1-ltthwNL7WsiqFPy-cNJ7) package

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
  	height: 200px;
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
