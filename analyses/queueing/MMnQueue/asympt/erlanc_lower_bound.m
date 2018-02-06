function L = erlanc_lower_bound(N, rho)
%erlanc_lower_bound: Tight upper bound for Erlang C
%   Tight lower bound for Erlang C
%   -N: number of servers
%   -rho: system load or server utilization (lambda/(mu x N))
%   Author: Victor E. Bazterra
%   Reference:
%   -Janssen, A. J. E. M., J. S. H. Van Leeuwaarden, and Bert Zwart. 
%    "Refining square-root safety staffing by expanding Erlang C." 
%    Operations Research 59.6 (2011): 1512-1522.
alpha = sqrt(-2*N*(1-rho+log(rho)));
Phi = normcdf(alpha);
phi = exp(-0.5*alpha^2)/sqrt(2*pi);
gamma = (1-rho)*sqrt(N); 
L = 1/(rho + gamma*(Phi/phi + (2/3)/sqrt(N) + 1/(phi*(12*N-1))));
end

