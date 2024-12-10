def outside():
       a = 10
       def inside():

           a = 20
           print("Inside a ->", a)
       inside()
       print("outside a->", a)
outside()
