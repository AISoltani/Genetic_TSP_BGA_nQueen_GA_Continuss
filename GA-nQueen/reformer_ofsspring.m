function newo=reformer_ofsspring(o)
newo=[];
while ~isempty(o)
   [newo]=[newo o(1)];
   [h]=find(o==o(1));
   o(h)=[];
end
end