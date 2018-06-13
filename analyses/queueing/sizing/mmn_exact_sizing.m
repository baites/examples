% Add path with Erlang C formulas
addpath('../erlang')

% System initial conditions
% Number of servers
N1 = 1000;
% Number of cutomers in queue
Q1 = 500;

% Extract system utilization
fwrap = @(x) faux(x, Q1, N1);
U1 = fzero(fwrap, 1.0);

% Compute plot range
fwrap = @(x) faux(x, 1.5*Q1, N1);
Umax = fzero(fwrap, 1.0);
U = 0.01:(Umax - 0.01)/100:Umax;

% Print details of the initial conditions
fprintf('Initial number of servers: %d\n', N1)
fprintf('Initial queue lenght: %0.1f\n', Q1)
fprintf('Initial server utilization: %0.2f\n', U1)

% Generate the elbow curve
K = size(U);
Ec = zeros(1, K(2));

for i = 1:K(2)
    Ec(i) = erlangc(N1,U(i)*N1)*U(i)/(1-U(i));
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
line([U1 U1], yl, 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [Q1 Q1], 'Color', 'red', 'LineStyle', ':', 'LineWidth', 1.5);

% Update system size using queue heuristic
N2 = mmn(0.5, U1, N1);

% Plot updated elbow curve
for i = 1:K(2)
    Ec(i) = erlangc(N2,U(i)*N2)*U(i)/(1-U(i));
end
plot(U, Ec, 'Color', 'blue', 'LineWidth', 2);

% Compute system final condition
U2 = U1*N1/N2;
Q2 = erlangc(N2,U2*N2)*U2/(1-U2);

% Print details of the initial conditions
fprintf('Final number of servers: %d\n', N2)
fprintf('Final queue lenght: %0.1f\n', Q2)
fprintf('Final server utilization: %0.2f\n', U2)

line([U2 U2], yl, 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);
line(xl, [Q2 Q2], 'Color', 'blue', 'LineStyle', ':', 'LineWidth', 1.5);

set(gca,'FontSize', 16);

function R = faux(U, Q, N)
    R = Q*(1-U)/U - erlangc(N, U*N);
end

function N2 = mmn(Q2, U1, N1)
    N2 = 1.1*U1*N1;
    while 1
        U2 = U1*N1/N2;
        p = Q2*(1-U2)/U2;
        N = erlangcinv(p, U2*N2);
        if N == N2 || N+1 == N2
            N2 = N;
            break
        end
        N2 = N;
    end
end
