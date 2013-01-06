#Octave script
#Performs the one-sided t-tests on mean of D with null hypothesis of mean being 0 across all datasests

dataDir = '../dist/';
names = {'symmetric_0.5', 'symmetric_1.0', 'symmetric_2.0', 'asymmetric_0.5', 'asymmetric_1.0', 'asymmetric_2.0'};

dataSetCount = length(names);
signif_greater = zeros(1, dataSetCount);
pvals_greater = zeros(1, dataSetCount);
signif_smaller = zeros(1, dataSetCount);
pvals_smaller = zeros(1, dataSetCount);
for i = 1:dataSetCount
	name = names{i};
	filePath = [dataDir, name];
	[d_noisy, d_denoised] = myread(filePath);
	d = d_noisy - d_denoised;
	MEAN_NULL = 0;
	p_greater = t_test(d, MEAN_NULL, '>');
	pvals_greater(i) = p_greater;
	p_smaller = t_test(d, MEAN_NULL, '<');
	pvals_smaller(i) = p_smaller;
end
ALPHA = 0.05;
signif_greater = pvals_greater <= ALPHA;
signif_smaller = pvals_smaller <= ALPHA;