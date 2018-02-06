plot(x, Rsimu, 'r--', 'LineWidth', 1.5)
hold on;
plot(x, Rtheo, 'k', 'LineWidth', 1.5)
xlabel('U', 'Interpreter', 'latex');
ylabel('R [$\mu^{-1}$]', 'Interpreter', 'latex');
legend('Simulation', 'Theory', 'Location', 'NorthWest')
legend boxoff 
grid on
grid minor
set(gca,'fontsize', 18);