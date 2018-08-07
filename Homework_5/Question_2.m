% Brian Powell 012362894
% EE381 - Chaw-Long Chu
%
% Homework_5
%
% Question_2
% Use Normal Distribution to generate Chi-sqquare distribution (graph
% results of 1 degree of freedom and 10 degree of freedom)
%

n = 10000;

% Random Values for 1 degree of Freedom to 10 degrees of Freedom.
n_1 = randn(1,n);
n_2 = randn(1,n);
n_3 = randn(1,n);
n_4 = randn(1,n);
n_5 = randn(1,n);
n_6 = randn(1,n);
n_7 = randn(1,n);
n_8 = randn(1,n);
n_9 = randn(1,n);
n_10 = randn(1,n);
sigma = 1;

% Chi Square for 1 degree of freedom
chisquare_1 = (sigma * n_1.^2);

% Plotting and labeling first result
figure(1);
hist(chisquare_1, 500);
xlabel('Bins');
ylabel('Occurences');
title('Chi-Square Distribution Composed of 1 Normal Distribution');

% Chi Square for 10 degrees of freedom
chisquare_2 = (sigma * n_1.^2) + (sigma * n_2.^2) + (sigma * n_3.^2) + (sigma * n_4.^2) + (sigma * n_5.^2) + (sigma * n_6.^2) + (sigma * n_7.^2) + (sigma * n_8.^2) + (sigma * n_9.^2) + (sigma * n_10.^2);

% Plotting and labeling second result
figure(2);
hist(chisquare_2, 500);
xlabel('Bins');
ylabel('Occurences');
title('Chi-Square Distribution Composed of 10 Normal Distributions');