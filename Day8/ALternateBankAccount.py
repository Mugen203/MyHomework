class Employee(object):
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def Display_count(self):
        print("Total Employees: {}".format(employee_count))
