from insurance_policy import InsurancePolicy

# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

class PropertyPolicy(InsurancePolicy):
    def __init__(self, policy_number, client_id, start_date, end_date,
                 property_address, property_value, property_type):
        super().__init__(policy_number, client_id, start_date, end_date)
        self._property_address = property_address
        self._property_value = property_value
        self._property_type = property_type

    def calculate_premium(self) -> float:
        # 0.5% of property value + 100,000 base
        return 0.005 * self._property_value + 100000

    def get_details(self):
        base = super().get_details()
        return (f"{base} | Property | Address: {self._property_address} | "
                f"Value: {self._property_value}")
