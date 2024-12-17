#READ A TEXT FILE LINE BY LINE AND DISPLAY EACH WORD SEPERATED BY A #
f=open("./Text/text.txt")
l=f.readlines()
for i in l:
    w=i.split()
    for x in w:
        print(x+"#",end="")