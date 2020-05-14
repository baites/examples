function [M, c] = map_configs(c, C)
%config_map Generate all the placement configuration.
%   Returns them in a cell array index by configuration utilization
K = size(c);
K = K(2);
Q = 0;
n = zeros(1,K);
M{Q+1}{1} = n;
veto = containers.Map;
veto(arrayfun(@num2str, n)) = 1;
c = sort(c, 'descend');
[M, veto] = map_configs_iter(M, veto, n, c, 1, Q, C);
end

function [M, veto] = map_configs_iter(M, veto, n, c, i, Q, C)
K = size(c);
K = K(2);
if i > K
    return
end
nmax = (C-Q)/c(i);
fnmax = floor((C-Q)/c(i));
if fnmax == 0
    return
end
for j = 0:fnmax
    n(i) = j;
    Qnew = Q + j * c(i);
    M = map_configs_iter(M, veto, n, c, i+1, Qnew, C);
    nkey = config2str(n);
    if veto.isKey(nkey)
        continue
    end
    S = size(M);
    N = 0;
    if Qnew+1 <= S(2)
        N = size(M{Qnew+1});
        N = N(2);
    end
    M{Qnew+1}{N+1} = n;
    veto(nkey) = 1;
end
end


function s = config2str(n)
  s = arrayfun(@num2str, n, 'UniformOutput', false);
  s = sprintf('%s',s{:});
end