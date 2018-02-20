%pulisce il workspace tranne la prima variabile
% vars=who
% clear(vars{2:end})

tic

a = '1 2 5 3 67 8 3 6 654 3 87 45';

splitted = str2num(a);

if(exist('X')==0)

    file = fopen('..\DatiUCI\data.txt');

    X = sparse(5000, 300000);
    
    tline = fgetl(file);
    row = 1;

    i = [];
    j = [];
    v = [];

    while ischar(tline) && row<=10
        splitted = str2num(tline);

%         for k=2:length(splitted)
%             i = [i, row];
%             j = [j, splitted(k)];
            
            X(row*ones(length(splitted(2:end))), splitted(2:end)) = 1;
%         end

        tline = fgetl(file);
        row=row+1;
    end

%     v = ones(length(i), 1);

%     X = sparse(i, j, v, 100,370000);
   
    fclose(file);
    
else
    fprintf('X esiste!\n');
end

toc