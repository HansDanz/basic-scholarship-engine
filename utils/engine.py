print("Loaded engine.py from:", __file__)

from .rules import MinimumGPARule, MinimumCreditsRule, MaximumIncomeRule, DisciplinaryRecordRule, MutantPowerRule

class Engine:
    def evaluate(self,student):
        reasons = []
        result = {
            "eligible": True,
            "reasons": []
        }       
        rules = [MinimumGPARule(), MinimumCreditsRule(), MaximumIncomeRule(), DisciplinaryRecordRule(), MutantPowerRule()]
        for rule in rules:
            passed, reason = rule.evaluate(student)
            result["reasons"].append(reason)
            if not passed:
                result["eligible"] = False
        return result