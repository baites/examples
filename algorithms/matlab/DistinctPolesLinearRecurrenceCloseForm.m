% Fibonacchi (A000045)
b = [0 1]
a = [1 1]
LinearRecurrenceSequence('Fibonacchi (A000045)', 20, a, b)

% Tribonacci (A000073)
b = [0 0 1];
a = [1 1 1];
LinearRecurrenceSequence('Tribonacci (A000073)', 20, a, b)

% Tetranacci (A000078)
b = [0 0 0 1];
a = [1 1 1 1];
LinearRecurrenceSequence('Tetranacci (A000078)', 20, a, b)

% Pentanacci (A001591)
b = [0 0 0 0 1];
a = [1 1 1 1 1];
LinearRecurrenceSequence('Pentanacci (A001591)', 20, a, b)

% (P,Q)-Fibonacchi
P = 1;
Q = 2;
b = [0 1];
a = [P Q];
LinearRecurrenceSequence('(1,2)-Fibonacchi: Jacobsthal (A001045)', 20, a, b)

% (P,Q)-Lucas of second kind
P = 2;
Q = 1;
b = [2 P];
a = [P Q];
LinearRecurrenceSequence('(2,1)-Lucas: Companion Pell (A002203)', 20, a, b)

function P = CreateP(a,b)
%CreateP Create the P polynomial
%   P polynomial is the numerator of the 
%   rational function that generate the sequeces
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
    P = fliplr(p);
end

function Q = CreateQ(a)
%CreateQ Create the Q polynomial
%   Q polynomial is the denominator of the rational 
%   function that generate the sequeces
    M = size(a,2);
    q = ones(1,M);
    for n = 2:M+1
        q(n) = -a(n-1);
    end
    Q = fliplr(q);
end

function [c,r] = GetCloseForm(P,Q)
%GetCloseForm Compute sequence close form
%   Compute close form base on generating function 
%   define as rational function P/Q
    Qr = fliplr(Q);
    r = roots(Qr)';
    if size(r,2)+1 ~= size(Qr,2)
        error('There is not trivial close form')
    end
    M = size(Q,2);
    dQ = polyder(Q);
    c = zeros(size(1,M-1));
    for k = 1:M-1
        c(k) = -r(k) * polyval(P, 1/r(k)) / polyval(dQ, 1/r(k));
    end
end

function f = EvalCloseForm(c, r, n, format)
%EvalCloseForm Compute a sequence value based its close form
%   Evaluate a close form base on coefficients(c) and roots(r)
    if size(c,2) ~= size(r,2)
        error('Coeff and root arrays are not same size');
    end
    M = size(r,2);
    f = 0;
    for k = 1:M
        f = f + c(k) * r(k)^n;
    end    
    if format == 'integer'
        f = int64(round(real(f)));
    elseif format == 'real'
        f = real(f);
    end
end

function LinearRecurrenceSequence(name, n, a, b)
%LinearRecurrenceSequence Compute a sequence value based its close form
%   Evaluate a close form base on coefficients(c) and roots(r)
    fprintf('Name: %s\n', name)
    fprintf('Degree: %d\n', size(a,2))
    fprintf('\n')

    fprintf('Recurrence coefficients')
    a
    fprintf('Initial conditions')
    b
    fprintf('\n')

    fprintf('Generating function\n')
    P = CreateP(a,b)
    Q = CreateQ(a)
    fprintf('\n')

    [c,r] = GetCloseForm(P,Q);
    fprintf('Partial fraction expantion\n')
    c
    r
    fprintf('\n')
    
    fprintf('Sequence\n')
    s = zeros(1,n);
    for i = 1:n
        s(i) = EvalCloseForm(c, r, i-1, 'integer');
    end
    disp(s);
    fprintf('------------------------')
    fprintf('\n')
end