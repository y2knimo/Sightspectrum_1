try:
	vars = 20/0
	print(vars)
except TypeError as aj:
    print(aj)

except:
	print("#Line8 String Error")