function model_mmn_queue(N, lambda, mu)
%model_mmn_queue Compute the result of M/M/N queue model
%   Compute the result of M/M/N queue model based on Erlang-C function

addpath('erlang')

% Compute all parameters
x = lambda/mu;
U = x/N;
assert(U < 1, 'Utilization is not less than one, no steady-state solution')
C = erlangc(N, x);
n = x;
q = C * U / (1 - U);
p = q + n;
w = C / (N * (1 - U));
R = w + 1;

fprintf('Number of busy servers: %0.1f\n', n)
fprintf('Server utilization: %0.2f\n', U)
fprintf('Throughput: %0.1f\n', x * mu)
fprintf('Number of customers in queue: %0.1f\n', q)
fprintf('Number of customers in system: %0.1f\n', p)
fprintf('Queue waiting time: %0.2f\n', w/mu)
fprintf('Response time: %0.2f\n', R/mu)

end

