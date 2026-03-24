# 1. Basic Positional Arguments 
def add(a,b):
    print("A = ",a)
    print("B = ",b)
    return a+b
result = add(2,5)
print("Sum =",result) 

# 2. Student Information 
def studen_info(name,roll,marks):
    print("Name : ",name)
    print("Roll no : ",roll)
    print("Marks : ",marks)
student_info("Ravi",101,88)  

# 3. Simple Interest 
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("Simple Interest :",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)     

# 4. Area of Circle 
def ar_circle(r):
    a_circle=3.14*r*r
    print("Area of Circle : ",a_circle)
ar_circle(1.5)
ar_circle(4) "

# 5. Check number positive,negative or zero 
def check_value(no):
    if(no>0):
        print("Positive")
    elif(no<0):
        print("Negative")
    else:
        print("Zero")
check_value(0)  
check_value(90)  
check_value(-15) 

# 6. Odd or Even 
def odd_even(no):
    if(no%2==0):
        print(f"Value {no} is even")
    else:
        print(f"Value {no} is odd")
odd_even(50)
odd_even(15) 

# 7. Arithmatic operations substraction , multiplication and division   
def addition(a,b):
    add = a+b
    print("Addition of two values",add)
addition(50,10.5)
addition(100,200)   

