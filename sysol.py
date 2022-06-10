from math import pow
import tkinter 
import tkinter.messagebox
print("Write a system in this way ")
print("______")
print("{ a x + b y = c ")
print("{ d x + e y = f ")
print("______")
print("such as => a,b,c,d,e and f ∈ ℝ")
print("=> (a,b) and (d,e) ≠ (0,0)")
print("∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆")
print("Choose a specific value for a")
a = float(input())
print("Choose a specific value for b")
b = float(input())
print("Choose a specific value for c")
c = float(input())
print('Choose a specific value for d')
d = float(input())
print("Choose another specific value for e")
e = float(input())
print("Now, choose the last value for f")
f = float(input())
print ("##############################")
res = a*e-b*d

if a==0 or b ==0:
    tkinter.messagebox.showerror(title="Error-System", message="Impossible, because (a, b)=(0, 0)")
elif  d==0 or e==0:
    tkinter.messagebox.showerror(title="Error-System", message="Impossible, because (d, e)=(0, 0")

else :       
    if res != 0:
       print("it is system admits (x,y), such that :")
       print("x=",(c*e-b*f)/res ,"y=",(a*f-c*d)/res )
    else :
       if (c*e-b*f)/res == 0 and (a*f-c*d)/res == 0 :
           print ("this system admits an infinity of solutions")
       if (c*e-b*f)/res == 0 or (a*f-c*d)/res == 0 :
           print ("this system does not admit a solution")
           print (" S=Ø ")
