clear all
load('dcai_brainbow_bm4d_sigma2000_00658.mat');
for i = 1:size(bbVol,3)
    tem(:,:,1) = bbVol(:,:,i,1);
tem(:,:,2) = bbVol(:,:,i,2);
tem(:,:,3) = bbVol(:,:,i,3);

tem = tem ./ max(tem(:));
if i ==1
imwrite(tem,'test6.tif');
else
imwrite(tem, 'test6.tif', 'writemode', 'append');
end
end