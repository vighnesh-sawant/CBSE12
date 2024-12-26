#Remove all the lines that contain the character `a' in a file and  write it to another file. 
# Wording is a little ambigious ):
f=open("./Text/text.txt","r")
f1=open("./Text/text1.txt","w")
for line in f:
    if "a" not in line:
        f1.write(line)
print("Sucessful")