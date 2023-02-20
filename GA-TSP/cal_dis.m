function dis = cal_dis( a )
dis=[];
for i=1:size(a,1)-1
    for j=i+1:size(a,1)
        dis(i,j)=sqrt((a(i,1)-a(j,1))^2+(a(i,2)-a(j,2))^2);
        dis(j,i)=dis(i,j);
    end  
end
end

