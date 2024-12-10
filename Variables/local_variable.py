# python-local-variable.py
# 
def function_local(a):
	print('a is -> ',a)
	a = 50
	print('After new value within the function a is -> ',a)
a = 100
function_local(40)
print('Value of a is ->',a)
