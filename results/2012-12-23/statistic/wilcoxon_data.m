#Octave script
#Performs the one-sided wilcoxon signed-rank tests to compare D_noisy and D_denoised across all datasests

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
	p_greater = wilcoxon_test(d_noisy, d_denoised, '>');
	pvals_greater(i) = p_greater;
	p_smaller = wilcoxon_test(d_noisy, d_denoised, '<');
	pvals_smaller(i) = p_smaller;
end
ALPHA = 0.05;
signif_greater = pvals_greater <= ALPHA;
signif_smaller = pvals_smaller <= ALPHA;