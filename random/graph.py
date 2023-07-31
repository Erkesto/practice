import matplotlib.pyplot as mp
a = [1,2,3]
b = [1,2,3]
mp.plot(a,b,label = 'line 1',color='blue',marker='o',markerfacecolor='black')
mp.title("dev chutiya") 
mp.xlabel("x-axis")
mp.ylabel("y-axis")
mp.legend()
mp.show()