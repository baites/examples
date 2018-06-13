addpath('erlang')
addpath('asympt')

N = 10;
U = 0.01:0.01:0.99;

K = size(U);
Ec1 = zeros(1, K(2));
Ec10 = zeros(1, K(2));
Ec100 = zeros(1, K(2));
Ec1000 = zeros(1, K(2));

for i = 1:K(2)
    Ec1(i) = erlangc(1, U(i));
    Ec10(i) = erlangc(10, U(i)*10);
    Ec100(i) = erlangc(100, U(i)*100);
    Ec1000(i) = erlangc(1000, U(i)*1000);
end

subplot(1,3,1)

plot(U, Ec1, 'Color', [.5 .5 .5], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Delay probability $C_N(U)$','interpreter','latex')
hold on;
plot(U, Ec10, 'g:', 'LineWidth', 2);
plot(U, Ec100, 'b--', 'LineWidth', 2);
plot(U, Ec1000, 'r-.', 'LineWidth', 2);
grid on
grid minor

legend('N = 1', 'N = 10', 'N = 100', 'N = 1000', 'Location', 'northwest')
legend('boxoff')
set(gca,'FontSize', 16);

for i = 1:K(2)
    Ec1(i) = erlangc(1, U(i))*U(i)/(1-U(i));
    Ec10(i) = erlangc(10, U(i)*10)*U(i)/(1-U(i));
    Ec100(i) = erlangc(100, U(i)*100)*U(i)/(1-U(i));
    Ec1000(i) = erlangc(1000, U(i)*1000)*U(i)/(1-U(i));
end

subplot(1,3,2)

plot(U, Ec1, 'Color', [.5 .5 .5], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Queue size $q$','interpreter','latex')
hold on;
plot(U, Ec10, 'g:', 'LineWidth', 2);
plot(U, Ec100, 'b--', 'LineWidth', 2);
plot(U, Ec1000, 'r-.', 'LineWidth', 2);
grid on
grid minor

set(gca,'FontSize', 16);

for i = 1:K(2)
    Ec1(i) = erlangc(1, U(i))*U(i)/(1-U(i));
    Ec10(i) = erlangc(10, U(i)*10)*U(i)/(10*(1-U(i)));
    Ec100(i) = erlangc(100, U(i)*100)*U(i)/(100*(1-U(i)));
    Ec1000(i) = erlangc(1000, U(i)*1000)*U(i)/(1000*(1-U(i)));
end

subplot(1,3,3)

plot(U, Ec1, 'Color', [.5 .5 .5], 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Waiting time $w$[$\mu^{-1}$]','interpreter','latex')
hold on;
plot(U, Ec10, 'g:', 'LineWidth', 2);
plot(U, Ec100, 'b--', 'LineWidth', 2);
plot(U, Ec1000, 'r-.', 'LineWidth', 2);
grid on
grid minor

set(gca,'FontSize', 16);
