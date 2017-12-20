info = imfinfo('/home/quan/Desktop/bbdata/Composite-1.tif');
a = uint16(info(1).Height);
b = uint16(info(1).Width);
c = numel(info);
thisVol = zeros(a,b,c,3);
FileTif = '/home/quan/Desktop/bbdata/Composite-1.tif';
TifLink = Tiff(FileTif, 'r');
for i=1:c
   TifLink.setDirectory(i);
   thisVol(:,:,i,:)=TifLink.read();
end
TifLink.close();

% for zz = 1:c
%     for i = 1:3
%    thisVol(:,:,zz) = imread('/home/quan/Desktop/00656_5R_C01_RGB.tif','Index', zz);
% end
CHANNELCOUNT = 3; %% only 2 colors, switch to 3 color later

% for kk=1:size(bbVol,3)
%   for mm = 1:CHANNELCOUNT
%   %  bbVol(:,:,kk,mm)=thisVol(:,:,CHANNELCOUNT*(kk-1)+mm);
%     bbVol(:,:,kk,mm) = imread('/home/quan/Desktop/RGB.tif','Index',kk);
%   end
% end
bbVol = thisVol;
clear thisVol;
cd /home/quan/Desktop/brainbowSegmentation/bb/BM4D_v3p2/; sigma = 2000; parfor kk=1:CHANNELCOUNT; [tmp, ~] = bm4d(squeeze(bbVol(:,:,:,kk)), 'Gauss', sigma); bbVol(:,:,:,kk) = tmp; end;
cd /home/quan/Desktop/brainbowSegmentation/bb/data;
save -v7.3 dcai_brainbow_bm4d_sigma2000_00658.mat bbVol
