#Function used to read in data from the tab delimited text files containing distance from reference tree information.
function [d_noisy, d_denoised] = myread(filePath)

DELIMITER = '\t';
START_ROW = 1;
START_COL = 1;
data = dlmread(filePath, DELIMITER, START_ROW, START_COL);
d_noisy = data(:,1);
d_denoised = data(:,2);