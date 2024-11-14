class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
    
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)

        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                return False
            
#chest if stack is empty 
    return stack.is_empty()

#test functions

print(is_balanced("(a + b) * (c - d)"))       
print(is_balanced("{[a * (b + c)] - d}"))      
print(is_balanced("([a + b)]"))                
print(is_balanced("{(a + b) * [c - d]})"))     
print(is_balanced("((a + b) * c)"))            
