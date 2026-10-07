# Group Members:
# Mulisa Docile
# Daniel Obar
# Abi Mirembe
# Flavia Sherinah
# Victoria Marvis
# Mordecai Corey Kwezi 

from system import InsuranceSystem
from validators import (
    ask_text, ask_name, ask_phone, ask_email,
    ask_positive_float, ask_positive_int,
    ask_policy_dates, ask_claim_date,
)


def main_menu():
    print("\n===== INSURANCE POLICY & CLAIMS SYSTEM =====")
    print("1. Clients")
    print("2. Policies")
    print("3. Claims")
    print("4. Reports & Summary")
    print("0. Exit")
    return input("Select option: ").strip()


def clients_menu(system):
    while True:
        print("\n--- CLIENTS ---")
        print("1. Register new client")
        print("2. List all clients")
        print("3. View one client")
        print("0. Back to Main Menu")
        choice = input("Select option: ").strip()

        try:
            if choice == "1":
                name = ask_name("Name: ")
                phone = ask_phone("Phone: ")
                email = ask_email("Email: ")
                client = system.register_client(name, phone, email)
                print(f"Registered: {client}")
            elif choice == "2":
                clients = system.list_clients()
                if not clients:
                    print("No clients yet.")
                else:
                    for c in clients:
                        print(c)
            elif choice == "3":
                cid = ask_text("Client ID (e.g. C001): ", "Client ID")
                client = system.get_client(cid)
                print(client if client else "Client not found.")
            elif choice == "0":
                break
            else:
                print("Unknown option. Try again.")
        except ValueError as e:
            print(f"Error: {e}")


def policies_menu(system):
    while True:
        print("\n--- POLICIES ---")
        print("1. Create Motor policy")
        print("2. Create Health policy")
        print("3. Create Property policy")
        print("4. View policies for a client")
        print("5. Calculate premium for a policy")
        print("0. Back to Main Menu")
        choice = input("Select option: ").strip()
        try:
            if choice == "1":
                cid = ask_text("Client ID: ", "Client ID")
                start, end = ask_policy_dates()
                reg = ask_text("Vehicle registration: ", "Vehicle registration")
                value = ask_positive_float("Vehicle value (UGX): ", "Vehicle value")
                vtype = ask_text("Vehicle type: ", "Vehicle type")
                policy = system.create_motor_policy(
                    cid, start, end, reg, value, vtype)
                print(f"Created: {policy.get_details()}")

            elif choice == "2":
                cid = ask_text("Client ID: ", "Client ID")
                start, end = ask_policy_dates()
                age = ask_positive_int("Age: ", "Age", minimum=18, maximum=100)
                level = ask_text("Coverage level (Basic/Standard/Premium): ",
                                "Coverage level")
                level_title = level.title()
                if level_title not in ("Basic", "Standard", "Premium"):
                    print("Coverage level should be Basic, Standard or Premium. "
                          "Using your entry as given.")
                else:
                    level = level_title
                policy = system.create_health_policy(
                    cid, start, end, age, level)
                print(f"Created: {policy.get_details()}")

            elif choice == "3":
                cid = ask_text("Client ID: ", "Client ID")
                start, end = ask_policy_dates()
                address = ask_text("Property address: ", "Property address")
                value = ask_positive_float("Property value (UGX): ", "Property value")
                ptype = ask_text("Property type: ", "Property type")
                policy = system.create_property_policy(
                    cid, start, end, address, value, ptype)
                print(f"Created: {policy.get_details()}")

            elif choice == "4":
                cid = ask_text("Client ID: ", "Client ID")
                policies = system.get_client_policies(cid)
                if not policies:
                    print("No policies for this client.")
                else:
                    for p in policies:
                        print(p.get_details())

            elif choice == "5":
                pnum = ask_text("Policy number: ", "Policy number")
                policy = system.get_policy(pnum)
                if policy is None:
                    print("Policy not found.")
                else:
                    # polymorphic call — works for any subclass
                    premium = policy.calculate_premium()
                    print(f"Premium: UGX {premium:,.0f}")

            elif choice == "0":
                break
            else:
                print("Unknown option. Try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


def claims_menu(system):
    while True:
        print("\n--- CLAIMS ---")
        print("1. Record a claim")
        print("2. Update claim status")
        print("3. View claims for a policy")
        print("4. View claims for a client")
        print("0. Back to Main Menu")
        choice = input("Select option: ").strip()

        try:
            if choice == "1":
                pnum = ask_text("Policy number: ", "Policy number")
                policy = system.get_policy(pnum)
                if policy is None:
                    print(f"Policy {pnum} does not exist.")
                    continue
                amount = ask_positive_float("Claim amount (UGX): ", "Claim amount")
                desc = ask_text("Description: ", "Description")
                claim_date = ask_claim_date(policy)
                claim = system.record_claim(pnum, amount, desc, claim_date)
                print(f"Recorded: {claim}")
            elif choice == "2":
                cid = ask_text("Claim ID: ", "Claim ID")
                print("Allowed: Pending, Approved, Rejected, Paid")
                new_status = ask_text("New status: ", "Status")
                system.update_claim_status(cid, new_status)
                print("Status updated.")
            elif choice == "3":
                pnum = ask_text("Policy number: ", "Policy number")
                claims = system.get_claims_for_policy(pnum)
                if not claims:
                    print("No claims for this policy.")
                else:
                    for c in claims:
                        print(c)
            elif choice == "4":
                client_id = ask_text("Client ID: ", "Client ID")
                claims = system.get_claims_for_client(client_id)
                if not claims:
                    print("No claims for this client.")
                else:
                    for c in claims:
                        print(c)
            elif choice == "0":
                break
            else:
                print("Unknown option. Try again.")
        except ValueError as e:
            print(f"Error: {e}")


def reports_menu(system):
    while True:
        print("\n--- REPORTS & SUMMARY ---")
        print("1. System summary")
        print("2. List all policies (with premiums)")
        print("0. Back to Main Menu")
        choice = input("Select option: ").strip()
        if choice == "1":
            s = system.generate_summary()
            print(f"Clients: {s['clients']}")
            print(f"Policies: {s['policies']} (active: {s['active_policies']})")
            print(f"Claims: {s['claims']}")
        elif choice == "2":
            policies = system.list_policies()
            if not policies:
                print("No policies yet.")
            else:
                for p in policies:
                    prem = p.calculate_premium()  # polymorphism
                    print(f"{p.get_details()} => UGX {prem:,.0f}")
        elif choice == "0":
            break
        else:
            print("Unknown option. Try again.")


def run_app():
    system = InsuranceSystem()
    while True:
        choice = main_menu()
        if choice == "1":
            clients_menu(system)
        elif choice == "2":
            policies_menu(system)
        elif choice == "3":
            claims_menu(system)
        elif choice == "4":
            reports_menu(system)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Unknown option. Please try again.")


if __name__ == "__main__":
    run_app()
