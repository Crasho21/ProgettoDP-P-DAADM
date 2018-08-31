clear
%% Random Seed
seed = 13;
randn('seed',seed);

%% Load Data
% mfile = matfile('D:\Universita\DataPrivacy\DatiAnon\dataPermGenLevel0APIGenLevel1Reduced2000_nocount.mat');
mfile = matfile('..\..\DatiUCI\mining\dataAllSparse.mat');

Y = mfile.Y;
    
%% Training
n = size(mfile.X,1);
d = size(mfile.X,2);

%permutazione di tutto il dataset
indexN = randperm(n)';
% nt = round(0.2 * n);    % 20% test
% nlv = n-nt;     %60 training + 20 valid (?)
nlv = round(0.8 * n);

tic
err_best = +Inf;
QT = mfile.QT;
% QT = mypdist2(mfile.X);

% alpha = [];
% index = [];

% for gamma = logspace(-6,4,30)
for gamma = logspace(-6,-4,10)
    Q = exp(-gamma*QT);
%     for lambda = logspace(-6,4,30)
    for lambda = logspace(-6,-4,10)
        err = 0;
%         tic
%         for k = 1:30
        for k = 1:10    % Montecarlo
            %permutazione del blocco train/val
            %passando per indexN
            i = randperm(nlv)';
            nl = round(.7*nlv);
            il = indexN(i(1:nl));
            iv = indexN(i(nl+1:end));
                    
            %training modello
            fm = Y(il) == 1; fp = Y(il) == 0;
            ilp = [il(fm); il(fp)];
            YP = [-ones(sum(fm),1); ones(sum(fp),1)];
            alpha = (Q(ilp,ilp)+lambda*eye(length(ilp)))\YP;
            index = ilp;
            
            %validation
            tmp = Q(iv, index) * alpha;
            tmp(tmp>=0) = 0;
            tmp(tmp<0) = 1;
            YF = tmp;
            
            %calcolo errore
            YF = mode(YF,2);
            err = err + mean(YF ~= Y(iv));
        end
%         toc
        if (err_best > err)
            err_best = err;
            gamma_best = gamma;
            lambda_best = lambda;
        end
        fprintf('%e %e %e %e\n', gamma, lambda, err_best, err);
    end
end
% toc

%% Training finale e test
% tic
gamma = gamma_best;
lambda = lambda_best;

[gamma_best lambda_best]

% alpha = [];
% index=[];
Q = exp(-gamma*QT);
% nl = round(.7*n);
il = indexN(1:nlv);
it = indexN(nlv+1:n); %indici test

fm = Y(il) == 1; fp = Y(il) == 0;
ilp = [il(fm); il(fp)];
YP = [-ones(sum(fm),1); ones(sum(fp),1)];
alpha = (Q(ilp,ilp)+lambda*eye(length(ilp)))\YP;
index = ilp;

tmp = Q(it, index) * alpha;
tmp(tmp>=0) = 0;
tmp(tmp<0) = 1;

%K = [tmp, Y((size(Y,1)-size(tmp,1)+1):end)];
K = [tmp, Y(it)];
full(K);
fprintf(['Valori uguali: ' , num2str(sum(K(:,1)==K(:,2))) , ' su ' , num2str(size(K,1)) , ' -> ' , num2str(((sum(K(:,1)==K(:,2)))/size(K,1))*100), '%%\n'])
toc
