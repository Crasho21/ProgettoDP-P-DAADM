%pulisce il workspace tranne la prima variabile
% vars=who
% clear(vars{2:end})

tic

a = '1 2 5 3 67 8 3 6 654 3 87 45';

splitted = str2num(a);

a=1;
save '..\DatiUCI\mining\data2000Sparse.mat' a -v7.3;
mfile = matfile('..\DatiUCI\mining\data2000Sparse.mat', 'Writable',true);

if(exist('X')==0)
    tic
    file = fopen('..\DatiUCI\data2000.txt');
%     numRows=14988;
    numRows=2000;

    X = sparse(numRows, 300000);
    Y = [];
    
    tline = fgetl(file);
    row = 1;

%     i = [];
%     j = [];
%     v = [];
    
    rowData = uint8(zeros(1, 300000));

    while ischar(tline) && row<=numRows
        %100rows => 844s
%         splitted = str2num(tline);
% 
% %         for k=2:length(splitted)
% %             i = [i, row];
% %             j = [j, splitted(k)];
%             
%             X(row*ones(length(splitted(2:end))), splitted(2:end)) = 1;
% %         end

%%%%%%%%%%%%%%%%%%%
        %100rows => 4.6s
%         rowData = zeros(1, 300000);
%         splitted = str2num(tline);
%         rowData(1, splitted(2:end)) = 1;
%         rowSparse = sparse(rowData);
%         X(row,:) = rowSparse;
%%%%%%%%%%%%%%%%%%%%%
        %100rows => 0.77s
        splitted = str2num(tline); 
        X(row, splitted(2:end)) = 1;
        
        %TODO leggere/costruire Y (col)
        Y(row, 1) = splitted(1);
        
%%%%%%%%%%%%%%%%%%%%
        tline = fgetl(file);
        row=row+1;
        
        
%         if row==100
            fprintf('%d', row);
%         end
    end
    toc
%     v = ones(length(i), 1);
%     X = sparse(i, j, v, 100,370000);
   
    fclose(file);
    
    mfile.X = X;
    mfile.Y = Y;
    
else
    fprintf('X esiste!\n');
    tic
    QT = pdist2(X, X);
    mfile.QT=QT;
    toc
end

toc