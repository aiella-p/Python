# def myfunc1():
#   x = "John"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x


def foo():
	name = "geek" # Our local variable

	def bar():
		nonlocal name		 # We are 
		#substituting global variable(name = "geek") with local variable (name = 'GeeksForGeeks') with nonlocal keyword....!!!
		name = 'GeeksForGeeks' # Overwrite this variable
		print(name)
		
	# Calling inner function
	bar()
	
	# Printing local variable
	print(name)

foo()
