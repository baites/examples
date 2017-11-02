% Homogeneous natural sequence
b = [0 1]
a = [2 -1]
LinearRecurrenceSequence('Positive integers (A000027)', 20, a, b)

% Inhomogeneous natural sequence
b = (0);
a = (1);
c = [1 -1];
d = [1];
LinearRecurrenceSequence('Non-homogeneous positive interngers (A000027)', 20, a, b, c, d)

% Fibonacchi sequence
b = [0 1];
a = [1 1];
LinearRecurrenceSequence('Fibonacchi (A000045)', 20, a, b)

% Tribonacci A000073
b = [0 0 1];
a = [1 1 1];
LinearRecurrenceSequence('Tribonacci (A000073)', 20, a, b)

% Tetranacci A000078
b = [0 0 0 1];
a = [1 1 1 1];
LinearRecurrenceSequence('Tetranacci (A000078)', 20, a, b)

% Pentanacci A001591
b = [0 0 0 0 1];
a = [1 1 1 1 1];
LinearRecurrenceSequence('Pentanacci (A001591)', 20, a, b)

% A006904 sequence
b = [1 1];
a = [1 2];
c = [1 1];
d = [1];
LinearRecurrenceSequence('Non-homogeneous A006904', 20, a, b, c, d)

% (P,Q)-Fibonacchi
P = 1;
Q = 2;
b = [0,1];
a = [P,Q];
LinearRecurrenceSequence('(1,2)-Fibonacchi: Jacobsthal (A001045)', 20, a, b)

% (P,Q)-Lucas of second kind
P = 2;
Q = 1;
b = [2,P];
a = [P,Q];
LinearRecurrenceSequence('(2,1)-Lucas: Companion Pell (A002203)', 20, a, b)



function P0 = CreateP0(a,b)
%CreateP0 Create the P0 polynomial
%   P0 polynomial is the numerator of the 
%   rational function that generate the homogeneous sequece
    if size(a,1) ~= 1 || size(b,1) ~= 1
        error('Error inputs need to be array of dim 1xm');
    end
    if size(a,2) ~= size(b,2)
        error('Error the inputs should be same dimension');
    end
    M = size(b,2);
    p = zeros(1,M);
    for n = 1:M
        if n == 1
            p(n) = b(1);
            continue;
        end
        p(n) = b(n);
        for m = 1:n-1
            p(n) = p(n) - a(m) * b(n-m);
        end
    end
    P0 = fliplr(p);
end

function Q0 = CreateQ0(a)
%CreateQ0 Create the Q0 polynomial
%   Q0 polynomial is the denominator of the rational 
%   function that generate the homogeneous sequece
    M = size(a,2);
    q = ones(1,M);
    for n = 2:M+1
        q(n) = -a(n-1);
    end
    Q0 = fliplr(q);
end

function [P,Q] = CreateG(a, b, c, d)
    Q0 = CreateQ0(a);
    P0 = CreateP0(a,b);
    QI = fliplr(c);
    PI = fliplr(d);
    M = size(a,2);
    zM = zeros(1,M+1);
    zM(1) = 1;
    P = conv(P0,QI) + conv(zM,PI);
    Q = conv(Q0,QI);
end

function f = EvalCloseForm(r, p, h, n, format)
%EvalCloseForm Compute a sequence value based its close form
%   Evaluate a close form base on coefficients(c) and roots(r)
    if size(r,1) ~= size(p,1)
        error('Residue array and poles should be same length');
    end
    M = size(r,1);
    f = 0;
    k = 0;
    pold = 0;
    for i = 1:M
        if k == 0 || p(i) ~= pold
            k = 1;
        else
            k = k + 1;
        end
        f = f + (-1)^k * nchoosek(k+n-1, n) * r(i) * p(i)^-(n+k);
        if i == n && n < size(h,1)
            f = f + h(i);
        end
        pold = p(i);            
    end    
    if format == 'integer'
        f = int64(round(real(f)));
    elseif format == 'real'
        f = real(f);
    end
end

function y = RemoveLeadingZeros(x)
%RemoveLeadingZeros Remove leading ceros
%   Leading zeros meant nothing for polynomials
    index = 1;
    for i = 1:size(x,2)
        if x(i) ~= 0
            index = i;
            break
        end
    end
    y = x(index:end);
end

function LinearRecurrenceSequence(name, n, a, b, c, d)
%LinearRecurrenceSequence Compute a sequence value based its close form
%   Evaluate a close form base on coefficients(c) and roots(r)

    switch nargin
        case 4
            c = zeros(1,size(a,2)+1);
            c(1) = 1;
            d = zeros(1,size(a,2));
    end

    fprintf('Name: %s\n', name)
    fprintf('Degree: %d\n', size(a,2))
    fprintf('\n')

    fprintf('Recurrence coefficients')
    a
    fprintf('Initial conditions')
    b
    fprintf('\n')

    if size(d,2) == 1 && d(1) ~= 0
        fprintf('Non-homogeneous rational polynomials\n')
        fprintf('QI:')
        disp(c)
        fprintf('PI:')
        disp(d)
    end
    fprintf('Generating function\n')
    [P,Q] = CreateG(a,b,c,d);
    fprintf('P: ')
    disp(RemoveLeadingZeros(P))
    fprintf('\n')
    fprintf('Q: ')
    disp(RemoveLeadingZeros(Q))
    fprintf('\n')
    
    fprintf('Partial fraction expantion\n')
    [r,p,h] = residue(P,Q);
    fprintf('residue (r)  : ')
    disp(r')
    fprintf('poles: (eta) : ')
    disp(p')
    fprintf('remainder (h): ')
    disp(h')
    fprintf('\n\n\n') 
    if size(d,2) > 0 && size(h,1) == 0
        fprintf('Can be reduce to homogeneous type\n')
        fprintf('Recurence coefficients : ')
        a = fliplr(Q);
        for i = 2:size(Q,2) 
            a(i) = -a(i);
        end
        disp(a(2:size(Q,2)))
        fprintf('Initial conditions : ')
        N = size(p,1);
        t = zeros(1,N);
        for i = 1:N
            t(i) = EvalCloseForm(r, p, h, i-1, 'integer');
        end
        disp(t)
        fprintf('\n')
    end
        
    fprintf('Sequence (%d)\n', n)
    t = zeros(1,n);
    for i = 1:n
        t(i) = EvalCloseForm(r, p, h, i-1, 'integer');
    end
    disp(t)
    fprintf('\n\n')
    fprintf('------------------------')
    fprintf('\n\n')
end