clear
tic

% mfile = matfile('D:\Universita\DataPrivacy\DatiUCI\dataReduced2000.mat', 'Writable',true);
mfile = matfile('..\DatiUCI\dataPermGenLevel1APIGenLevel1_count.mat', 'Writable',true);

X = mfile.X;
X = X(randperm(size(X,1)),:);
mfile.Y = X(:,1);
mfile.X = X(:,2:end);
% mfile.X = X;
% mfile.Y = Y;

clear('X');
clear('Y');

mfile.QT = pdist2(mfile.X,mfile.X);

toc
% clear