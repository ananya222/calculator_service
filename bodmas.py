from calculator import calculator
from stack import stack

def parse_expression(expr):
    start_index_operand=0
    operand_stack=stack()
    operator_stack=stack()
    result=0
    for i in range(0,len(expr)):
        if(expr[i]=='+' or expr[i]=='-' or expr[i]=='*' or expr[i]=='/' or expr[i]=='='):
            operand=expr[start_index_operand:i]
            operator=expr[i]
            start_index_operand=i+1
            if(operator_stack.is_empty()==True):
                operand_stack.push(operand)
                operator_stack.push(operator)
            else:
                previous_operator=operator_stack.pop()
                if(previous_operator=='/' or previous_operator=='*'):
                    result=calculate(operand_stack.pop(),operand,previous_operator)
                    operand_stack.push(result)
                    operator_stack.push(operator)
                if(previous_operator=='+'):
                    operator_stack.push(previous_operator)
                    operator_stack.push(operator)
                    operand_stack.push(operand)
                if(previous_operator=='-'):
                    operator_stack.push('+')
                    operator_stack.push(operator)
                    operand='-'+operand
                    operand_stack.push(operand)
    return reduce(operand_stack,operator_stack)

def reduce(operand_stack,operator_stack):
    result=0
    if(operand_stack.length()==1):
        return float(operand_stack.pop())
    while(operand_stack.is_empty()==False and operator_stack.is_empty()==False):
        operand2=operand_stack.pop()
        operand1=operand_stack.pop()
        operator=operator_stack.pop()
        if(operator=='='):
            operator=operator_stack.pop()
        result=calculate(operand1,operand2,operator)
        operand_stack.push(result)
    return float(result)

def calculate(operand1,operand2,operator):
    c=calculator()
    result=0
    if(operator=='+'):
        result=float(operand1)+float(operand2)

    if(operator=='-'):
        result=float(operand1)-float(operand2)

    if(operator=='*'):
        result=float(operand1)*float(operand2)

    if(operator=='/'):
        result=float(operand1)/float(operand2)
    return result
