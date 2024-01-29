import unittest
from __init__ import comprova_signe

def comprova_signe(num: int)->int:
    class test (unittest.TestCase):
        def test(self):
         resultat = 0
    if(num>0):
            
                resultat = 1
   
    elif(num==0):
        resultat = 0
    
    else:
        resultat = -1
    return resultat




if __name__== '__main__':
       unittest.main() 
