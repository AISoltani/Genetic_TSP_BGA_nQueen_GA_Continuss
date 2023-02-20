function crosspop=crossover(crosspop,pop,nvar,ncross)
f=[pop.cost];
f=1./f;
f=f./sum(f);
f=cumsum(f);
for n=1:2:ncross
i1=find(rand<=f,1,'first');
i2=find(rand<=f,1,'first');
p1=pop(i1).pos;
p2=pop(i2).pos;
j=randi([1 nvar-1]);
o1=[p1(1:j) p2(j+1:end)];
o2=[p2(1:j) p1(j+1:end)];
o1=unique([o1 randperm(nvar)],'stable');
o2=unique([o2 randperm(nvar)],'stable');
crosspop(n).pos=o1;
crosspop(n).cost=fitness(o1,nvar);
crosspop(n+1).pos=o2;
crosspop(n+1).cost=fitness(o2,nvar);
end
end