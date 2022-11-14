'''pflfybt 2'''

def read():
    f = open("stdin.txt", "r")
    mas = []
    for i in f:
        mas.append(int(i))
    f.close()
    return mas

def write(P):
    f = open("stdout.txt", "w")
    f.write(str(P))
    f.close()
    
mas = read()
##mas = mas.spit()
print (mas)
P = 0
if mas[0]==1 and mas[1]==1:
    P = 1

write(P)