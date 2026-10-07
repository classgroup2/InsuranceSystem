from abc import ABC, abstractmethod


# Capture everything that is common to every policy
# Abstract base: cannot instantiate this class directly
class InsurancePolicy(ABC):
    def __init__(self, policy_number, client_id, start_date, end_date):
        self._policy_number = policy_number
        self._client_id = client_id
        self._start_date = start_date
        self._end_date = end_date
        self._is_active = True

    @abstractmethod
    def calculate_premium(self) -> float:
        """Subclasses must implement this and return the premium as a float."""
        pass

    def get_details(self):
        return (f"Policy {self._policy_number} | Client {self._client_id} | "
                f"Active: {self._is_active}")
