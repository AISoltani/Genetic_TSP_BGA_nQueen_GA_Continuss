function k=fitness(sol,nvar)
k=0;
for i=1:nvar-1
    for j=i+1:nvar
        if abs(i-j)==abs(sol(i)-sol(j))
            k=k+1;
        end
    end
end
end
