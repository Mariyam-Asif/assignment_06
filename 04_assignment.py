class Bank:
    bank_name = "Default Bank" # class variable

    @classmethod
    def change_bank_name(cls, name): # Class method
        cls.bank_name = name

    def show_bank_name(self):
        print(f"Bank Name: {Bank.bank_name}")

customer1 = Bank()
customer2 = Bank()

customer1.show_bank_name()
customer2.show_bank_name()

Bank.change_bank_name("Super Bank")

customer1.show_bank_name()
customer2.show_bank_name()