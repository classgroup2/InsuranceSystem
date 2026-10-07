from motor_policy import MotorPolicy
from health_policy import HealthPolicy
from property_policy import PropertyPolicy
from client import Client
from claim import Claim

# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

class InsuranceSystem:
    def __init__(self):
        self._clients = {}   # client_id -> Client
        self._policies = {}  # policy_number -> InsurancePolicy
        self._claims = {}    # claim_id -> Claim
        self._next_client_num = 1
        self._next_policy_num = 1
        self._next_claim_num = 1

    # ---------- Clients ----------
    def register_client(self, name, phone, email):
        client_id = f"C{self._next_client_num:03d}"
        client = Client(client_id, name, phone, email)
        self._clients[client_id] = client
        self._next_client_num += 1
        return client

    def list_clients(self):
        return list(self._clients.values())

    def get_client(self, client_id):
        return self._clients.get(client_id)  # None if not found

    # ---------- Policies ----------
    def create_motor_policy(self, client_id, start, end, reg, value, vtype):
        if client_id not in self._clients:
            raise ValueError(f"Client {client_id} does not exist.")
        pnum = f"M{self._next_policy_num:03d}"
        policy = MotorPolicy(pnum, client_id, start, end, reg, value, vtype)
        self._policies[pnum] = policy
        self._next_policy_num += 1
        return policy

    def create_health_policy(self, client_id, start, end, age, coverage_level):
        if client_id not in self._clients:
            raise ValueError(f"Client {client_id} does not exist.")
        pnum = f"H{self._next_policy_num:03d}"
        policy = HealthPolicy(pnum, client_id, start, end, age, coverage_level)
        self._policies[pnum] = policy
        self._next_policy_num += 1
        return policy

    def create_property_policy(self, client_id, start, end, address, value, property_type):
        if client_id not in self._clients:
            raise ValueError(f"Client {client_id} does not exist.")
        pnum = f"P{self._next_policy_num:03d}"
        policy = PropertyPolicy(pnum, client_id, start, end, address, value, property_type)
        self._policies[pnum] = policy
        self._next_policy_num += 1
        return policy

    def get_policy(self, policy_number):
        return self._policies.get(policy_number)

    def list_policies(self):
        return list(self._policies.values())

    def get_client_policies(self, client_id):
        return [p for p in self._policies.values() if p._client_id == client_id]

    # ---------- Claims ----------
    def record_claim(self, policy_number, amount, description, claim_date, max_limit=None):
        if policy_number not in self._policies:
            raise ValueError(f"Policy {policy_number} does not exist.")
        if max_limit is not None and amount > max_limit:
            raise ValueError(f"Claim amount exceeds policy limit of {max_limit}.")
        cid = f"CL{self._next_claim_num:03d}"
        claim = Claim(cid, policy_number, amount, description, claim_date)
        self._claims[cid] = claim
        self._next_claim_num += 1
        return claim

    def update_claim_status(self, claim_id, new_status):
        if claim_id not in self._claims:
            raise ValueError(f"Claim {claim_id} does not exist.")
        self._claims[claim_id].status = new_status  # uses setter (validates)

    def get_claims_for_policy(self, policy_number):
        return [c for c in self._claims.values() if c._policy_number == policy_number]

    def get_claims_for_client(self, client_id):
        client_policy_nums = {
            p._policy_number
            for p in self._policies.values()
            if p._client_id == client_id
        }
        return [
            c for c in self._claims.values()
            if c._policy_number in client_policy_nums
        ]

    # ---------- Reports ----------
    def generate_summary(self):
        return {
            "clients": len(self._clients),
            "policies": len(self._policies),
            "claims": len(self._claims),
            "active_policies": sum(1 for p in self._policies.values() if p._is_active),
        }
