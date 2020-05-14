function [M, c] = map_configs(c, C)
%config_map Generate all the placement configuration.
%   Returns them in a cell array index by configuration utilization
K = size(c);
K = K(2)+1;
Q = 0;
n = zeros(1,K);
M{1} = n;
veto = containers.Map;
veto(arrayfun(@num2str, n)) = 1;
c = sort(c, 'descend');
[M, veto] = map_configs_iter(M, veto, n, c, 1, Q, C);
end

function [M, veto] = map_configs_iter(M, veto, n, c, i, Q, C)
K = size(c);
K = K(2)+1;
if i > K - 1
    n(K) = floor(C-Q);
    nkey = config2str(n);
    if veto.isKey(nkey)
        return
    end        
    [M, veto] = saveconfig(M, veto, nkey, n);    
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
    [M, veto] = map_configs_iter(M, veto, n, c, i+1, Qnew, C);
end
end

function s = config2str(n)
  s = arrayfun(@num2str, n, 'UniformOutput', false);
  s = sprintf('%s',s{:});
end

function [M, veto] = saveconfig(M, veto, nkey, n)
    N = size(M);
    N = N(2);
    M{N+1} = n;
    veto(nkey) = 1;
end