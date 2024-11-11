class Business:
    def __init__(self, name, address, founding_year, email, phone):
        self.name = name
        self.address = address
        self.founding_year = founding_year
        self.email = email
        self.phone = phone

    def change_phone(self, new_phone):
        self.phone = new_phone

    def display_info(self):
        print(f"Business Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Founding Year: {self.founding_year}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


my_business = Business(name="ABC Corp", address="123 Main St", founding_year=2000, email="info@abccorp.com", phone="555-123-4567")
my_business.display_info()
my_business.change_phone("555-987-6543")
my_business.display_info()
