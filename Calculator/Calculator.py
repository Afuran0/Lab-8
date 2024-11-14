class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        
        return len(self.items) == 0

def evaluate_expression(expression):
    # Initialize  stacks
    num_stack = Stack()  
    op_stack = Stack()   

    def apply_operator():
        
        operator = op_stack.pop()
        
        right = num_stack.pop()
        left = num_stack.pop()
        
        if operator == '+':
            num_stack.push(left + right)
        elif operator == '-':
            num_stack.push(left - right)
        elif operator == '*':
            num_stack.push(left * right)
        elif operator == '/':
            num_stack.push(left / right)

    # Loop through the expression
    i = 0
    while i < len(expression):
        char = expression[i]
        
       
        if char == ' ':
            i += 1
            continue

        # Check if the character is a num
        if char.isdigit():
           
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.push(num)
            continue

        # Check if the character is an opening parenthesis '('
        elif char == '(':
            
            op_stack.push(char)

        #check if closing ^
        elif char == ')':
            
            while op_stack.peek() != '(':
                apply_operator()
            op_stack.pop()  

        # operators (+, -, *, /)
        elif char in "+-*/":
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            while (not op_stack.is_empty() and
                   op_stack.peek() != '(' and
                precedence[char] <= precedence[op_stack.peek()]):
                apply_operator()
            op_stack.push(char)

        # Move to the next char
        i += 1

  
    while not op_stack.is_empty():
        apply_operator()

   
    return num_stack.pop()

# Test cases
expression1 = "(((6+9)/3)*(6-4))"
expression2 = "10 + (2 * (6 + 4))"
expression3 = "100 * (2 + 12) / 4"
# print statments
print(evaluate_expression(expression1))  
print(evaluate_expression(expression2))  
print(evaluate_expression(expression3)) 
