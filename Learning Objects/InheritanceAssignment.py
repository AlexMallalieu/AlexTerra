# Alexander Mallalieu
# April 25th 2022

class Employee:
    name = ""
    phone = ""
    email = ""
    address = ""
    postal_zip = ""
    region = ""
    country = ""
    age = 0
    department = ""
    salary = 0
    full_or_part = ""
    bonus = 0
    tax = 0.1


    def net_worth(self):
        worth = int(self.age) - 18 * float(x.pay_after_tax())
        return worth



class InformationTech(Employee):
    programming_language = ""


class Teachers(Employee):
    subject = ""


class HumanResources(Employee):
    def __init__(self,name,phone,email,address,postal_zip, region, country, age, department, salary,full_or_part, boss, bonus, programming_language, subject, tax):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.postal_zip = postal_zip
        self.region = region
        self.country = country
        self.age = age
        self.department = department
        self.salary = salary
        self.full_or_part = full_or_part
        self.boss = boss
        self.bonus = bonus
        self.programming_language = programming_language
        self.subject = subject
        self.tax = tax


    def pay_after_tax(self):
        # print(str(self.tax), 'x ',  '1 - ', str(self.salary), '+', str(self.bonus))
        if self.bonus == 'N/A':
            self.bonus = 0.00
        total_pay = float(self.salary)*(int(1)-float(self.tax)) + int(self.bonus)
        return total_pay


    def boss_name(self):
        if self.boss == True:
            boss_name = "Roanna"
            return boss_name

class Communications(Employee):
    full_or_part = False

class Admin(Employee):
    bonus = 0.00

data_list = []
file = open("employeedata.txt","r")

for row in file:
    data = row.split(",")
    if str(data[0]) != "name":
         data_list.append(
             HumanResources(
                 name=data[0],
                 phone=data[1],
                 email=data[2],
                 address=data[3],
                 postal_zip=data[4],
                 region=data[5],
                 country=data[6],
                 age=data[7],
                 department=data[8],
                 salary=data[9],
                 bonus=data[10],
                 programming_language=data[11],
                 subject=data[12],
                 boss=data[13],
                 full_or_part=data[14],
                 tax = data[15]))

for x in data_list:
    print(x.name + "-" + str(x.pay_after_tax()) + "     " + str(x.net_worth()))


