#!/usr/bin/env python
# coding: utf-8

# ## 1.1 Simple echange ##

# In[4]:


a = 5
b = 8
a = 8


# In[5]:


a


# ## 1.2 Le carré ##

# In[8]:


def Carre(n:int):
    return n * n

Carre(10)


# ## 1.3 la condition ##

# In[15]:


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


# ## 1.4 Le produit ##

# In[26]:


def calcProduct(n1: int, n2 :int) : 
    i = ""
    if(n1 * n2) > 0 :
        i = "positif"
    else:
        i = "negatif"
    print(i)


# In[27]:


calcProduct(2, 5)


# ## 1.5 Calcul ##

# In[54]:


def calcul(n:int):
    i = 0
    while(i <= n):
        i += 1
        if(i <= 10):
            print(n+i)
        else:
            break;


# In[55]:


calcul(17)


# ## 1.6 La somme ##

# In[75]:


def additivte(n):
    i = 0
    while(i <= n):
        i+= 1
        if(i == 5): 
            print(i+n)
            break
        else:
             i+= 1


# In[76]:


additivte(10)




## 29/03/2021 ##
## Target Somme ##

def getkeyNumbers(array, tatgetSum){
// on parcours le tableau via une boucle for
for(i=0; i<=array.length; i++){
    
  for(y=i+1; i<= array.length; y++){
      if
      
  }
    
  ## we test each conbinaison
  var a = array[i];
  var b = array[i-1];
  var c = array[i+1];
    
  # we get sum of combinaison   
  var sumAB = a + b;
  var somAC = a + c;
  var somCB = c +b
    
  # we test the equation
  if(sumAB == tatgetSum ):
    # we return the result
    return [a, b];
 endif

  elif(sumAC == TargetSum) :

  return [a, c];

 endif;

elif(sumBC == TargetSum) :

 return [b, c];

endif;

else:
    return "0 number has been found";
}


}












