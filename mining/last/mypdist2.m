function [ D ] = mypdist2( X )
%courtesy of https://github.com/maksimt/matlab_funcs/blob/master/mypdist.m
[n,~] = size(X);
nx = dot(X,X,2);
N = repmat(nx,1,n);
D = N+N'-2*(X*X');
D = sqrt(D);