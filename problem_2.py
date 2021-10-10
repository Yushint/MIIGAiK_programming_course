def func1(tpl, num1, num2):
    if (num1 not in tpl):
        return ()
    elif num2 not in tpl:
        ind = tpl.index(num1)
        l_tuple = [tpl[i] for i in range(ind, len(tpl))]
        tpl = tuple(l_tuple)
        return tpl
    else:
        if num1 in tpl and num2 in tpl:
            ind = tpl.index(num1)
            l_tuple = []
            for i in range(ind, len(tpl)+1):
                if tpl[i] != num2:
                    l_tuple.append(tpl[i])
                else:
                    l_tuple.append(tpl[i])
                    break
            tpl = tuple(l_tuple)
            return tpl
    

def func2(tpl):
    dictionary = {tpl[i]:(tpl[i]**2 if str(tpl[i]).isdigit() else 'квадрат') for i in range(len(tpl))}
    return dictionary

tuple0 =  (8,2,'k',1,3,4,'jj',5,';',2,8,4,1,5,8)
tuple1 = func1(tuple0,1,8)
b = func2(tuple1)
print(tuple0)
print(tuple1)
print(b)