# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

from insurance_policy import InsurancePolicy


class HealthPolicy(InsurancePolicy):
    def __init__(self, policy_number, client_id, start_date, end_date,
                 age, coverage_level):
        super().__init__(policy_number, client_id, start_date, end_date)
        self._age = age
        self._coverage_level = coverage_level

    def calculate_premium(self) -> float:
        # Base by coverage level, adjusted by age
        base_rates = {"Basic": 15000000, "Standard": 30000000, "Premium": 50000000}
        base = base_rates.get(self._coverage_level, 30000000)
        if self._age < 25:
            factor = 1.2
        elif self._age <= 45:
            factor = 1.0
        else:
            factor = 1.4
        return base * factor

    def get_details(self):
        base = super().get_details()
        return (f"{base} | Health | Age: {self._age} | "
                f"Coverage: {self._coverage_level}")
