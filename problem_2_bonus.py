def make_to_text(num):
    s = ''
    
    
    

d = {}
num1, num2 = int(input()), int(input())
d = {i:make_to_text(i) for i in range(num1, num2+1)}
print(d)

#1 10 100 1000 10000 100000 1000000