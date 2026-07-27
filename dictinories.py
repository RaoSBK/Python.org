import numpy as np

arr = np.array([34])

print(arr.ndim) #printing the dimension of the list

arr = np.array([[[],[]]])
print(arr.ndim)


#range

a = np.arange(0,10, 2)      # (start, stop, step)
print(a)

#linspace
arr = np.linspace(0,1,5)    #(start, stop, no of values) this is the property of the linspace
print(arr)


#logspace
arr = np.logspace(1,3,3)        #logarithmic scale array -> 10^1 -> 10^2, 10^3   number of points
print(arr)


        #np.logspace(start, ending -> powers, 3 -> points)


#zeros  -> array full of zeros

arr = np.zeros(5)
print(arr)



arr = np.zeros([2,3])   #(rows, coloumn)
print(arr)


#ones -> array full of ones

arr = np.ones([4,2], dtype=int)
print(arr)


#create an array full of any values
arr = np.full(10,2)
print(arr)


arr = np.full([2,4], 7.1) #([rows, coloumn], default values)
print(arr)


#uninitialized array -> create an array without setting any sort of value
arr = np.empty([2,3])
print(arr)


#random float
arr = np.random.rand(10)
print(arr)


arr = np.random.rand(2,3)
print(arr)


arr = np.random.randn(2,3)       # Return a sample (or samples) from the "standard normal" distribution, This is a convenience function for users porting code from Matlab, and wraps standard_normal. That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like numpy.zeros and numpy.ones
print(arr)


arr = np.random.randint(10,100, size=(2, 3))        #(start, stop, size)
print(arr)