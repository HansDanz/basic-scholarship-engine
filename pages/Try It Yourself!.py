from utils.models import Student
from utils.engine import Engine
import streamlit as st

st.title("Check Your Eligibility")

st.write("### Personal Information")

gpa = st.number_input("GPA", min_value=0.0)

credits_completed = st.number_input("Credits Completed", min_value=0)

household_income = st.number_input("Annual Household Income (in USD)", min_value=0)

disciplinary_record = st.checkbox("Have Disciplinary Record")

international_student = st.checkbox("International Student")

mutant_power = st.checkbox("Have Mutant Power")

engine = Engine()

student = Student(
    gpa=gpa,
    credits_completed=credits_completed,
    annual_income_usd=household_income,
    has_disciplinary_record=disciplinary_record,
    is_international_student=international_student,
    has_mutant_power = mutant_power
)

result = engine.evaluate(student)

if result["eligible"]:
    st.write("Outcome: Passed")
else:
    st.write("Outcome: Failed")

st.write("Reasons:")

st.write(result["reasons"])
