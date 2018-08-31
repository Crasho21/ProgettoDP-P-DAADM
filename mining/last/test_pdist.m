%test pdist2 vs pdist

% mfile = matfile('..\..\DatiUCI\mining\data2000Sparse.mat');
% Xred = X(500:700,1:1000);
% Xred=round(rand(1000,5000));

% X=10*rand(100,200);

tic
QT = pdist2(Xred, Xred);
toc

% tic
% QT1 = squareform(pdist(X,'euclidean'));
% toc


tic
QT2 = mypdist2(Xred);
toc
% tic
% [n,~] = size(X);
% nx = dot(X,X,2);
% N = repmat(nx,1,n);
% D = N+N'-2*(X*X');
% QT2 = sqrt(D);
% toc

%check
% sum(sum(QT-QT1))
[sum(sum(QT-QT2)) norm(QT-QT2,'fro')]