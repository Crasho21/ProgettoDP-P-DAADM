clear
clc

%8/11/17 - Se il prob non � lineare?

%% seed
%blocchiamo seed del rand
seed = 23;  %regola empirica, partire da num primi fa buone distr
randn('seed', seed);

%% dati

X = load('../DatiUCI/dataReduced500.txt');
Y = X(:,1);
Y(Y==0) = -1;
[n, d] = size(X);

index = randperm(n);
nl = round(0.7 * n);    % # dati per learning
il = index(1:nl);   %indici dati learning
iv = index(nl+1:end);   %indici dati valid

Xtest = X(iv, :);
X = X(il, :);
Ytest = Y(iv, :);
Y = Y(il, :);
[n, d] = size(X);

%Per costruzione non esiste un separatore lineare per questo dataset
% => aumento espressivit� aumentando il grado del perceptr
% == presi i dati, creo sinteticamente nuove feature

%% Osservazione dei dati

%% preprocessing

%% eventuale conversioni di var categoriche

%% normalizzazione

%% plot post normal
% figure, hold on, box on, grid on
% plot(X(Y>0,1), X(Y>0,2), 'ob', 'linewidth', 2);
% plot(X(Y<0,1), X(Y<0,2), 'or', 'linewidth', 2);


%% aggiunta di dati
% X = [X, X(:,1).^2, X(:,2).^2, X(:,1).*X(:,2)];
% X = [X, X(:,2).^2, X(:,1).*X(:,2)];
% X = [X, X(:,1).^2];
% X = [X, X(:,1).*X(:,2)];
%Tra queste la pi� interessante � l'ultima. 
% Indica una relazione tra le due var 


%% Applicazione alg

%Perceptrone
seed=11;
randn('seed' , seed);
%uno per feature
w = randn(d, 1);    %gauss, media 0, var 1
%sfasamento (unico)
b = randn(1, 1);

%num errori
err = sum((X*w + b) .* Y <= 0);  

i = 1;
j = 0; %num iterazioni
while (err > 0)
    j=j+1;
    %HO classificato scorrettamente il sample i-esimo?
    f = X(i,:)*w + b;
    if(f*Y(i) <= 0)
        %Aggiorno pesi
        w = w + Y(i)*X(i,:)';
        b = b + Y(i);
        
        %ricalcolo err
        err = sum((X*w + b) .* Y <= 0);
%         plot(x1, x2, 'm')
        
%         pause
    end
    
    i = i+1;
    %Se finisco i sample riparto
    if(i>n) i=1; end
    
    fprintf('j: %04d, err: %3d \n', j, err);
end


% Visualizziamo il separatore
%y = w1x1 + w2x2 + w3x1^2 + w4x2^2 + w5x1x2 + b = 0
% per trovare intersezione separatore con piano
%cartesiano

%Sol analitica difficile da trovare
%allora 
%   lancio punti
%   coloro in base a se � + o -
%   identifico cos� dove passa il piano

% %X, Y predette
% XP = rand(50000, d);
% % XP = [XP, XP(:,1).^2, XP(:,2).^2, XP(:,1).*XP(:,2)];
% % XP = [XP, XP(:,2).^2, XP(:,1).*XP(:,2)];
% % XP = [XP, XP(:,1).^2, XP(:,1).*XP(:,2)];
% XP = [XP, XP(:,1).^2];
% % XP = [XP, XP(:,1).*XP(:,2)];

% YP = XP*w + b;

% plot(XP(YP>0,1), XP(YP>0,2), '.b', 'markersize', 1);
% plot(XP(YP<0,1), XP(YP<0,2), '.r', 'markersize', 1);


% Plotto
% Poi modifico X eliminando qualche feature per vedere come si comporta il
% perceptrone => "Feature selection"
%Riesco a ridurre a X = [X, X(:,1).^2]
% Come minimo avr�

%Posso ancora farlo?
%X = sqrt(X(:,1))
% La speranza � di abbassare a qualcosa di lineare i punti.
% Ma non funziona in questo caso.
%1h50min

% Come decido quali feature eliminare?
% - Forza bruta
% Poi posso ricercare altre feature che possono essere interessanti, 
%   e hanno un senso per il problema, in modo da meglio rappresentare il
%   problema che l'alg va a risolvere. Questo viene facile per algoritmi
%   pi� semplici come questo, ma gi� non lo si riesce a fare con ad es. reti
%   neurali

%test
Yclass = Xtest*w + b;

results = [Yclass, Ytest];
