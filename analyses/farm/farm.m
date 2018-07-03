function [RunningThreads, Utilization, Throughput, ResponseTime] = farm(xrange, M, N, e, k)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

RunningThreads = [];
Utilization = [];
Throughput = [];
ResponseTime = [];

for x = xrange
    f = @(z) froot(x, M, z, N, e, k);
    n = fzero(f, 0);
    U = n/N;
    if U > 1
        U = 1;
    end
    X = x*(M-n);
    R = M/X - 1/x;
    RunningThreads = [RunningThreads; n];
    Utilization = [Utilization; U];
    Throughput = [Throughput; X];
    ResponseTime = [ResponseTime; R];
end

end

