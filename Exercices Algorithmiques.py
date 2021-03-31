## 1.1 Simple echange ##

a = 5
b = 8
a = 8

a

## 1.2 Le carré ##

def Carre(n:int):
    return n * n

Carre(10)

## 1.3 la condition ##

def checkNumber(n:int):
    v = ""
    if n > 0:
        v = "postif"
    elif n < 0:
        v = "negatif"
    else:
        v = " is null"
    print(v)

checkNumber(str(n))

## 1.4 Le produit ##

def calcProduct(n1: int, n2 :int) : 
    i = ""
    if(n1 * n2) > 0 :
        i = "positif"
    else:
        i = "negatif"
    print(i)

calcProduct(2, 5)

## 1.5 Calcul ##

def calcul(n:int):
    i = 0
    while(i <= n):
        i += 1
        if(i <= 10):
            print(n+i)
        else:
            break;

calcul(17)

## 1.6 La somme ##

def additivte(n):
    i = 0
    while(i <= n):
        i+= 1
        if(i == 5): 
            print(i+n)
            break
        else:
             i+= 1

 additivte(10)

# Target Somme 

# Distance of Levenshtein

def getDistance(a, b) {
        var n = a.length, m = b.length, matrice = [];
        for(var i=-1; i < n; i++) {
                matrice[i]=[];
                matrice[i][-1]=i+1;
        }
        for(var j=-1; j < m; j++) {
                matrice[-1][j]=j+1;
        }
        for(var i=0; i < n; i++) {
                for(var j=0; j < m; j++) {
                        var cout = (a.charAt(i) == b.charAt(j))? 0 : 1;
                        matrice[i][j] = minimum(1+matrice[i][j-1], 1+matrice[i-1][j], cout+matrice[i-1][j-1]);
                }
        }
        return matrice[n-1][m-1];
}
// la fonction minimum() est à définir !

   



    

