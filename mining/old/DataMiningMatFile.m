%% Random Seed
seed = 13;
randn('seed',seed);

%% Load Data

%pulisce il workspace tranne la prima variabile


% tic
% if(exist('X')==0)
% 
% %     file = fopen('D:\Universita\DataPrivacy\DatiUCI\data250.txt');
%     file = fopen('..\DatiUCI\data100.txt');
% 
%     X = sparse(250, 370000);
%     
%     tline = fgetl(file);
%     row = 1;
%     while ischar(tline)
%     %while ischar(tline)&&(row <= 50)
%     
%         fprintf(num2str(row));
%                
%         splitted = str2num(tline);
%         
%         X(row, 1) = splitted(1);
%         X(row*ones(length(splitted(2:end))), splitted(2:end)+1) = 1;
% 
%         tline = fgetl(file);
%         row=row+1;
%     end
%    
%     fclose(file);
%     
%     X = X(randperm(size(X,1)),:);
%     Y = [X(:,1)];
%     Y(Y==0)=2;
%     X = [X(:,2:end)];
%     
% else
%     vars=who;
%     [~,p] = ismember({'X','Y', 'matfile'},vars);
%     vars(p) = '';
%     clear(vars{:});
%     fprintf('X esiste!\n');
% end
% toc
%%
n = size(mfile.X,1);
d = size(mfile.X,2);
c = 2;

%% Algoritmo
% tic

err_best = +Inf;
QT = pdist2(mfile.X,mfile.X); % x * x'
for gamma = logspace(-6,4,30)
    Q = exp(-gamma*QT);
    for lambda = logspace(-6,4,30)
        err = 0;
        for k = 1:30
            i = randperm(n)';
            nl = round(.7*n);
            il = i(1:nl);
            iv = i(nl+1:end);
            ALPHA = cell(c*(c-1)/2,1); 
            INDEX = cell(c*(c-1)/2,1);
            im = 0;
            for i = 1:c
                for j = i+1:c
                	im = im + 1;
                    fm = Y(il) == i; fp = Y(il) == j;
                    ilp = [il(fm); il(fp)];
                    YP = [-ones(sum(fm),1); ones(sum(fp),1)];
                    alpha = (Q(ilp,ilp)+lambda*eye(length(ilp)))\YP;
                    ALPHA{im} = alpha; 
                    INDEX{im} = ilp;
                end
            end
            YF = [];
            im = 0;
            for i = 1:c
                for j = i+1:c
                	im = im + 1;
                    tmp = Q(iv,INDEX{im}) * ALPHA{im};
                    tmp(tmp>0) = j;
                    tmp(tmp<=0) = i;
                    YF = [YF, tmp]; %#ok<AGROW>
                end
            end
            YF = mode(YF,2);
            err = err + mean(YF ~= Y(iv));
        end
        if (err_best > err)
            err_best = err;
            gamma_best = gamma;
            lambda_best = lambda;
        end
        fprintf('%e %e %e %e\n',gamma,lambda,err_best,err);
    end
end

%%
gamma = gamma_best;
lambda = lambda_best;

ALPHA = cell(c*(c-1)/2,1); 
INDEX = cell(c*(c-1)/2,1);
im = 0;
tic
Q = exp(-gamma*pdist2(mfile.X,mfile.X));
toc
nl = round(.7*n);
il = (1:nl)';
iv = (nl+1:n)';

for i = 1:c
    for j = i+1:c
        im = im + 1;
        fm = Y(il) == i; fp = Y(il) == j;
        ilp = [il(fm); il(fp)];
        YP = [-ones(sum(fm),1); ones(sum(fp),1)];
        alpha = (Q(ilp,ilp)+lambda*eye(length(ilp)))\YP;
        ALPHA{im} = alpha; 
        INDEX{im} = ilp;
    end
end

tmp = Q(iv,INDEX{im}) * ALPHA{im};
tmp(tmp>0) = 2;
tmp(tmp<=0) = 1;

K = [tmp,Y((size(Y,1)-size(tmp,1)+1):end)];
full(K);
sum(K(:,1)==K(:,2))

% toc
