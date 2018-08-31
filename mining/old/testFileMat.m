% tic

% X = load('..\DatiUCI\dataReduced200.txt');
% 
% save('..\DatiUCI\dataReduced200.mat', 'X');

% toc

%% 
tic

file = fopen('..\DatiUCI\dataReduced3000.txt');

% X = sparse(250, 370000);

mfile = matfile('..\DatiUCI\dataReduced3000.mat', 'Writable', true);

splitted = zeros(1, 3026110);

tline = fgetl(file);
row = 1;
while ischar(tline)
%while ischar(tline)&&(row <= 50)
    
    fprintf(num2str(row));
    fprintf(' ');

    splitted = str2num(tline);

%     X(row, 1) = splitted(1);a
%     X(row*ones(length(splitted(2:end))), splitted(2:end)+1) = 1;

    mfile.X(row, 1:size(splitted,2)) = splitted;

    tline = fgetl(file);
    row=row+1;
end

fclose(file);

% load('..\DatiUCI\dataReduced200.mat');
% save('..\DatiUCI\dataReduced200_73.mat', '-v7.3')

tic