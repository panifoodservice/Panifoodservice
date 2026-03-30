l="\n"
#a=int(input("1️⃣ number"))
#b=int(input("2️⃣ number"))
c=f"{l}{l}codes: {l}{l} q1=add,substract,multiply,divide {l}{l} q2=(a+b)²{l}{l} q3=(a-b)²{l}{l} q4=divide{l} {l} q5=square {l}{l} q6= (a+b)²{l}{l}"
print (c)
a="1️⃣ value of (a)::-  "
b="2️⃣ value of (b)::-  "
d="👉 RESULT:-"
e=f"{a}{l}{l}{l}"
f=f"{b}{l}{l}{l}"
g=f"{l}{l}"
h="sorry type number,s"
i="don't add simbol,s"
def q1():
        try:
            n1=input(f"add (+),subtract (-),multiply(*),divide(/) use this simbols and sum karne ke liye iss tarh number de jaisa braket ke    andar dikhaya gaya hai (12+21+23+24) iss tarh jitna jodna   hai waise numbers de{l}{l}")
            #n2=int(input(f))
            #n3=n1+n2
            #print(f"{l}{l}{n1}+{n2}")
            print (d,eval(n1))
        except ValueError :
            print (g,h)
        except SyntaxError :
            print (n1,"write prperly .remove  symbols in the last")
        except NameError:
            print ("name error")
def q2():
        try:
            print(f"q2:-(a+b)²{l}{l}")
            n1=int(input(a))  
            #print (f"value of (b)")
            n2=int(input(b))  
            n3=n1**2+2*n1*n2+n2**2
            print(g,f"({n1}+{n2})²")   
            print(d,n3) 
        except ValueError:
            print (g,h)
def q3():
        try:
            print(f"q3:-(a-b)²")
            n1=int(input(a))
            n2=int(input(b))
            n3=n1**2-2*n1*n2+n2**2
            print(g,f"({n1}-{n2})²")
            print(d,n3)
        except ValueError:
            print (g,h)
        except SyntaxError :
            print (g,h,"don't add simbols")
def q4() :
       try :
          print (f"q4:-(a+b)³")
          n1=int(input(a))
          n2=int(input(b))
          n3=n1**3+3*n1**2*n2+3*n1*n2**2+n2**3
          print(g,f"({n1}+{n2})³")
          print(d,n3)
       except ValueError :
                 print (g,h)
       except SyntaxError :
                 print(g,h,i)
def q5():
          try:
              print (f"q5:-(a-b)³")
              n1=int(input(a))
              n2=int(input(b))
              n3=n1**3-3*n1**2*n2+3*n1*n2**2-n2**3
              print (g,f"({n1}-{n2})³")
              print (d,n3)
          except ValueError :
              print (g,h)
          except SyntaxError :
              print (g,h,i)
#def q6():
#          try:
#              print (f"q6:-")
          
          
          
       
 
 
                
            
        
        
           
            
         
            
        

   

    
    
   
    
    
  

def dd():
    try:
        
    
        while True :
            p=input ()
            print (f"{l}{l}{p}{l}{l}")
            if p == ("q1"):
                 print(q1())
                 
            elif p == ("q2"):
                print(q2())
            elif p == ("q3"):
                print (q3())
            elif p == ("q0"):
                print (c)
            elif p==("q4"):
                print(q4())
            
            else:
                print ("type code")
    except SyntaxError :
                print("syntax error") 
    except ValueError :
                print("value error")   
                
    #except ValueError :
    #   print("write code an number") 
dd()          
       
