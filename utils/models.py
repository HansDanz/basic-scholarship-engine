class Student:
    def __init__(self, gpa, credits_completed, annual_income_usd, has_disciplinary_record, is_international_student, has_mutant_power):
        self._gpa = gpa
        self._credits_completed = credits_completed
        self._annual_income_usd = annual_income_usd
        self._has_disciplinary_record = has_disciplinary_record
        self._is_international_student = is_international_student
        self._has_mutant_power = has_mutant_power
    
    @property
    def gpa(self):
        return self._gpa
    
    @property
    def credits_completed(self):
        return self._credits_completed
    
    @property
    def annual_income_usd(self):
        return self._annual_income_usd
    
    @property
    def has_disciplinary_record(self):
        return self._has_disciplinary_record
    
    @property
    def is_international_student(self):
        return self._is_international_student   
    
    @property
    def has_mutant_power(self):
        return self._has_mutant_power  