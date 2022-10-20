import numpy as np

a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)

b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
			"Array type is complex:\n", d)

e = np.random.random((2, 2))
print ("\nA random array:\n", e)

f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
										"0 and 5:\n", g)

arr = np.array([[1, 2, 3, 4],
				[5, 2, 4, 2],
				[1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)
