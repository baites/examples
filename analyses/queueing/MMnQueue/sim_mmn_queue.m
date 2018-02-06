addpath('erlang')
lambda = 0.5;
mu = 1;
N = 10;
load_system('MMNQueue');

sample = 0.1:0.1:1.4;
x = zeros(size(sample));
Rsimu = zeros(size(sample));
Rtheo = zeros(size(sample));

for i = 1:size(sample,2)
    x(i) = 1.0 - 10.0^(-sample(i));
    lambda = x(i) * N;
    sim('MMNQueue');
    Rsimu(i) = ResponseTime(end);
    C = erlangc(N, lambda/mu);
    Rtheo(i) = C/(N*mu - lambda) + 1/mu;
end
