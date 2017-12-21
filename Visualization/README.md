# Overview
Included here are scripts to visualize results from Brainbow Segmentation
# Basic Usage
- Run the segProjectionWrite_script.m to generate a jpg image that contains the Max Intensity Projection of all the clustered colors. 
- Users then look at the clustered group that contain the neuron of interest, write down the index of that group, and use that index in the write3dTifForIndividualComponents.m script.
- The write3dTifForindividualComponents.m script will create a tiff file with just the data from chosen group, or the chosen color.

