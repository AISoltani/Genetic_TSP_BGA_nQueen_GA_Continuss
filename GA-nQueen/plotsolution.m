function plotsolution(sol,nvar)
x=repmat((1:nvar)',1,nvar);
y=repmat((1:nvar),nvar,1);
figure(1)
plot(x,y,'bo')
xlim([0 nvar+1])
ylim([0 nvar+1])
hold on
plot(fliplr(sol),(1:nvar),'r*')
end