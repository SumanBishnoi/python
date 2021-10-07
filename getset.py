# class car:
#     def __init__(self,a=40):
#         self.speed = a
#     def get_speed(self):
#         return self.speed
#     def set_speed(self,a):
#         self.speed=a
#         return

# c1= car()
# print(c1.get_speed())
# c1.set_speed(80)
# print(c1.get_speed())
# c1.speed= 20
# print(c1.get_speed())

#private variable
# class car:
#     def __init__(self,a=40):
#         self._speed = a
#     def get_speed(self):
#         return self._speed
#     def set_speed(self,a):
#         self._speed=a
#         return

# c1= car()
# print(c1.get_speed())
# c1.set_speed(80)
# print(c1.get_speed())
# c1.speed= 20 #this will not change the value of variable as it is private now
# print(c1.get_speed())


# class car:
#     def __init__(self,a=40):
#         self.set_speed(a)
#     def get_speed(self):
#         return self._speed
#     def set_speed(self,a):
#         if a<=0 or a>=160:
#             print("speed needs to be between 0 to 160")
#         else:
#          self._speed=a
#         return

# c1=car()
# print(c1.get_speed())
# c1.set_speed(0)
# print(c1.get_speed())


class car:
    def __init__(self,a=40):
        self._speed= a
    def get_speed(self):
        return self._speed
    def set_speed(self,a):
        if a<=0 or a>=160:
            print("speed needs to be between 0 to 160")
        else:
         self._speed=a
        return
    speed= property(get_speed, set_speed)

c1=car()
print(c1.speed)
c1.speed=80
print(c1.speed)