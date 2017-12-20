svMeans = superVoxelMeans;
svCells = superVoxelCells;
voxCounts = zeros(cc,1);
for kk = 1:cc
    voxCounts(kk) = numel(svCells{kk});
    
end
opts_fkmeans.weight=sqrt(voxCounts);
opts_fkmeans.careful = true;
opts_fkmeans.maxIter = 200;
if size(svMeans,2) == 3
    svMeansLUV = rgb2luv(svMeans')';
else
    svMeansLUV(:,1:3) = rgb2luv(svMeans(:,1:3)')';
    svMeansLUV(:,4:end) = svMeans(:,4:end)*50;
end
clusterCount = 5 0;
index = colorKmeans(clusterCount,svMeansLUV,opts_fkmeans);