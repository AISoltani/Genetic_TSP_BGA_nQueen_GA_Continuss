clc
clear
close all
format shortG
%% parameters setting
nvar=input(' Number of Queen = ');% number of variable
npop=100;% number of population
maxiter=5000; % max of iteration
pc=0.7;% percent of cross over
ncross=2*round(npop*pc/2); % number of cross over
pm=.29; % percent of mutation
nmut=round(npop*pm);% number of mutation
nrep=npop-ncross-nmut;% number of reproduction
%% inialization
tic
empty.pos=[]; % position
empty.cost=[]; % cost
pop=repmat(empty,npop,1);% population matrix
for i=1:npop
    pop(i).pos=randperm(nvar);
    pop(i).cost=fitness(pop(i).pos,nvar);
end
[value index]=sort([pop.cost]);
%% main loop
best=1000*ones(maxiter,1);
AVR=1000*ones(maxiter,1);
%Bad=realmax*ones(maxiter,1);
iter=0;
while value(1)>0
    iter=iter+1;
    % cross
    crosspop=repmat(empty,ncross,1);
    crosspop=crossover(crosspop,pop,nvar,ncross);
    % mutation
    mutpop=repmat(empty,nmut,1);
    mutpop=mutation(mutpop,pop,nvar,nmut);
    % reproduction
    reppop=pop(index(1:nrep));
    % merged
    [pop]=[reppop;
        crosspop;
        mutpop];
    [value index]=sort([pop.cost]);
    %pop=pop(index(1:npop));
    best(iter)=value(1);
    AVR(iter)=mean([pop.cost]);
    disp([ 'Iter = ' num2str(iter)  ' BEST = ' num2str(value(1))])
end
%% results
figure(1)
plotsolution(pop(index(1)).pos,nvar);
disp('===========================================')
disp([ 'Time = ' num2str(toc)])
disp('===========================================')
disp([ 'Best fitness = ' num2str(value(1))])
disp('===========================================')
disp([ 'Best Solution = ' num2str(pop(index(1)).pos)])
figure(2)
plot(best(1:iter),'g','LineWidth',2)
hold on
plot(AVR(1:iter),'m','LineWidth',2)
legend('BEST','MEAN')
xlabel('Iteration')
ylabel('Fitness')
title(' GA for TSP ')