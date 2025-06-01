# Exercicio 1
salario = 100
idade = 20

a = salario < 500 and idade > 18      
b = salario >= 100 and idade < 30     
c = salario == 100 and idade >= 20      
d = salario != 50 and idade <= 25    
e = salario > 50 and idade == 20    
f = salario < 1000 or idade > 25    
g = salario >= 200 or idade < 18   
h = salario == 100 or idade >= 30      
i = salario != 100 and idade < 21     
j = salario > 200 and idade > 15   
k = salario <= 100 and idade >= 20      
l = salario < 500 or idade == 20     
m = salario > 200 and not idade > 18     
n = salario == 100 and not idade != 20    
o = salario != 100 or idade > 30    
p = not (salario > 1000 and idade > 18) 
q = not (salario == 100 and idade < 18)    
r = not (salario < 50 or idade > 40)   
s = not (salario >= 500 or idade <= 18)   
t = not (salario != 100 and idade == 20)

print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)