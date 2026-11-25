class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name: str = name
        self.__bill_amount: float = bill_amount
    def get_name(self):
        print(f"Patient Name: {self.__name}")
    def set_name(self, name: str):
        self.__name = name
    def get_bill_amount(self):
        print(f"Original Bill: \u20b1{self.__bill_amount:,.2f}")
    def set_bill_amount(self, bill_amount: float):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        final_bill = self.__bill_amount * (1.00-0.00)
        print(f"Final Bill: \u20b1{final_bill:,.2f}")
    @property
    def bill_amount(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        final_bill = self.bill_amount * (1.00-0.20)
        return print(f"Final Bill: \u20b1{final_bill:,.2f}")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        final_bill = self.bill_amount * (1.00-0.15)
        return print(f"Final Bill: \u20b1{final_bill:,.2f}")

# main code

patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-"*23, end="")
for x in [patient1, patient2, patient3]:
    x.get_name()
    x.get_bill_amount()
    x.calculate_bill()