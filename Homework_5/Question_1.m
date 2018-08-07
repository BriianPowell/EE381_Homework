% Brian Powell 012362894
% EE381 - Chaw-Long Chu
%
% Homework_5
%
% Question_1
% X ranges from 0 to 50 and the interval on x-axis is 0.05, please plot pdf
% of Gamma Distribution for
% 1.(a=1,b=1) 2.(a=1,b=5) 3.(a=1,b=10) 4.(a=5,b=1) 5.(a=10,b=1)
% 6.(a=10,b=2)
%

clc
clear

z = (0:0.5:50);

%Gamma Distribution for each value
g1 = gampdf(z,1,1);
gg11 = g1/max(g1);

g2 = gampdf(z,1,5);
gg15 = g2/max(g2);

g3 = gampdf(z,1,10);
gg110 = g3/max(g3);

g4 = gampdf(z,5,1);
gg51 = g4/max(g4);

g5 = gampdf(z,10,1);
gg101 = g5/max(g5);

g6 = gampdf(z,10,2);
gg102 = g6/max(g6);
figure(1);

%Plotting 6 lines for each distribution
plot(z, gg11, 'r', 'LineWidth', 2);
hold on;
plot(z, gg15, 'g', 'LineWidth', 2);
hold on;
plot(z, gg110, 'k', 'LineWidth', 1);
hold on;
plot(z, gg51, 'b', 'LineWidth', 2);
hold on;
plot(z, gg101, 'y', 'LineWidth', 2);
hold on;
plot(z, gg102, 'p', 'LineWidth', 2);
title('Gamma Distribution');





