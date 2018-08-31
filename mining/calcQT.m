clear

tic

% mfile = matfile('D:\Universita\DataPrivacy\DatiUCI\dataReduced200.mat', 'Writable',true);
mfile = matfile('..\DatiUCI\dataPermGenLevel1APIGenLevel1.mat', 'Writable', true);



mfile.QT = pdist2(mfile.X,mfile.X);

toc