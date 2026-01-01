print("Loaded rules.py from:", __file__)
print("Defined symbols:", dir())

from abc import ABC, abstractmethod
class Rule(ABC):
    @abstractmethod
    def evaluate(self, student):
        pass

class MinimumGPARule(Rule):
    def evaluate(self, student):
        if student.is_international_student:
            required_GPA = 3.7
        else:
            required_GPA = 3.5
        if student.gpa >= required_GPA:
            return True, "GPA satisfies required threshold"
        else:
            return False, "GPA below required threshold"

class MinimumCreditsRule(Rule):
    def evaluate(self, student):
        if student.credits_completed >= 60:
            return True, "Credits satisfy required threshold"
        else:
            return False, "Credits below required threshold"

class MaximumIncomeRule(Rule):
    def evaluate(self, student):
        if student.annual_income_usd <= 50000:
            return True, "Household income within limit"
        else:
            return False, "Household income above limit"

class DisciplinaryRecordRule(Rule):
    def evaluate(self, student):
        if student.has_disciplinary_record:
            return False, "Has disciplinary record"
        else:
            return True, "Has no disciplinary record"
        
class MutantPowerRule(Rule):
    def evaluate(self, student):
        if student.has_mutant_power:
            return True, "Has mutant power"
        else:
            return False, "Has no mutant power"