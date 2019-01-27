import pickle
import os
class Services:
    
        
    l=[]
#    @staticmethod
    def add(emp):
        scores = []
        high_scores_filename='data.dat'

#        for i in Services.l:
#            if emp.getId() == i.getId():
#                return False
#        Services.l.append(emp)
        if os.path.exists(high_scores_filename):
            with open(high_scores_filename,'rb') as rfp: 
                scores = pickle.load(rfp)
                
            rfp.close()
                
        for values in scores:
            if emp.getId()==values.getId():
                return False
        scores.append(emp)
        
        with open(high_scores_filename,'wb') as wfp:
            pickle.dump(scores, wfp)
        wfp.close()
        return True
    
    def View():
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
        rfp.close()
        return scores
#        return Services.l
    def  searchEmp(user_id):
        
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
        rfp.close()
            
      
        for j in scores:#Services.l:
            if user_id == j.getId():
                return j
        return False

    def  searchEmp_by_name(user_name):
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
            rfp.close()
            
        allEmp=[]
        for v in scores:#Services.l:
            if user_name.lower() == v.getName().lower():
                allEmp.append(v)
        return allEmp
        
    def deleteEmp(idd):
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
        rfp.close()
            
        for m in scores:#Services.l:
            if idd == m.getId():
                scores.remove(m)
#                Services.l.remove(m)
                with open('data.dat','wb') as wfp:
                    pickle.dump(scores, wfp)
                rfp.close()
                return True
        
                
        return False
        
    def checkUser(idd):
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
        rfp.close()
        
        for m in scores:#Services.l:
            if idd == m.getId():
                return m
        return False
    def updateEmp(u_id,n_name,n_salary):
        with open('data.dat','rb') as rfp:
            scores = pickle.load(rfp)
            
        for n,val in enumerate(scores):
            if val.getId()==u_id:
                scores[n].setName(n_name)
                scores[n].setSalary(n_salary)
                
            
#        for val in scores:#Services.l:
#            val.setName(n_name)
#            val.setSalary(n_salary)

        with open('data.dat','wb') as wfp:
    
            pickle.dump(scores, wfp)
        wfp.close()
            
            
           
            
            
    
            
    
        
        
            
            
        
        
        
        
        
        
        
        
        
        
        
       
        
        