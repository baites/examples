addpath('erlang')
addpath('asympt')

N = 10;
U = 0.01:0.01:0.98;

K = size(U);
Ec = zeros(1, K(2));
UpT = zeros(1, K(2));
UpL = zeros(1, K(2));

for i = 1:K(2)
    Ec(i) = erlangc(N,U(i)*N);
    UpT(i) = erlangc_upper_bound(N,U(i));
    UpL(i) = erlangc_loose_upper_bound(N,U(i));
end

plot(U, Ec, 'Color', [.5 .5 .5], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Delay probability','interpreter','latex')
hold on;
plot(U, UpT, 'b:', 'LineWidth', 2);
plot(U, UpL, 'r--', 'LineWidth', 2);
grid on
grid minor

legend('Enlang C','Upper tight bound','Upper loose bound', 'Location', 'northwest')
legend('boxoff')
set(gca,'FontSize', 16);
