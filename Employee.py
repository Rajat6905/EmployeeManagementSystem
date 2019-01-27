class Employee:
    def __init__(self,u_id=None,name=None,salary=None):
        self.u_id=u_id
        self.name=name
        self.salary=salary
    
    def setId(self,u_id):
        self.u_id=u_id
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
        
    def getId(self):
        return self.u_id
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
#    
#obj=Employee()
#obj.setId('1')
#obj.setName("Rajat")
#obj.setSalary("1000")
#print(obj.getId())
#print(obj.getName())
#print(obj.getSalary())
    