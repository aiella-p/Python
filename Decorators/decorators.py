# A function that extends the behavior of another function w/o modifiying the base function
#pass the base function as an argument to the decorator
#  get_ice_cream("vanilla") - A base function, and @add_sprinkles - Decorator is also a function

# create base function

# def get_ice_cream():
#     print("Here is your ice cream 🍦")

# get_ice_cream()    

# ####################
# # creating decorator

# def add_sprinkles(func):
#     def wrapper(): # within this function we call parameter(func)
#         func() 
#         return wrapper
    
# #########################
# # to apply Decorator to base function get_ice_cream() preceeding with decorator function(@add_sprinkles)

# def add_sprinkles(func):
#     def wrapper(): # within this function we call parameter(func)
#       print("You add sprinkles 😄") 
#       func()       
#     return wrapper

# @add_sprinkles
# def get_ice_cream():
#     print("Here is your ice cream 🍦")

# get_ice_cream()    

#########################
#  Let's add more than one decorators ....as below, we add more decorators to base function

def add_sprinkles(func):
    def wrapper(*args,**kwargs): # within this function we call parameter(func)
      print("You add sprinkles 😄") 
      func(*args,**kwargs)       
    return wrapper

def add_fudge(func):
   def wrapper(*args,**kwargs): # within this function we call parameter(func)
      print("You add fudge 🍫") 
      func(*args,**kwargs)       
   return wrapper
   
   
@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("Vanilla")    
