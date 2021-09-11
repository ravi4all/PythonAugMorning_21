data = {
    "names" : ["Ram","Shyam","Mohit","Sumit"],
    "marks" : [78,98,70,58],
    }

'''
1. Find out total marks
2. Find out average marks
3. Print the data of students whose marks are above 80
'''
n = len(data["marks"])

total = 0

for i in range(n):
    total += data["marks"][i]

print("Total Marks :",total)

avg = total / n
print("Average Marks :",avg)



