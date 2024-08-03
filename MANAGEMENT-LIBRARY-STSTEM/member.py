
#Memeber class
class Member:
    def __init__(self, name, memebership_id):
        self.name = name
        self.memebership_id = memebership_id
    
    def __str__(self):
        return f"Member Name: {self.name} Membership Id: {self.memebership_id}" 
      