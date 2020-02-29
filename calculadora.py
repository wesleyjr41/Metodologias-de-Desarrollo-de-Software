pm="***********Bienvenido a la Calculadora***********"; 
print(pm);
def suma(a,b):
   s=a+b;
   return s;
def resta(a, b):
   r=a-b
   return r
def multiplicacion(a, b):
   pass;
def division(a, b):
   try:
      d=a/b
   except ZeroDivisionError:
      print("no se pued dividir para 0")
   else:
      return d     
def potencia (a):
   pass;
