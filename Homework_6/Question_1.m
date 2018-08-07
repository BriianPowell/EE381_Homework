% Brian Powell 012362894
% EE381 - Chaw-Long Chu
%
% Homework_6
%
% Get average of 2000 sampling of a) any 2000-number sampling from exponential 
% distribution and plot the histogram of these 2000 numbers against normal 
% distribution. Repeat the same calculation by b) 5-number sampling, and 
% c) 30-number sampling. Also, d) find the mean (u) and standard deviation 
% (o) of the population.
%

clc
clear   

% static variables;
p = 2000;
theta = 5;
n2 = 2;
n5 = 5;
n30 = 30;

% array functions for y average
yav2 = (p);
yav5 = (p);
yav30 = (p);

for i=1:p
   y2 = exppdf(rand(1,n2), theta);
   y5 = exppdf(rand(1,n5), theta);
   y30 = exppdf(rand(1,n30), theta);
   yav2(i) = sum(y2)/n2;
   yav5(i) = sum(y5)/n5;
   yav30(i) =sum(y30)/n30;
end

% mean2 = mean5  = mean30 = the mean of population (u)
% std2 * sqrt(2) = std5 * sqrt(5) = std30 * sqrt(30) = standard deviation
% of population (o)

mean2 = mean(yav2);
mean5 = mean(yav5);
mean30 = mean(yav30);

std2 = std(yav2);
std5 = std(yav5);
std30 = std(yav30);

variance2 = std2 * sqrt(2);
variance5 = std5 * sqrt(5);
variance30 = std30 * sqrt(30);

% mean2 = 0.1813
% mean5 = 0.1814
% mean30 = 0.1813   
% std2 = 0.0074     standard deviation of population is 0.0074 * sqrt(2) = 0.010465
% std5 = 0.0046     standard deviation of population is 0.0046 * sqrt(5) = 0.10286
% std30 = 0.0019    standard deviation of population is 0.0019 * sqrt(30) = 0.10406


figure(1);
histfit(yav2);
title('N = 2');

figure(2);
histfit(yav5);
title('N = 5');

figure(3);
histfit(yav30);
title('N = 30');