# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

# Represent a request for payment against a policy
class Claim:
    VALID_STATUSES = ("Pending", "Approved", "Rejected", "Paid")

    def __init__(self, claim_id, policy_number, amount, description, claim_date):
        self._claim_id = claim_id
        self._policy_number = policy_number
        self._description = description
        self._claim_date = claim_date
        self._status = "Pending"
        self.amount = amount  # goes through the setter (validates)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Amount must be a number.")
        if value <= 0:
            raise ValueError("Claim amount must be positive.")
        self._amount = float(value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in Claim.VALID_STATUSES:
            raise ValueError(f"Invalid status. Allowed: {Claim.VALID_STATUSES}")
        self._status = new_status

    @property
    def claim_id(self):
        return self._claim_id  # read-only: no setter

    def __str__(self):
        return (f"Claim {self._claim_id} | Policy {self._policy_number} | "
                f"Amount {self._amount} | Status {self._status}")
