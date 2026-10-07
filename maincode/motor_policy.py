from insurance_policy import InsurancePolicy
class MotorPolicy(InsurancePolicy):
    def __init__(self, policy_number, client_id, start_date, end_date,
                 vehicle_reg, vehicle_value, vehicle_type):
        super().__init__(policy_number, client_id, start_date, end_date)
        self._vehicle_reg = vehicle_reg
        self._vehicle_type = vehicle_type
        self._vehicle_value = vehicle_value

    def calculate_premium(self) -> float:
        # 3% of vehicle value + 150,000 base
        return 0.03 * self._vehicle_value + 150000

    def get_details(self):
        base = super().get_details()
        return (f"{base} | Motor | Reg: {self._vehicle_reg} | "
                f"Value: {self._vehicle_value}")
    
    
