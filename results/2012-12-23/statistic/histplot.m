#Octave script
#Calculates and plots the histograms of D for all data sets, assembling them on a single figure

dataDir = '../dist/';
names = {'symmetric_0.5', 'symmetric_1.0', 'symmetric_2.0', 'asymmetric_0.5', 'asymmetric_1.0', 'asymmetric_2.0'};

ROWS = 2;
COLS = 3;
for i = 1:length(names)
	subplot(ROWS, COLS, i)
	name = names{i};
	filePath = [dataDir, name];
	[d_noisy, d_denoised] = myread(filePath);
	d = d_noisy - d_denoised;
	hist(d);
	nameTitle = regexprep(name, '_', '\_');
	title(['D hist for ', nameTitle]);
end