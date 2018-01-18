class Contact:
   def __init__(self,name,number,address,note=""):
       self.name = name
       self.number = number
       self.address = address
       self.note = note

   def all(self):
       print(self.name)
       print(self.number)
       print(self.address)
       print(self.note)
       print("")
