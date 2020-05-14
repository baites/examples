function P = config_probs(x, p, M)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

C = sum(M{2});
P = zeros(1, C+1);
Ms = size(M);
Ms = Ms(2);

p = (1 - x) * p;
ps = size(p);
ps = ps(2);
p(ps+1) = x;

for i = 2:Ms
    idle = M{i}(end);
    M{i}
    a = C - idle
    P(C-idle+1) = P(C-idle+1) + mnpdf(M{i}, p);
end

P = P/sum(P);

end

