# PeSOTIF
The first batch of the PeSOTIF dataset includes 1126 frames of data that covers different weather, seasons, and times of the day. This work labeled 11 categories of traffic participants, including car, bus, truck, train, bike, motor, person, rider, traffic sign, traffic light, and traffic cone. In the YOLO format, each frame of image has a .txt file to store its annotations. Besides, the dataset is also reorganized as the COCO format for quick use. In addition to the category and bounding box parameters, a binary factor has been added to the annotation of each object to indicate whether the object is safety critical in the scenario. The ability to recognize the key object in the keyframe may be reduced due to trigger conditions in the scenario. In summary, there are 2555 key objects and 2778 key objects labeled. The demonstration video shows the basic information of the dataset.

# Data collection
The PeSOTIF dataset aims to be a diverse test dataset for perception SOTIF problems currently, thus collects key frames of critical traffic scenarios extracted from multiple data sources. In the future, after collecting sufficient corner cases, decomposing a training dataset to improve the algorithm performance will be considered.  
The first part of the data comes from experiments designed to study trigger conditions and performance boundaries under different rain intensity and illumination intensity in previous works. A FLIR color camera was used to collect the data. Model: GS3-U3-41C6C-C; CMOSISCMV4000-3E5; global shutter; gain: -7.742dB to 24dB; high dynamic range: cycle 4 gain and exposure presets; frequency: 90Hz; 4.1MP; image size: 2048×2048; lens: FA1215A; lens hFov: -53.6°-53.6°; lens vFov: -41.8°-41.8°; lens focal length: 12mm. About two frames in each group of experiments were extracted and added to the PeSOTIF dataset.   
The second part of the data comes from traffic accident videos. There are thousands of videos uploaded by the perception task group of the China SOTIF technical alliance. These videos were screened from road test data, public traffic accident databases, and even clips-sharing sites like YouTube. This work has browsed these videos, further filtered out the scenarios related to perception SOTIF problems. Then, the key frames that may cause perception failure and traffic accidents were located and added to the PeSOTIF dataset.    
In addition, we also carefully selected some images that meet our requirements from the test subset of the existing data sets, including BDD100k, COCO, KITTI, Raindrop, ExDark and Radiate. For on-board traffic data sets, some scenarios affected by the perceptual trigger conditions were added to the PeSOITF dataset. For visual detection data sets under adverse environment, some outdoor data was extracted.

# Contact us
Only a few samples have been disclosed in this repo. If you would like to use this dataset for academic research, please contact me or my tutor.    
E-mails:    
hong_wang@mail.tsinghua.edu.cn    
peng-l20@mails.tsinghua.edu.cn

# Cite us
Please kindly cite us if you make contributions to or by the dataset.    
Papers:    
https://link.springer.com/article/10.1007/s42154-021-00154-0    
https://ieeexplore.ieee.org/abstract/document/9827365    
https://arxiv.org/abs/2211.03402    
https://arxiv.org/abs/2211.04009
