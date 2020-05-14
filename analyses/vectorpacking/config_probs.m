function P = config_probs(p, M)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

C = size(M);
C = C(2);
P = zeros(1,C);

for Q = 1:C
    n = M{Q};
    ns = size(n);
    ns = ns(2);
    for i = 1:ns
        P(Q) = P(Q) + mnpdf(n{i},p);
    end
end

end

