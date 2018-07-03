% Add path with Erlang C formulas
addpath('../erlang')

% System initial conditions
% Number of servers
NI = 1000;
% Number of customers in queue
Q1 = 500;
% Overprovision
beta = 2.29;

% Extract system utilization
fwrap = @(x) faux(x, Q1, NI);
UI = fzero(fwrap, 1.0);

% Compute plot range
fwrap = @(x) faux(x, 1.5*Q1, NI);
Umax = fzero(fwrap, 1.0);
U = 0.01:(Umax - 0.01)/100:Umax;

% Print details of the initial conditions
fprintf('Initial number of servers: %d\n', NI)
fprintf('Initial queue lenght: %0.1f\n', Q1)
fprintf('Initial server utilization: %0.2f\n', UI)

% Generate the elbow curve
K = size(U);
Ec = zeros(1, K(2));

for i = 1:K(2)
    Ec(i) = erlangc(NI,U(i)*NI)*U(i)/(1-U(i));
end

plot(U, Ec, 'Color', 'red', 'LineWidth', 2);
xlabel('Server utilization $U$','interpreter','latex')
ylabel('Queue size $q$','interpreter','latex')
grid on
grid minor

% Show initial system condition
hold on;
xl = xlim;
yl = ylim;
line([UI UI], yl, 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [Q1 Q1], 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);

% Update system size using queue heuristic
NF = ceil(NI + beta * sqrt(NI));

% Plot updated elbow curve
for i = 1:K(2)
    Ec(i) = erlangc(NF,U(i)*NF)*U(i)/(1-U(i));
end
plot(U, Ec, 'Color', 'blue', 'LineWidth', 2);

% Compute system final condition
UF = UI*NI/NF;
Q2 = erlangc(NF,UF*NF)*UF/(1-UF);

% Print details of the initial conditions
fprintf('Final number of servers: %d\n', NF)
fprintf('Final queue lenght: %0.1f\n', Q2)
fprintf('Final server utilization: %0.2f\n', UF)

line([UF UF], yl, 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [Q2 Q2], 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);

set(gca,'FontSize', 16);

function R = faux(U, Q, N)
    R = Q*(1-U)/U - erlangc(N, U*N);
end
