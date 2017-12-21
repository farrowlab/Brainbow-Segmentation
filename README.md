# Brainbow-Segmentation

# Overview
- This Repo includes Scripts needed to segment individual neurons in a Brainbow stack
- Some codes are modified to be in Python, with GPU acceleration.
- The rest are written in Matlab.
- Basically, the image is denoised, then segmented and clustered by colors, and finally users manipulate the clustering scheme to pick the cluster that contains cell of interest.

# Step by Step guide
After combining the 3 channels of the image by creating a composite, save stacks as tiff file.
1) Go into bmd3 folder, open the denoiseGPU.py script, change the file name of the image to be processed, as well as the denoise sigma level, default at 1000, and run the script to get a denoise tiff file in the same folder.

2) Go into the SegmentationScripts folder, open the superVoxelizationScript, and edit the file location of the newly created denoise tiff stack. It should be something like: info = iminfo('/home/user/brainBowSegmentation/bm3d-gpu/denoise_image.tif')

3) Run this SegmentationScripts. It will take a while, depending on how big the file is. After this script has finished running, The user has to specified the number of cluster, default is 20, and they can do so in the clusterK.m script, by assigning the clusterCount variable to the appropriate number of cluster. This has to be done by trial and error, but the clusterK script is really fast, so once all the variable in the SegmentationScripts are calculated, user can rerun the clusterK script as many time as they want.


4) Next step would be to visualize the result and manipulate the cluster number, to make sure the clustering result is correct, as in the colors separated contains separated neurons.

5) Open the Visualization folder, and run the segProjectionWrite_script.m file. This script will create a jpg files with the maximum intensity projection of all the separated colors. Check the result to see if neuron with corresponding dendrites are retained. If not, adjust the number of cluster accordingly.

6) Then, once user find a cluster that contains good result, user can use the write3dTiffForIndividualComponents, specify the cluster group the neuron of interest are in, and then have the script create a tiff stack that just contain the Individual neuron and nothing else. 
