function mutpop=mutation(mutpop,pop,nvar,nmut)
npop=length(pop);
for n=1:nmut
i=randi([1 npop]);
p=pop(i).pos;
j1=randi([1 nvar-1]);
j2=randi([j1+1 nvar]);
nj1=p(j1);
nj2=p(j2);
p(j1)=nj2;
p(j2)=nj1;
mutpop(n).pos=p;
mutpop(n).cost=fitness(p,nvar);
end
end
