#importing libraries
import numpy as np
import math                                   #it is a built-in module that you can use for mathematical tasks
import matplotlib.pyplot as plt               #it is collection of functions that make matplotlib work like MATLAB

#initializing variables

gravity_acceleration=9.81                    # gravity acceleration constant approximately equal 9.81
flag= True 

# the road type
roadtype=["concrete","ice","water","gravel","sand"]

# the road condition
roadcondition=["dry","wet","aquaplaning"]

# the coefficient of friction type
frictiontype=["static","dynamic"]

while(flag):
    # input the initial velocity of the car (in km/hr)
    velocity_Kh=float(input("Enter the initial velocity of the car before braking (in km/hr): "))
    if velocity_Kh <=0:
        print("Please try again")
        continue

    #input for wheel type
    w_type = str(input("Enter the wheel type [rubber]: "))
    if w_type != "rubber" :
         print("Please try again")
         continue

    #input for road type
    r_type = str(input("Enter the road type [concrete, ice, water, gravel, sand]: "))
    if r_type not  in roadtype :
        print("Please try again")
        continue
        
    #input for road condition
    r_con=str(input(("Enter the road condition [dry, wet, aquaplaning]:")))
    if r_con not in roadcondition :
        print("Please try again")
        continue
        
    #input for  coefficient friction type
    f_type =str(input(("Enter the coefficient of friction type (static or dynamic):")))
    if f_type not in frictiontype :
        print("Please try again)")
        continue
    if r_type == "concrete":
        if r_con == "dry" and f_type== "static": mu = 0.65 
        elif r_con == "dry" and  f_type=="dynamic" : mu = 0.5 
        elif r_con  == "wet" and f_type == "static": mu = 0.4
        else: mu = 0.35
        
    elif r_type == "ice":
        if r_con == "dry" and f_type == "static": mu = 0.2
        elif r_con == "dry" and  f_type=="dynamic" : mu = 0.15
        elif r_con == "wet" and f_type == "static": mu = 0.1
        else: mu = 0.08
            
    elif r_type == "water":
        if r_con== "aquaplaning" and f_type == "static": mu = 0.1
        else: mu = 0.05 
    
    elif r_type == "gravel" and r_con == "dry" and f_type == "dynamic": mu = 0.35
        
    elif r_type == "sand" and r_con == "dry" and f_type== "dynamic": mu = 0.3
    else:
        print(" wrong choice, please try again ")
        continue

    break
        

velocity_ms=velocity_Kh*5/18                #convert velocity of car in (kileometer per hour) to (meter per) 
velocity=np.arange(0,velocity_ms+1,10,dtype=int) #create a numpy array to velocities

# calculate the braking distance, bd formula = (velocity ^ 2) / (2 * mu * gravity acceleration)
#iterating over the list of initial velocities v, and for each initial velocity i

bd = [(i**2 - velocity_ms**2) / (2 * mu * gravity_acceleration) for i in velocity]
    
# braking time = (velocity) / (mu * gravity acceleration)
t = [(velocity[i] - velocity_ms) / (-mu * gravity_acceleration) for i in range(len(velocity))]
#t = float( v / (mu * g))
#Rule of Thumb
s_normal=np.array((velocity / 10)**2)
s_danger=np.array(((velocity/10)**2)*0.5)
s_reaction=np.array((velocity/10)*3)

# ploting figures
fig, (ax1, ax2,ax3) = plt.subplots(1, 3,figsize=(15,4))
ax1.plot(velocity, bd, label='Physics model',color="red")
ax1.set_title('Braking Distance vs. Initial Velocity')
ax1.set_xlabel('Initial Velocity (km/h)')
ax1.set_ylabel('Braking Distance (m)')
ax1.legend(loc='lower right')

ax2.plot(velocity, t,color="black")
ax2.set_xlabel('Initial velocity (m/s)')
ax2.set_ylabel('Braking time (s)')
ax2.set_title('Braking time vs. Initial velocity')

ax3.plot(velocity, s_normal, label='S_normal',color="green")
ax3.plot(velocity, s_danger, label='S_danger',color="yellow")
ax3.plot(velocity,s_reaction, label='S_reaction',color="blue")
ax3.set_title('Rule of thumb')
ax3.set_xlabel('Initial Velocity (km/h)')
ax3.set_ylabel('Braking Distance (m)')
ax3.legend(loc='upper left')
plt.show()