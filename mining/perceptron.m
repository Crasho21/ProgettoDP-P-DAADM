% clear
% clc

%8/11/17 - Se il prob non � lineare?

%% seed
%blocchiamo seed del rand
seed = 23;  %regola empirica, partire da num primi fa buone distr
randn('seed', seed);

%% dati
%pulizia workspace tranne X, Y
% vars=who;
% [~,p] = ismember({'X','Y'},vars);
% vars(p) = '';
% clear(vars{:});

% X = load('../DatiUCI/dataReduced2000.txt');
% Y = X(:,1);

[n, d] = size(X);

tic

index = randperm(n);
nl = round(0.7 * n);    % # dati per learning
il = index(1:nl);       %indici dati learning
iv = index(nl+1:end);   %indici dati valid

Yperc=Y;
Yperc(Y==0) = -1;

Xtest = X(iv, :);
Xlearn = X(il, :);
Ytest = Yperc(iv, :);
Ylearn = Yperc(il, :);
[n, d] = size(Xlearn);

%% Applicazione alg

%Perceptrone
seed=11;
randn('seed' , seed);
%uno per feature
w = randn(d, 1);    %gauss, media 0, var 1
%sfasamento (unico)
b = randn(1, 1);

%num errori
err = sum((Xlearn*w + b) .* Ylearn <= 0);  

i = 1;
j = 0; %num iterazioni

err_min = +Inf;

while (err > 0)
    j=j+1;
    %HO classificato scorrettamente il sample i-esimo?
    f = Xlearn(i,:)*w + b;
    if(f*Ylearn(i) <= 0)
        %Aggiorno pesi
        w = w + Ylearn(i)*Xlearn(i,:)';
        b = b + Ylearn(i);
        
        %ricalcolo err
        err = sum((Xlearn*w + b) .* Ylearn <= 0);
%         plot(x1, x2, 'm')
        
%         pause
    end
    
    i = i+1;
    %Se finisco i sample riparto
    if(i>n) i=1; end
    
    fprintf('j: %04d, err: %3d - ', j, err);
    if(mod(j, 1000) == 0) fprintf('\n'); end
    
    if(err<err_min) err_min=err; end
end

toc

%% test
Yclass = Xtest*w + b;

results = [Yclass, Ytest];
