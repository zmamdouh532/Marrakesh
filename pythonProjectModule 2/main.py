class DiagramCommunication:
    def __init__(self):

        self.project_stakeholder1 = input("Enter the project stakeholder1: ")
        self.project_stakeholder2 = input("Enter the project stakeholder2: ")
        self.project_stakeholder3 = input("Enter the project stakeholder3: ")
        self.project_stakeholder4 = input("Enter the project stakeholder4: ")
        self.system_1 = input("Enter the system 1: ")
        self.system_2 = input("Enter the system 2: ")

    def get_communication(self):
        communication = {
            "Project stakeholder1": self.project_stakeholder1,
            "project stakeholder2": self.project_stakeholder2,
            "project stakeholder3": self.project_stakeholder3,
            "project stakeholder4": self.project_stakeholder4,
            "system 1": self.system_1,
            "system 2": self.system_2,
        }
        return communication

    def __str__(self):
        return f"""
Diagram Elements:
    Project stakeholder1: {self.project_stakeholder1}
    project stakeholder2: {self.project_stakeholder2}
    project stakeholder3: {self.project_stakeholder3}
    project stakeholder4: {self.project_stakeholder4}
    system 1: {self.system_1}
    system 2: {self.system_2}
"""


# Create an instance of the class and get the elements
diagram_communication = DiagramCommunication()
communication = diagram_communication.get_communication()

# Print the communication in a well-formatted output
print(diagram_communication)


