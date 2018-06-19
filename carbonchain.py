
import turtle

def counts(Sp3, Sp2, Sp1, H, molecule, n):
    count = 0
    i = 0
    hCount = 0

    while i != (len(molecule)):
            if Sp3 == molecule[i:i+3]:
                count +=1
                n.append("CH3")
                i+=3
    
            elif Sp2 == molecule[i:i+3]:
                count+=1
                n.append("CH2")
                i+=3
            elif Sp1 == molecule[i:i+2]: 
                count+=1
                n.append("CH")
                i+=2
            elif H[0] == molecule[i]:
                hCount+=1
                n.append(H[0])
                i+=1
            elif H[1] == molecule[i:i+2]:
                hCount+=1
                n.append(H[1])
                i+=2
            elif H[2] == molecule[i:i+2]:
                hCount+=1
                n.append(H[2])
                i+=2
            elif H[3] == molecule[i]:
                hCount+=1
                n.append(H[3])
                i+=1
            else:
                i+=1
    return n, count, hCount

def carbonChain(total, n, hCount):

    position = [ ]

    wn = turtle.Screen()
    turtle.hideturtle()
    turtle.pendown()
    alex = turtle.Turtle()
    alex.hideturtle()
    alex.penup()
    alex.setpos(-300, 1)
    alex.pendown()
    alex.left(-330)

    l = 1
    r = -1
    s = 1
    x = 2
    i = 0
    
    while i != len(n):
        if n[i] == "Br": 
            if i%4 == 0:
                alex.right(60)
                alex.forward(50)
                i+=1
                alex.penup()
                alex.forward(10)
                alex.write("Br", align="left")
                alex.backward(60)
                alex.pendown()
                alex.left(60)
            else:
                if i%3 == 0 and i%6 !=0:
                    alex.right(300*r)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Br", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300*r)
                if i%6 == 0 and i%4 !=0:
                    alex.right(60)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Br", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(60)
                else:
                    alex.right(300)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Br", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300)                    
                r = r*(-1)
        if n[i] == "F": # FLUORINE Substituents
            if i%4 == 0:
                alex.right(60)
                alex.forward(50)
                i+=1
                alex.penup()
                alex.forward(10)
                alex.write("F", align="left")
                alex.backward(60)
                alex.pendown()
                alex.left(60)
            else:
                if i%3 == 0 and i%6 !=0:
                    alex.right(300*r)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("F", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300*r)
                if i%6 == 0 and i%4 !=0:
                    alex.right(60)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("F", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(60)
                else:
                    alex.right(300)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("F", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300)                    
                r = r*(-1)
        if n[i] == "Cl": # Clorine Substituents
            if i%4 == 0:
                alex.right(60)
                alex.forward(50)
                i+=1
                alex.penup()
                alex.forward(10)
                alex.write("Cl", align="left")
                alex.backward(60)
                alex.pendown()
                alex.left(60)
            else:
                if i%3 == 0 and i%6 !=0:
                    alex.right(300*r)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Cl", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300*r)
                if i%6 == 0 and i%4 !=0:
                    alex.right(60)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Cl", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(60)
                else:
                    alex.right(300)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("Cl", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300)                    
                r = r*(-1)

        if n[i] == "I": # Iodine Substituents
            if i%4 == 0:
                alex.right(60)
                alex.forward(50)
                i+=1
                alex.penup()
                alex.forward(10)
                alex.write("I", align="left")
                alex.backward(60)
                alex.pendown()
                alex.left(60)
            else:            
                if i%3 == 0:
                    alex.right(300*r)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("I", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300*r)
                if i%6 == 0 and i%4 !=0:
                    alex.right(60)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("I", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(60)
                else:
                    alex.right(300*r)
                    alex.forward(50)
                    i+=1
                    alex.penup()
                    alex.forward(10)
                    alex.write("I", align="left")
                    alex.backward(60)
                    alex.pendown()
                    alex.left(300*r)                    
                r = r*(-1)

            
        elif n[i] == "CH3" or "CH2" or "CH":
            if i == 0:
                alex.penup()
            alex.right(60*l)
            alex.forward(50)
            l = l*(-1)
            i+=1
            if i>=1:
                alex.pendown()
                       

        else:
            return None
        
def name(names, total):
    for i in range(len(names)):
        if i == total:
            structure = (names[i-1])
    return structure
            
def halogenP(n, H, fullH):
    aLoc = []
    order = []
    
    
    s = -2    
    for i in range(len(n)-1):
        if i%2 ==0:
         s+=1
        for j in range(len(fullH)):
            if n[i] == H[j]:
                if n[i] =="Br":
                    if i == 2:
                        aLoc.append(i)
                    elif i%2== 0 and i>2:
                        aLoc.append(i-s)
                    elif i%2==1 and i>2:
                        aLoc.append(i-s)
                    aLoc.append("-bromo")
    a = -2    
    for l in range(len(n)-1):
        if l%2 ==0:
         a+=1
        for k in range(len(fullH)):
            if n[l] == H[k]:
                if n[l] =="Cl":
                    if l == 2:
                        aLoc.append(l)
                    elif l%2== 0 and l>2:
                        aLoc.append(l-a)
                    elif l%2==1 and l>2:
                        aLoc.append(l-a)
                    aLoc.append("-chloro")
    p = -2    
    for t in range(len(n)-1):
        if t%2 ==0:
         p+=1
        for z in range(len(fullH)):
            if n[t] == H[z]:
                if n[t] =="F":
                    if t == 2:
                        aLoc.append(t)
                    elif t%2== 0 and t>2:
                        aLoc.append(t-p)
                    elif t%2==1 and t>2:
                        aLoc.append(t-p)
                    aLoc.append("-fluoro")   
                
    e = -2
    for q in range(len(n)-1):
        if q%2 ==0:
         e+=1
        for w in range(len(fullH)):
            if n[q] == H[w]:
                if n[q] =="I":
                    if q == 2:
                        aLoc.append(q)
                    elif q%2== 0 and q>2:
                        aLoc.append(q-e)
                    elif q%2==1 and q>2:
                        aLoc.append(q-e)
                    aLoc.append("-iodo")
    return aLoc

def sideChain(position, side):
       return

def main():

    Sp3 = "CH3"
    Sp2= "CH2"
    Sp1 = "CH"
    H= ["F", "Cl", "Br", "I"]
    fullH = ["fluoro", "chloro", "bromo", "iodo"]

    n = []
    total = 0

    names = ["methane", "ethane", "propane", "butane", "pentane", "hexane", "heptane", "octane", "nonane", "decane"]


    print()
    print("Hi welcome to Carbon Chain. This will convert carbon chains into line molecules.")
    print("1: Input your own organic molecule")
    print("2: CH3CHClCHFCH3")
    print("3: CH3CH2CH2CH2CH2CH3")
    print("4: CH3CHBrCH2CHBrCH3")
    print()
    
    done = False
    while not done:
        config = eval(input("Choose your number: "))
            
        if config == 4:
            molecule = "CH3CHBrCH2CHBrCH3"
            n, total, hCount= counts(Sp3, Sp2, Sp1, H, molecule, n)
            position = carbonChain(total, n, hCount)
            structure = name(names, total)
            num= halogenP(n, H, fullH)
            done = True
            
        if config == 3:
            molecule = "CH3CH2CH2CH2CH2CH3"
            n, total, hCount= counts(Sp3, Sp2, Sp1, H, molecule, n)
            position = carbonChain(total, n, hCount)
            structure = name(names, total)
            num= halogenP(n, H, fullH)
            done = True
        
        if config == 2:
            molecule = "CH3CHClCHFCH3"
            n, total, hCount= counts(Sp3, Sp2, Sp1, H, molecule, n)
            position = carbonChain(total, n, hCount)
            structure = name(names, total)
            num= halogenP(n, H, fullH)
            done = True
            
        if config == 1:
            molecule = input("Type in a molecule: ")
            n, total, hCount= counts(Sp3, Sp2, Sp1, H, molecule, n)
            position = carbonChain(total, n, hCount)
            structure = name(names, total)
            num= halogenP(n, H, fullH)
            done = True
            
            
        elif config > 6:
            print("Please enter a number between 1-5")
        elif config < 1:
            print("Please enter a number between 1-5")
        elif config != 1 and config != 2 and config  != 3 and config != 4:
            print("Please enter a number between 1-5")
        else:
            done = True

    print()
    print(num,"-", structure, sep="")




main()
input()