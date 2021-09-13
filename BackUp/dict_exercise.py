data = {
    "names" : ["Ram","Shyam","Manoj","Mohit","Gopal"],
    "dept" : ["IT","HR","IT","HR","SALES"],
    "address" : ["delhi","pune","delhi","delhi","chennai"],
    "salary" : [45000,89000,43000,50000,25000]
    }

'''
1. Show the employees of IT department
2. Find the employee who is in IT department and has max salary
3. Show the employees who lives in delhi and earn more than 40000
4. Calculate average salary of employees of HR department
'''
for i in range(len(data['names'])):
    if data["dept"][i] == "IT":
        print(data["names"][i], data["dept"][i], data["address"][i])