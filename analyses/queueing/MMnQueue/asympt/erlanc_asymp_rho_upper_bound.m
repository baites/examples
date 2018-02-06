function U = erlanc_asymp_rho_upper_bound(N, rho)
%erlanc_asymp_rho_upper_bound: Asymp (rho const) upper bound for Erlang C 
%   Asymptotic (rho const) upper bound for Erlang C
%   -N: number of servers
%   -rho: system load or server utilization (lambda/(mu x N))
%   Author: Victor E. Bazterra
%   Derived from tighter upper bound in:
%   -Janssen, A. J. E. M., J. S. H. Van Leeuwaarden, and Bert Zwart. 
%    "Refining square-root safety staffing by expanding Erlang C." 
%    Operations Research 59.6 (2011): 1512-1522.
alpha = sqrt(-2*N*(1-rho+log(rho)));
Phi = normcdf(alpha);
phi = exp(-alpha^2/2)/sqrt(2*pi);
U = phi/(sqrt(N)*(1-rho)*Phi);
if U > 1
    U = 1;
end
end

