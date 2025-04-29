# subscripting
print("hello"[0])
print("hello"[1])
print("hello"[-1])

# string
print("123" + "345")

# integer/whole number
print(123+345)

# large integers
print(123456789)
print(123_456_789)

# float/floating point number/decimal
print(3.14159)

# boolean
print(True)
print(False)

# length
print(len("Hello"))

# how we know the data type
print(type("hello"))
print(type(123))
print(type(12.3))
print(type(True))

# type convertion or casting int(), float(), str(), bool()
print(int("123") + int("456"))
print("Number of letters in your name: " + str(len(input("Enter your name here: "))))

# mathematical operations
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 2)

# number manipulation
bmi = 84 / 1.65 ** 2
print(bmi)
print(round(bmi))
print(round(bmi, 2))

# assignment operator
score = 10
score += 1
print(score)
score -= 1
print(score)
score *= 2
print(score)
score /= 2
print(score)