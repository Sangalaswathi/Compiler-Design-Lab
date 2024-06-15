def generate_three_address_code(instruction):
    operators = ['+','-','*','/']
    temp = {}
    k = 1
    stack = []
    for i in instruction:
        if i in operators:
            stack.append(i)
        elif i=='(':
            stack.append(i)
        elif i==')':
            op1 = ''
            op2 = ''
            op = ''        
            while stack[-1]!='(':
                s = stack.pop()
                if s in operators:
                    op = s
                elif op=='':
                    op2 = s+op2
                else:
                    op1 = s+op1
            temp['t'+str(k)] = op1+op+op2
            stack.pop()
            stack.append('t'+str(k))
            k+=1
        else:
            stack.append(i)
    return temp

input ='(a+((b*e)+(c-d)))'
address_code = generate_three_address_code(input)
print("Three address code")
for i in address_code:
    print(i+' := '+address_code[i])