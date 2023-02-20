function  mutpop=mutation(mutpop,pop,nvar,dis,nmut,npop)




for n=1:nmut


   i=randi([1 npop]); 
    
sol=pop(i).par;




j1=randi([1 nvar-1]);
j2=randi([j1+1 nvar]);



nj1=sol(j1);
nj2=sol(j2);


sol(j1)=nj2;
sol(j2)=nj1;


mutpop(n).par=sol;
mutpop(n).fit=fitness(sol,dis,nvar);


end



end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                   %
%                          www.matlabnet.ir                         %
%                   Free Download  matlab code and movie            %
%                          Shahab Poursafary                        %
%                                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
