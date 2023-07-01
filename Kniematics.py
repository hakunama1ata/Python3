import math

what_to_find=input("What should i find for you ? a= acceleration, s=distance, u=initial velocity, v=final velocity, t=time taken")
what_to_find.lower
parameters=set(['a','s','t','u','v'])
while what_to_find not in parameters:
    print("unknown parameter, please enter the correct one!")
    what_to_find=input("What should i find for you ? a= acceleration, s=distance, u=initial velocity, v=final velocity, t=time taken")

print("What are the given values?")
if what_to_find=='a':
    v=float(input("Please enter the value of final velocity"))
    u=float(input("Please enter the value of initial velocity"))
    s=float(input("Please enter the value of displacement"))
    t=float(input("Please enter the value of time"))
    t=(v-u)/a
    u=v-(a*t)
    u=(s-((a*(t*t)/2)))/t
    u=(math.sqrt((v*v)-(2*a*s)))
    s=((u*t)+((1/2)*a*t*t))
    s=((v*v)-(u*u))/(2*a)
    v=(math.sqrt((u*u)+(2*a*s)))
    v=u+(a*t)
    a=float((v-u)/t)
    a=((v*v)-(u*u)/(2*s))
    a=(2*(s-(u*t)))/(t*t)
    print("The acceleration is",a)
elif what_to_find=='v':
    u=float(input("Please enter the value of initial velocity"))
    s=float(input("Please enter the value of displacement"))
    t=float(input("Please enter the value of time"))
    a=float(input("Please enter the value of acceleration"))
    t=(v-u)/a
    u=v-(a*t)
    u=(s-((a*(t*t)/2)))/t
    u=(math.sqrt((v*v)-(2*a*s)))
    s=((u*t)+((1/2)*a*t*t))
    s=((v*v)-(u*u))/(2*a)
    v=(math.sqrt((u*u)+(2*a*s)))
    v=u+(a*t)
    a=float((v-u)/t)
    a=((v*v)-(u*u)/(2*s))
    a=(2*(s-(u*t)))/(t*t)
    print("The final velocity is",v)
    
elif what_to_find=='u':
    v=float(input("Please enter the value of final velocity"))
    s=float(input("Please enter the value of displacement"))
    t=float(input("Please enter the value of time"))
    a=float(input("Please enter the value of acceleration"))
    t=(v-u)/a
    u=v-(a*t)
    u=(s-((a*(t*t)/2)))/t
    u=(math.sqrt((v*v)-(2*a*s)))
    s=((u*t)+((1/2)*a*t*t))
    s=((v*v)-(u*u))/(2*a)
    v=(math.sqrt((u*u)+(2*a*s)))
    v=u+(a*t)
    a=float((v-u)/t)
    a=((v*v)-(u*u)/(2*s))
    a=(2*(s-(u*t)))/(t*t)
    print("The initial velocity is",u)
elif what_to_find=='t':
    v=float(input("Please enter the value of final velocity"))
    s=float(input("Please enter the value of displacement"))
    a=float(input("Please enter the value of acceleration"))
    u=float(input("Please enter the value of initial velocity"))
    t=(v-u)/a
    u=v-(a*t)
    u=(s-((a*(t*t)/2)))/t
    u=(math.sqrt((v*v)-(2*a*s)))
    s=((u*t)+((1/2)*a*t*t))
    s=((v*v)-(u*u))/(2*a)
    v=(math.sqrt((u*u)+(2*a*s)))
    v=u+(a*t)
    a=float((v-u)/t)
    a=((v*v)-(u*u)/(2*s))
    a=(2*(s-(u*t)))/(t*t)
    print("The time is",t)

else:
    a=float(input("Please enter the value of acceleration"))
    v=float(input("Please enter the value of final velocity"))
    u=float(input("Please enter the value of initial velocity"))
    t=float(input("Please enter the value of time"))
    t=(v-u)/a
    u=v-(a*t)
    u=(s-((a*(t*t)/2)))/t
    u=(math.sqrt((v*v)-(2*a*s)))
    s=((u*t)+((1/2)*a*t*t))
    s=((v*v)-(u*u))/(2*a)
    v=(math.sqrt((u*u)+(2*a*s)))
    v=u+(a*t)
    a=float((v-u)/t)
    a=((v*v)-(u*u)/(2*s))
    a=(2*(s-(u*t)))/(t*t)
    print("The value of displacement is",s)


