class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        index=0

        while index < len(tokens):

            if tokens[index] not in {"+","-","*","/"}:
                stack.append(tokens[index])
                index+=1

            else:
                num2=int(stack.pop())
                num1=int(stack.pop())
                
                if tokens[index] == "+":
                    res=num1+num2
                    stack.append(str(res))
                    index+=1

                elif tokens[index] == "*":
                    res=num1*num2
                    stack.append(str(res))
                    index+=1

                elif tokens[index] == "-":
                    res=num1-num2
                    stack.append(str(res))
                    index+=1

                elif tokens[index] == "/":
                    res=int(num1/num2)
                    stack.append(str(res))
                    index+=1

        return int(stack[0])
                

        


        