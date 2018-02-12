function U = erlangc_loose_upper_bound(N, U)
%erlanc_loose_upper_bound: Asymp upper bound for Erlang C 
%   Loose upper bound for Erlang C
%   -N: number of servers
%   -U: system load or server utilization (lambda/(mu x N))
%   Author: Victor E. Bazterra
%   Derived from tighter upper bound in:
%   -Janssen, A. J. E. M., J. S. H. Van Leeuwaarden, and Bert Zwart. 
%    "Refining square-root safety staffing by expanding Erlang C." 
%    Operations Research 59.6 (2011): 1512-1522.
alpha = sqrt(-2*N*(1-U + log(U)));
Phi = normcdf(alpha);
phi = exp(-alpha^2/2)/sqrt(2*pi);
U = phi/(sqrt(N)*(1-U)*Phi);
if U > 1
    U = 1;
end
end

