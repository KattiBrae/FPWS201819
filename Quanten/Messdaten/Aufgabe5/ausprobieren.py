#zwischen zwei
if __name__=="__main__":
    a =[2,3,4,6,7,8,9,10,12,13,14,15]     #array
    #print (a[1])
    print (a)

    x=3
    b=[0,0,0,0]
    B=0
    while (x>2 and x<7):
        print (x, a[x])
        b[B]=a[x]
        x=x+1
        B=B+1

    #b=a[3]
    #a[3]=a[5]
    #a[5]=b


    print (a)
    print (b)

    x=3
    B=1
    while (x>2 and x<7):
        a[x]=b[len(b)-B]
        x=x+1
        B=B+1
    print(a)

    import numpy as np
    x, y = np.loadtxt('tabelle.txt', unpack = True , delimiter = ' ')
    print (y)
    c = 343.28
    l = c / y
    k=(2*np.pi)/l
    print (k)

    #for(i; i<a.length; i++):

    #if (a[1]>3):
    #    print("hallo")



    #x=a[0]
    #a[0]=x
    #print(x)
    #a[5]=7
    #for x in a:
    #    if x==4:
    #        print ("hallo")
    #    if x>4 and x<12:
    #        print ("darzwischen")

    #x = 2
    #while x in a:       #solange x in dem array enthalten ist gieb den wert aus und +1
    #    print (x)       #eine sortierung solange die werte nur 1 auseinander liegen
    #    x=x+1

    ## in java:
    #  int b=2;
    #  for (int x; x<.length; x++)
    #  if (b==a[x]){
    #    System.out.println(b)
    #    b++
    #   }

    #for x in a:
    #    print (x)

    ##In java:
    # for (int x; x<a.length;x++){
    # System.out.println(a[x]);
    # }




    #x=8
    #b=0
    #while x in a:           #solange der wert x in dem arry ist wird dieser Wert ausgegeben
    #    #print (a[b])
    #    #b=b+1
    #    print(x)
    #    x=x+1
