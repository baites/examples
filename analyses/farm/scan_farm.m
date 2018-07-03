% Farm parameter
M = 200;
N = 100;

% HT parameters
e = 0.01;
k = 0.001;

xrange = 0.001:0.001:10.0;

[P, U, T, R] = farm(xrange, M, N, e, k);
subplot(1,2,1);
plot(P, R) 
xlabel('Running processes');
ylabel('Response time [\mu^{-1}]');
grid on;
grid minor;
set(gca,'fontsize',18);

subplot(1,2,2);
plot(P, T)
xlabel('Running processes');
ylabel('Throughput [\mu]');
grid on;
grid minor;
set(gca,'fontsize',18);
