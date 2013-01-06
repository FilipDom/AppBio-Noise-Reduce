#Octave script
#Calculates the mean and standard deviation of D, D_noisy and D_denoised across all data sets

dataDir = '../dist/';
names = {'symmetric_0.5', 'symmetric_1.0', 'symmetric_2.0', 'asymmetric_0.5', 'asymmetric_1.0', 'asymmetric_2.0'};

dataSetCount = length(names);
means_D = zeros(1, dataSetCount);
std_D = zeros(1, dataSetCount);
means_noisy = zeros(1, dataSetCount);
std_noisy = zeros(1, dataSetCount);
means_denoised = zeros(1, dataSetCount);
std_denoised = zeros(1, dataSetCount);
for i = 1:dataSetCount
	name = names{i};
	filePath = [dataDir, name];
	[d_noisy, d_denoised] = myread(filePath);
	d = d_noisy - d_denoised;
	
	means_D(i) = mean(d);
	std_D(i) = std(d);
	
	means_noisy(i) = mean(d_noisy);
	std_noisy(i) = std(d_noisy);
	
	means_denoised(i) = mean(d_denoised);
	std_denoised(i) = std(d_denoised);
end