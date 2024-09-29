% Apply 2D Gaussian Filter
imdata1 = imread('book.jpg');
g_filter = imgaussfilt(imdata1, 0.5);

% Apply two 1D Gaussian Filters
sigma = sqrt(0.5);
gauss_i = (1/sqrt(2*pi*sigma))*exp(-1*(i^2/(2*(sigma^2))));
gauss_j = (1/sqrt(2*pi*sigma))*exp(-1*(j^2/(2*(sigma^2))));

smoothed_i = imfilter(imdata1, gauss_i,'conv');
smoothed_j = imfilter(imdata1, gauss_j, 'conv');


figure(1);
imshow(g_filter);
figure(2);
imshow(smoothed_j);