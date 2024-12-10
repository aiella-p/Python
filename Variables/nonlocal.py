def outside():
       a = 10
       def inside():
              nonlocal a
              a = 20
              print("The value of a in inside() function - ", a)
       inside()
       print("The value of a in outside() function -  ", a)
outside()
