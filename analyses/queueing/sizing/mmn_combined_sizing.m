% Add path etaith Erlang C formulas
addpath('../erlang')

% Condition range
% Number of busy servers
n = 0:5:10000;
% Safeties
epsilon = 10;
alpha = 0.25;
beta = 2.3;
eta = 200;

nsize = size(n);
U = zeros(1, nsize(2));
q = zeros(1, nsize(2));

for i = 1:nsize(2)
    N = ceil(n(i)+max(epsilon, alpha*n(i)*exp(-n(i)/eta) + beta*sqrt(n(i))*(1-exp(-n(i)/eta))));
    U(i) = n(i)/N;
    q(i) = erlangc(N,n(i))*U(i)/(1-U(i));
end

subplot(1,2,1)
plot(n, q, 'LineWidth', 2);
xlabel('Number of busy servers $n$','interpreter','latex')
ylabel('Queue size $q$','interpreter','latex')
grid on
grid minor
ylim([0 1]);
set(gca,'FontSize', 16);

subplot(1,2,2)
plot(n, U, 'LineWidth', 2);
xlabel('Number of busy servers $n$','interpreter','latex')
ylabel('Server utilization $U$','interpreter','latex')
grid on
grid minor
set(gca,'FontSize', 16);
