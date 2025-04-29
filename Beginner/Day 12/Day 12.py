# local vs global scope
enemies = 1 # global scope

def increase_enemies():
    enemies = 2 # local scope, it can only be accessed inside the function
    print(enemies)

increase_enemies()
print(enemies)

# exercise prime number checker
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range (2, num):
            if num % i == 0:
                return False
        return True

# Modifying global scope
enemies1 = 1 # global scope

def increase_enemies1():
    global enemies1
    enemies1 += 1 # local scope, it can only be accessed inside the function
    print(enemies1)

# BUT DONT TRY TO MODIFY GLOBAL SCOPE
# Just use it as an input
enemies2 = 1 # global scope

def increase_enemies2(enemy):
    enemy += 1 # local scope, it can only be accessed inside the function
    return enemy

# Global Contents
pi = 3.14159 # you do not want to change it at all

def my_func():
    print(pi)

my_func()
