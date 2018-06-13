% Add path with Erlang C formulas
addpath('../erlang')

% System initial conditions
% Number of servers
NI = 100;
% Number of cutomers in queue
QI = 200;

% Extract system utilization
fwrap = @(x) faux(x, QI, NI);
UI = fzero(fwrap, 1.0);

% Compute plot range
fwrap = @(x) faux(x, 1.5*QI, NI);
Umax = fzero(fwrap, 1.0);
U = 0.01:(Umax - 0.01)/100:Umax;

% Print details of the initial conditions
fprintf('Initial number of servers: %d\n', NI)
fprintf('Initial queue lenght: %0.1f\n', QI)
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
line(xl, [QI QI], 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);

% Update system size using queue heuristic
NF = mmn(0.5, UI, NI);

% Plot updated elbow curve
for i = 1:K(2)
    Ec(i) = erlangc(NF,U(i)*NF)*U(i)/(1-U(i));
end
plot(U, Ec, 'Color', 'blue', 'LineWidth', 2);

% Compute system final condition
UF = UI*NI/NF;
QF = erlangc(NF,UF*NF)*UF/(1-UF);

% Print details of the initial conditions
fprintf('Final number of servers: %d\n', NF)
fprintf('Final queue lenght: %0.1f\n', QF)
fprintf('Final server utilization: %0.2f\n', UF)

line([UF UF], yl, 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [QF QF], 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);

set(gca,'FontSize', 16);

function R = faux(U, Q, N)
    R = Q*(1-U)/U - erlangc(N, U*N);
end

function NF = mmn(QF, UI, NI)
    NF = 1.1*UI*NI;
    while 1
        UF = UI*NI/NF;
        p = QF*(1-UF)/UF;
        N = erlangcinv(p, UF*NF);
        if N == NF || N+1 == NF
            NF = N;
            break
        end
        NF = N;
    end
end
