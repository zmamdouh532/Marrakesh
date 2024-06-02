"""
Mamdouh Zayed
"""
class Pothole:
    def __init__(self, street_address, size, location, district):
        self.id = None  # Assigned by the system
        self.street_address = street_address
        self.size = size
        self.location = location
        self.district = district
        self.repair_priority = None  # Assigned by the system

class WorkOrder:
    def __init__(self, pothole, crew_id, num_people, equipment, hours_applied, status, filler_material_used):
        self.pothole = pothole
        self.crew_id = crew_id
        self.num_people = num_people
        self.equipment = equipment
        self.hours_applied = hours_applied
        self.status = status
        self.filler_material_used = filler_material_used
        self.cost_of_repair = self.calculate_cost()
        # Print work order
        self.print()

    def calculate_cost(self) -> object:
        # Implement cost calculation logic based on hours, people, material, etc.
        return 25 * self.hours_applied * self.num_people * 100 if self.equipment else 1 * self.filler_material_used
    def print(self):
        print("Printing work order: ")
        print("Number of people: ", self.num_people)
        print("status: ", self.status)
        print("equipment: ", self.equipment)
        print("crew_id: ", self.crew_id)
        print("hours_applied: ", self.hours_applied)
        print("cost_of_repair: ", self.cost_of_repair)

class DamageReport:
    def __init__(self, citizen_name, address, phone_number, damage_type, dollar_amount):
        self.citizen_name = citizen_name
        self.address = address
        self.phone_number = phone_number
        self.damage_type = damage_type
        self.dollar_amount = dollar_amount
        # self.print()
        self.print()

    def print(self):
        print("citizen_name: ", self.citizen_name)
        print("address: ", self.address)
        print("phone_number: ", self.phone_number)
        print("damage_type: ", self.damage_type)
        print("dollar_amount: ", self.dollar_amount)

class PHTRSSystem:
    def __init__(self):
        self.potholes = []
        self.work_orders = []
        self.damage_reports = []

    def report_pothole(self, street_address, size, location, district):
        pothole = Pothole(street_address, size, location, district)
        # Generate and assign ID and repair priority
        pothole.id = len(self.potholes) + 1
        pothole.repair_priority = self.calculate_repair_priority(size)
        self.potholes.append(pothole)
        print("Pothole on: ", street_address)# Print pothole
        print("size: ", size)
        print("location: ", location)
        print("district: ", district)
        return pothole

    def assign_work_order(self, pothole, crew_id, num_people, equipment, hours_applied, status, filler_material_used):
        work_order = WorkOrder(pothole, crew_id, num_people, equipment, hours_applied, status, filler_material_used)
        self.work_orders.append(work_order)
        return work_order

    def report_damage(self, citizen_name, address, phone_number, damage_type, dollar_amount):
        damage_report = DamageReport(citizen_name, address, phone_number, damage_type, dollar_amount)
        self.damage_reports.append(damage_report)
        return damage_report

    def calculate_repair_priority(self, size):
        # Implement repair priority calculation logic based on the size of the pothole
        if size > 7: return "High priority"
        elif size > 3:  return "Middle priority"
        else: return "Low priority"

# Example usage:
phtrs_system = PHTRSSystem()
pothole = phtrs_system.report_pothole("123 Main St", 8, "middle", "District A\n")
work_order = phtrs_system.assign_work_order(pothole, "Crew001", 3, 100, 8, "Work in Progress", 5)
print("\n")
damage_report = phtrs_system.report_damage("Mamdouh Zayed", "456 Oak St", "509-555-1234", "Flat tire", 100)



