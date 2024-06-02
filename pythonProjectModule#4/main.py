"""
Mamdouh Zayed
"""
from abc import ABC, abstractmethod

# Abstract Builder class
class DeveloperBuilder(ABC):
  @abstractmethod
  def set_communication_skills(self, communication_skills):
      pass

  @abstractmethod
  def set_problem_solving_skills(self, problem_solving_skills):
      pass

  @abstractmethod
  def set_teamwork_skills(self, teamwork_skills):
      pass

  @abstractmethod
  def get_developer(self):
      pass

# Director class
class DeveloperDirector:
  @staticmethod
  def build_developer(builder):
      builder.set_communication_skills("ExpertCommunication")
      builder.set_problem_solving_skills("ExpertProblemSolving")
      builder.set_teamwork_skills("ExpertTeamwork")

# Concrete Builder class
class DeveloperBuilderImpl(DeveloperBuilder):
  def __init__(self):
      self.developer = Developer()

  def set_communication_skills(self, communication_skills):
      self.developer.communication_skills = communication_skills

  def set_problem_solving_skills(self, problem_solving_skills):
      self.developer.problem_solving_skills = problem_solving_skills

  def set_teamwork_skills(self, teamwork_skills):
      self.developer.teamwork_skills = teamwork_skills

  def get_developer(self):
      return self.developer

# Product class
class Developer:
  def __init__(self):
      self.communication_skills = None
      self.problem_solving_skills = None
      self.teamwork_skills = None

  def __str__(self):
      return f"Communication Skills: {self.communication_skills}\n" \
             f"Problem-Solving Skills: {self.problem_solving_skills}\n" \
             f"Teamwork Skills: {self.teamwork_skills}"

def main():
  builder = DeveloperBuilderImpl()
  director = DeveloperDirector()
  director.build_developer(builder)
  developer = builder.get_developer()
  print(developer)

if __name__ == "__main__":
  main()
