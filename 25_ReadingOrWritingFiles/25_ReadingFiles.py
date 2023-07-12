employeeFile = open("groot.txt", "r")

for employee in employeeFile.readlines():
    print(employee)

employeeFile.close()