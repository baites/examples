function C = fC(n, N, e, k)
%fC Corrected speedup model as function utilization (U) for HT CPUs
%   Input parameters are:
%       n: number of server in used
%       N: total number of servers
%       e: serial fraction
%       k: coordination latency
C = n;
if n > 1
    if n > N
        n = N;
    end
    C = n/(1 + e*(n-1) + k*(1-e)*(n-1)*n);
end
