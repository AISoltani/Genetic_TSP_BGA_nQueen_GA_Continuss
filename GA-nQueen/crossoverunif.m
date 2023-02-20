function crosspop=crossoverunif(crosspop,pop,nvar,ncross)
f=[pop.cost];
f=1./f;
f=f./sum(f);
f=cumsum(f);
for n=1:2:ncross
i1=find(rand<=f,1,'first');
i2=find(rand<=f,1,'first');
p1=pop(i1).pos;
p2=pop(i2).pos;
mask=randi([0 1],1,nvar);
o1=zeros(1,nvar);
o2=zeros(1,nvar);
for i=1:nvar
    if mask(i)==1
        o1(i)=p1(i);
        o2(i)=p2(i);
    else
        o1(i)=p2(i);
        o2(i)=p1(i);
    end
end
o1=unique([o1 randperm(nvar)],'stable');
o2=unique([o2 randperm(nvar)],'stable');
crosspop(n).pos=o1;
crosspop(n).cost=fitness(o1,nvar);
crosspop(n+1).pos=o2;
crosspop(n+1).cost=fitness(o2,nvar);
end
end