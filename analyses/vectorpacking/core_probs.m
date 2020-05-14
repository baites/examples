function [Q,PQ] = core_probs(P)

indexes = find(P > 0);
sindexes = size(indexes);
sindexes = sindexes(2);

PQ = zeros(1, sindexes);
NQ = zeros(1, sindexes);
Q = zeros(1, sindexes);

PQ(sindexes) = P(indexes(end));
NQ(sindexes) = 1 - P(indexes(end));
Q(sindexes) = indexes(sindexes) - 1;

for i = sindexes-1:-1:1    
    PQ(i) = P(indexes(i)) * NQ(i+1);
    NQ(i) = (1 - P(indexes(i))) * NQ(i+1);
    Q(i) = indexes(i) - 1;
end

end

