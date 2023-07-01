what_to_find=input("What should i find for your ? a= acceleration, s=distance, u=initial velocity, v=final velocity, t=time taken")
what_to_find.lower
parameters=[a,s,t,u,v]
while what_to_find not in parameters:
    print("unknown parameter, please enter the correct one!")
    what_to_find=input("What should i find for your ? a= acceleration, s=distance, u=initial velocity, v=final velocity, t=time taken")

print("What are the given values?")
acc=int(input("Please enter the acceleration"))
vel=int(input("Please enter the final velocity"))
if what_to_find=a:

