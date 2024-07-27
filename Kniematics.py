import math

def get_value(prompt):
    return float(input(prompt))

def calculate_unknown_value(unknown):
    if unknown == 'a':
        v = get_value("Please enter the value of final velocity: ")
        u = get_value("Please enter the value of initial velocity: ")
        t = get_value("Please enter the value of time: ")
        a = (v - u) / t
        print("The acceleration is", a)
    
    elif unknown == 'v':
        u = get_value("Please enter the value of initial velocity: ")
        a = get_value("Please enter the value of acceleration: ")
        t = get_value("Please enter the value of time: ")
        v = u + (a * t)
        print("The final velocity is", v)
    
    elif unknown == 'u':
        v = get_value("Please enter the value of final velocity: ")
        a = get_value("Please enter the value of acceleration: ")
        t = get_value("Please enter the value of time: ")
        u = v - (a * t)
        print("The initial velocity is", u)
    
    elif unknown == 't':
        v = get_value("Please enter the value of final velocity: ")
        u = get_value("Please enter the value of initial velocity: ")
        a = get_value("Please enter the value of acceleration: ")
        t = (v - u) / a
        print("The time taken is", t)
    
    elif unknown == 's':
        u = get_value("Please enter the value of initial velocity: ")
        v = get_value("Please enter the value of final velocity: ")
        a = get_value("Please enter the value of acceleration: ")
        s = ((v * v) - (u * u)) / (2 * a)
        print("The displacement is", s)

def main():
    parameters = {'a', 's', 't', 'u', 'v'}
    
    what_to_find = input("What should I find for you? a= acceleration, s= distance, u= initial velocity, v= final velocity, t= time taken: ").lower()
    
    while what_to_find not in parameters:
        print("Unknown parameter, please enter the correct one!")
        what_to_find = input("What should I find for you? a= acceleration, s= distance, u= initial velocity, v= final velocity, t= time taken: ").lower()
    
    print("What are the given values?")
    calculate_unknown_value(what_to_find)

if __name__ == "__main__":
    main()
