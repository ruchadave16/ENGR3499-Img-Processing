imdata1 = imread('book.jpg');
imdata2 = imread('pumpkin.jpg');
imdata3 = imread('red_chair.jpg');
brightness_value = 50;
contrast_value = 10;        %choose a multiplier
std2 = 10;
I = [0 0 0; 0 1 0; 0 0 0];

img1 = imread('book.jpg');
img2 = imread("pumpkin.jpg");
img3 = imread("red_chair.jpg");
[r,g,b] = imsplit(img1);

% figure;
% imhist(r)
% title('Red Channel')
% figure;
% imhist(g)
% title('Green Channel')
% figure;
% imhist(b)
% title('Blue Channel')
[h,s,v] = rgb2hsv(img1);
figure;
imhist(h);
title("Hue")
figure;
imhist(s);
title("Saturation")
figure;
imhist(v);
title("Value")
computer_I = imfilter(imdata1, I, 'conv');
computer_G2 = imgaussfilt(imdata1, std2);

brighter_img1 = imdata1 + 100;
% imshow(brighter_img1)

contrast_img1 = imdata1 * 2;
% imshow(contrast_img1)

% Btw this is for alternating brightness of every other pixel but still
% needs some debugging
% img1_odd = imdata1(mod());
% imdata1(mod(imdata1,2)==0) = imdata1(mod(imdata1,2)==0)+100;
% imshow(imdata1)





