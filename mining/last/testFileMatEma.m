clear

%% 
tic

%Crea file con v7.3? Vediamo
a=3;
save '..\DatiUCI\anom\count\dataPermGenLevel2APIGenLevel3Reduced2000_count.mat' a -v7.3;

% file = fopen('D:\Universita\DataPrivacy\DatiUCI\dataReduced200.txt');
file = fopen('..\DatiUCI\anom\count\dataPermGenLevel2APIGenLevel3Reduced2000_sparse_count.txt');

% mfile = matfile('D:\Universita\DataPrivacy\DatiUCI\dataReduced200.mat', 'Writable',true);
mfile = matfile('..\DatiUCI\anom\count\dataPermGenLevel2APIGenLevel3Reduced2000_count.mat', 'Writable',true);

splitted = zeros(1, 370000);

tline = fgetl(file);
row = 1;

while ischar(tline)
%while ischar(tline)&&(row <= 50)
%     fprintf(num2str(row)+'\n');
    fprintf(num2str(row));
    
    splitted = str2num(tline);

    mfile.X(row, 1:size(splitted,2)) = splitted;

    tline = fgetl(file);
    row=row+1;
end
   
fclose(file);

% creazione Y, calcolo QT
X = mfile.X;
X = X(randperm(size(X,1)),:);
mfile.Y = X(:,1);
mfile.X = X(:,2:end);
% mfile.X = X;
% mfile.Y = Y;

clear('X');
clear('Y');

mfile.QT = pdist2(mfile.X,mfile.X);


% clear
% load('D:\Universita\DataPrivacy\DatiUCI\dataReduced.mat');
% save('D:\Universita\DataPrivacy\DatiUCI\dataReduced_73.mat', '-v7.3')

toc