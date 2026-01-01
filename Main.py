import streamlit as st
import pandas as pd

st.image("xaviers_school.jpg", caption="Xavier's Institute for Gifted Youngsters")

st.title("Charles Xavier Excellence Scholarship")

st.write("The rigour at Xavier's Institute for Gifted Children are unlike any other. While normal students your age fret about math tests, students here are always on the lookout of evil mutant attacks, home invasions by the CIA, and the occasional world-ending event. We can't give you back your childhood but we can pay you, assuming you fit the criteria.")

st.write("### Eligibility Criteria")

st.markdown("""
- Minimum GPA of 3.5 (3.7 for international students)
- Minimum 60 credits completed
- Annual household income of 50000 USD (for those still with houses)
- Has no disciplinary record (mind control not counted)
""")

st.write("### Sample Students")

st.write("Sample 1: Scott Summers")

scott = pd.DataFrame(
    {
        "Criteria Met?": [4.0, "No", 70, "$0", "No", "Yes"]

    },
    index=[
        "GPA",
        "International Student",
        "Credits Completed",
        "Annual Household Income",
        "Has Disciplinary Record",
        "Has Mutant Power"]
)
st.table(scott)

st.write("Outcome: Passed")

st.divider() 

st.write("Sample 2: Peter Parker")

peter = pd.DataFrame(
    {
        "Criteria Met?": [5.3, "No", 75, "$200", "No", "No"]

    },
    index=[
        "GPA",
        "International Student",
        "Credits Completed",
        "Annual Household Income",
        "Has Disciplinary Record",
        "Has Mutant Power"]
)
st.table(peter)

st.write("Outcome: Failed")

st.divider() 

st.write("Sample 3: Emma Frost")

emma = pd.DataFrame(
    {
        "Criteria Met?": [4.0, "Yes", 70, "$22000000", "Yes", "Yes"]

    },
    index=[
        "GPA",
        "International Student",
        "Credits Completed",
        "Annual Household Income",
        "Has Disciplinary Record",
        "Has Mutant Power"]
)
st.table(emma)

st.write("Outcome: Failed")