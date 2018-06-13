addpath('erlang')
addpath('asympt')

N = 10;
U = 0.01:0.01:0.98;

K = size(U);
Ec = zeros(1, K(2));
Lw = zeros(1, K(2));
Up = zeros(1, K(2));

for i = 1:K(2)
    Lw(i) = erlanc_lower_bound(N,U(i));
    Ec(i) = erlangc(N,U(i)*N);
    Up(i) = erlanc_upper_bound(N,U(i));
end

subplot(1,3,1)

plot(U, Ec, 'Color', [.8 .8 .8], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Delay probability $C_N(U)$','interpreter','latex')
hold on;
plot(U, Lw, 'b:', 'LineWidth', 2);
plot(U, Up, 'r--', 'LineWidth', 2);
grid on
grid minor

legend('Enlang C','Lower bound','Upper bound','Location','northwest')
legend('boxoff')
set(gca,'FontSize', 16);

for i = 1:K(2)
    Lw(i) = erlanc_lower_bound(N,U(i))*U(i)/(1-U(i));
    Ec(i) = erlangc(N,U(i)*N)*U(i)/(1-U(i));
    Up(i) = erlanc_upper_bound(N,U(i))*U(i)/(1-U(i));    
end

subplot(1,3,2)

plot(U, Ec, 'Color', [.8 .8 .8], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Queue size $q$','interpreter','latex')
hold on;
plot(U, Lw, 'b:', 'LineWidth', 2);
plot(U, Up, 'r--', 'LineWidth', 2);
grid on
grid minor

set(gca,'FontSize', 16);

for i = 1:K(2)
    Lw(i) = erlanc_lower_bound(N,U(i))/(N*(1-U(i)));
    Ec(i) = erlangc(N,U(i)*N)/(N*(1-U(i)));
    Up(i) = erlanc_upper_bound(N,U(i))/(N*(1-U(i)));    
end

subplot(1,3,3)

plot(U, Ec, 'Color', [.8 .8 .8], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Waiting time $w$ [$\mu^{-1}$]','interpreter','latex')

hold on;
plot(U, Lw, 'b:', 'LineWidth', 2);
plot(U, Up, 'r--', 'LineWidth', 2);
grid on
grid minor

set(gca,'FontSize', 16);
