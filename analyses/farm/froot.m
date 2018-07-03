function v = froot(x, M, n, N, e, k)
% f function witch root is solution steady state farm
%   Input parameters are:
%       x: offered load
%       M: number of threads
%       n: number of servers in used
%       N: total number of servers
%       e: serial fraction
%       k: coordination latency
v = x*(M - n) - fC(n, N, e, k);
end

