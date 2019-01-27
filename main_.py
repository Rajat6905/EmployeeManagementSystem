from Employee import Employee 
from EmpServices import Services


class mainn: 
    def addEmp(self):
        user_id=input("Enter Id : ")
        user_name=input("Enter UserName : ")
        user_salary=input("Enter User Salary : ")
        obj=Employee()
        obj.setId(user_id)
        obj.setName(user_name)
        obj.setSalary(user_salary)
        return obj
    def search_by_id(self):
        user_idd=input("Enter User Id : ")
        return user_idd
    
    def search_by_Name(self):
        user_name=input("Enter User Name : ")
        return user_name

    def delete_By_Id(self):
        idd=input("Enter User Id : ")
        return idd
    
    def update(self):
        user_id=input("Enter user Id : ")
        us=Services.checkUser(user_id)
        if us:
            input_name=input("Enter new User Name: ")
            input_salary=input("Enter new Salary: ")
            Services.updateEmp(user_id,input_name,input_salary)
            print("Record Sucessfully updated \n")
        else:
            print("\n Invalid ID \n")
            
   
            
    def delete_By_Name(self):
        obj7=self.search_by_Name()
        name=Services.searchEmp_by_name(obj7)
        if len(name)==1:
            if Services.deleteEmp(name[0].getId()):
                print("Sucessfully Delete \n")
            else:
                print("Please Enter Invalid Id \n")
        elif len(name)>1:
            print("Found "+str(len(name))+ " Employees")
            for value in name:
                   print(value.getId(),value.getName(),value.getSalary())
            obj8=self.delete_By_Id()
            if Services.deleteEmp(obj8):
                print("Sucessfully Delete \n")
            else:
                print("Please Enter Invalid Id \n")
        else:
            print("No User found \n")
   
  
    def choice(self):
        print("Select Options ")
        print("1. Add Record ")
        print("2. View Record ")
        print("3. Search by Id ")
        print("4. Delete by Id ")
        print("5. Update Record ")
        print("6. Search by Name ")
        print("7. Delete By Name ")
        print("8. View By Alphabetic order")
        print("9. View By Salary (Decreasing order)")
        print("0. Exit")
        choice=input("Select your Choice : ")
        if choice=='1':
            obj1=self.addEmp()
            if Services.add(obj1):
                print("Record Sucessfully Added")
            else:
                print("Already Exists")
                
            self.choice()
        elif choice=='2':
            listEmp=Services.View()
            
            if listEmp:
                print("Total Employees: "+str(len(listEmp)))
                for i in listEmp:
                    print(i.getId(),i.getName(),i.getSalary())
                self.choice()
            else:
                print("No User found \n")
                
            
                self.choice()
        elif choice=='3':
            obj3=self.search_by_id()
            ob=Services.searchEmp(obj3)
            if ob:
                print(" User ID:"+ob.getId()+"\n","User Name: "+ob.getName()+"\n","User Salary: "+ob.getSalary()+'\n')
            else:
                print("Please Enter Valid Id \n")

            self.choice()
        elif choice=='4':
            obj4=self.delete_By_Id()
            if Services.deleteEmp(obj4):
                print("Sucessfully Delete \n")
            else:
                print("Please Enter Invalid Id \n")
       
            self.choice()
        elif choice=='6':
            obj5=self.search_by_Name()
            name=Services.searchEmp_by_name(obj5)
            if name:
                print("Found "+str(len(name))+ " Employees")
                for value in name:
                    print(value.getId(),value.getName(),value.getSalary())
            else:
                print("No User found \n")
            self.choice()
        elif choice=='5':
            self.update()
            self.choice()
            
        elif choice=='7':
            self.delete_By_Name()
            self.choice()
        elif choice=='8':
            
            listemploee=Services.View()
            if listemploee:
                sorted_emp=sorted(listemploee, key = lambda x : x.getName())
                for val in sorted_emp:
                    print(val.getId(),val.getName(),val.getSalary())
            else:
                print("No users found \n")
            self.choice()
        elif choice=='9':
            listemploee=Services.View()
            if listemploee:
                sorted_emp=sorted(listemploee, key = lambda x: int(x.getSalary()),reverse=True)
                for val in sorted_emp:
                    print(val.getId(),val.getName(),val.getSalary())
            else:
                print("No users found \n")
            self.choice()
        elif choice=='0':
            
            print("Sucessfully Exit \n")
        else:
            self.choice()
            
        
        
obj=mainn()
obj.choice()

