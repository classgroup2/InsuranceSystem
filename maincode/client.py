# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

# Represent the person that is to be recorded
class Client:
    def __init__(self, client_id, name, phone, email):
        self._client_id = client_id
        self._name = name
        self._phone = phone
        self._email = email

    def get_contact_info(self):
        return f"{self._name} | {self._phone} | {self._email}"

    def __str__(self):
        return f"Client ({self._client_id}: {self._name})"
