% Math 381 Project 1
% Variation 1: Change difficulty preference
clc; clear; close all

d = readtable('TimeMatrix.csv'); % read file with travel time between rivers
d = table2array(d); % converts table in file to array
% Convert d from minutes to hours
d = d / 60;

% Gets data for length of river to use for river travel time.
river_data = readtable('rivers_20.csv');
river_length = table2array(river_data(:, 3));  % given in miles

% Define the river weights using the negative of the square of the 
% difference from our target difficulty - rivers near our target difficulty
% are penalized less.
river_diffs = table2array(river_data(:, 2));

% For variation a change to 2, and for variation c change to 4
diff_targ = 3; 
w = 1 - (river_diffs - diff_targ).^2;

river_speed = 5; % miles per hour
r = river_length ./ river_speed; % hours

% total number of rivers
N = length(river_length);

% K has an upper bound of N since we visit every river at most once.
K = N;  % max number of steps

B = 2 * 8; % max number of hours

% Creates file where output conditions will be printed and stored
file = fopen('project1_var1.lp', 'wt');

% Set optimization function
fprintf(file, 'max: ');
fprintf(file, '%fy_%i', w(1), 1);
for ii = 2:N
    fprintf(file, ' + %fy_%i', w(ii), ii);
end
fprintf(file, ';\n');

% Set y_i to 1 if we travel to river i
for ii = 1:N
    fprintf(file, 'y_%i = ', ii);
    fprintf(file, 'x_%i_%i', ii, 1);
    for kk = 2:N
        fprintf(file, ' + x_%i_%i', ii, kk);
    end
    fprintf(file, ';\n');
end

% Sets z_k to 1 if we travel to a river at time k
for kk = 1:K
    fprintf(file, 'z_%i = ', kk);
    fprintf(file, 'x_%i_%i', 1, kk);
    for ii = 2:N
        fprintf(file, ' + x_%i_%i', ii, kk);
    end
    fprintf(file, ';\n');
end

% Tells us whether two rivers directly follow each other on our optimal
% route (if yes then value for e_i_j = 1).
for ii = 1:N
    for jj = 1:N
        if ii ~= jj
            for kk = 1:K-1
                fprintf(file, 'e_%i_%i >= x_%i_%i + x_%i_%i - 1;\n', ii, jj, ii, kk, jj, kk+1);
            end
        end
    end
end

% Ensure we go through steps in sequential order
for kk = 1:K-1
    fprintf(file, 'z_%i >= z_%i;\n', kk,kk+1);
end

% Ensure our trip does not exceed B hours
fprintf(file, '%fy_%i', r(1), 1);
for ii = 2:N
    fprintf(file, ' + %fy_%i', r(ii), ii);
end
for ii = 1:N
    for jj = 1:N
        if (ii ~= jj)
            fprintf(file, ' + %fe_%i_%i', d(ii, jj), ii, jj);
        end
    end
end
fprintf(file, ' <= %f;\n', B);

% Define variables as binary
fprintf(file, 'bin ');
fprintf(file, 'x_%i_%i', 1, 1);
for ii = 1:N
    for kk = 1:K
        if (ii ~= 1 && kk ~= 1)
            fprintf(file, ', x_%i_%i', ii, kk);
        end
    end
end
for ii = 1:N
    for jj = 1:N
        if (ii ~= jj)
            fprintf(file, ', e_%i_%i', ii, jj);
        end
    end
end
for ii = 1:N
    fprintf(file, ', y_%i', ii);
end
for kk = 1:K
    fprintf(file, ', z_%i', kk);
end
fprintf(file, ';');