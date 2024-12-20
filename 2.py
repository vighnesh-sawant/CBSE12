#Program to read content of file and display total number of vowels, consonants, lowercase and uppercase characters
f=open("./Text/text.txt","r")
contents=f.read()
vowels=["a","e","i","o","u"]
c=0
v=0
l=0
u=0
o=0
words=contents.split()
for i in contents:
  for ch in i:
    if(ch.isalpha()):
        if(ch.lower() in vowels):
           v+=1
        else:
            c+=1
        if(ch.islower()):
            l+=1
        else:
           u+=1
    elif ch!=" " or ch!="\n":
        o+=1
print("No of vowels:",v)
print("No of consonants:",c)
print("No of lowercase letters:",l)
print("No of uppercase letters:",u)
print("No of other characters:",o)



