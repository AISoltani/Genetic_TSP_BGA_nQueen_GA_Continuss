function crosspop=crossovertour(crosspop,pop,nvar,ncross)
npop=length(pop);
ntour=10;
for n=1:2:ncross
 g=randperm(npop);   
 g=g(1:ntour);  
 tourpop=pop(g);
 [~,index]=sort([tourpop.cost]);
p1=tourpop(index(1)).pos;
p2=tourpop(index(2)).pos;
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