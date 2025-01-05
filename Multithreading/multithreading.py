# used to perform multiple tasks concurrently. Good for input / output bound tasks like reading
# files or fetching data from APIs.
# threading.thread(target=my_function) - 

# import threading
# import time
# #threading.thread(target=my_function) # we access threating module and call the constractor(thread(target=my_function))

# def walk_dog():
#     time.sleep(8)
#     print("You finish walking the dog")

# def take_out_trash():
#         time.sleep(2)
#         print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")      

# tr1 = threading.Thread(target=walk_dog)
# tr1.start()

# tr2 = threading.Thread(target=take_out_trash)
# tr2.start()

# tr3 = threading.Thread(target=get_mail)
# tr3.start()

# tr1.join()
# tr2.join()
# tr3.join()

# print("All Threads are finish")
# walk_dog()
# take_out_trash()
# get_mail()    

# ########################################
# # To display first name of the Dog...

# import threading
# import time
# #threading.thread(target=my_function) # we access threating module and call the constractor(thread(target=my_function))

# def walk_dog(first):
#     time.sleep(8)
#     print(f"You finish walking {first}")

# def take_out_trash():
#         time.sleep(2)
#         print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")      

# tr1 = threading.Thread(target=walk_dog, args=("jenny",)) # Since we have tuple with one argument should end up with (,)
# tr1.start()

# tr2 = threading.Thread(target=take_out_trash)
# tr2.start()

# tr3 = threading.Thread(target=get_mail)
# tr3.start()

# tr1.join()
# tr2.join()
# tr3.join()

# print("All Threads are finish")

########################################
# To display first and last names of the Dog...

import threading
import time
#threading.thread(target=my_function) # we access threating module and call the constractor(thread(target=my_function))

def walk_dog(first,last):
    time.sleep(8)
    print("======================================")
    print(f"You finish walking {first} {last} 🐕‍🦺")
    print("======================================")

def take_out_trash():
        time.sleep(2)
        print("You take out the trash: 🗑️ 🗑️ ")

def get_mail():
    time.sleep(4)
    print("*****You get the mail: 💌*****")      

tr1 = threading.Thread(target=walk_dog, args=("Jenny","Aiella")) # Since we have tuple with one argument should end up with (,)
tr1.start()

tr2 = threading.Thread(target=take_out_trash)
tr2.start()

tr3 = threading.Thread(target=get_mail)
tr3.start()

tr1.join()
tr2.join()
tr3.join()

print("All Threads are finish: 👍👍👍")

