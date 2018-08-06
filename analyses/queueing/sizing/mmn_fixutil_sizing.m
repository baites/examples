% Add path with Erlang C formulas
addpath('../erlang')

% System initial conditions
% Number of servers
NI = 1000;
% Number of customers in queue
qI = 500;
% Fix overprovision
alpha = 0.25;

% Extract system utilization
fwrap = @(x) faux(x, qI, NI);
UI = fzero(fwrap, 1.0);

% Compute plot range
fwrap = @(x) faux(x, 1.5*qI, NI);
Umax = fzero(fwrap, 1.0);
U = 0.01:(Umax - 0.01)/100:Umax;

% Print details of the initial conditions
fprintf('Initial number of servers: %d\n', NI)
fprintf('Initial queue lenght: %0.1f\n', qI)
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
line(xl, [qI qI], 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);

% Update system size using queue heuristic
NF = ceil(NI + alpha*NI);

% Plot updated elbow curve
for i = 1:K(2)
    Ec(i) = erlangc(NF,U(i)*NF)*U(i)/(1-U(i));
end
plot(U, Ec, 'Color', 'blue', 'LineWidth', 2);

% Compute system final condition
UF = UI*NI/NF;
qF = erlangc(NF,UF*NF)*UF/(1-UF);

% Print details of the initial conditions
fprintf('Final number of servers: %d\n', NF)
fprintf('Final queue lenght: %0.1f\n', qF)
fprintf('Final server utilization: %0.2f\n', UF)

line([UF UF], yl, 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [qF qF], 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);

set(gca,'FontSize', 16);

function R = faux(U, Q, N)
    R = Q*(1-U)/U - erlangc(N, U*N);
end
