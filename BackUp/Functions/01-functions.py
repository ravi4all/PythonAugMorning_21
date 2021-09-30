# Variable Scope - Global, Local

# Global
x = 12
y = 55

# Function Definition
def add():
    print("Hello User")
    # Local Scope
    x = 10
    y = 5
    z = x + y
    print("Sum is",z)

# Function Call
add()
print("X is",x)
print("Y is",y)
