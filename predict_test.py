#!/usr/bin/env python
# coding: utf-8



import requests


url = 'http://localhost:9696/predict'



patient = { 
            "program_category": "outpatient",
            "age_group": "adult",
            "sex": "male",
            "sexual_orientation": "straight_or_heterosexual",
            "transgender": "no,_not_transgender",
            "living_situation": "private_residence",
            "veteran_status": "no",
            "employment_status": "not_in_labor_force:unemployed_and_not_looking_for_work",
            "number_of_hours_worked_each_week": "not_applicable",
            "educational_status": "middle_school_to_high_school",
            "special_educational_services": "not_applicable",
            "mental_illness": "yes",
            "intellectual_disability": "no",
            "autism_spectrum": "no",
            "other_developmental_disabilities": "no",
            "alcohol_related_disorder": "no",
            "drug_substance_related_disorder": "yes",
            "mobility_impairment_disorder": "no",
            "hearing_visual_impairment": "no",
            "hyperlipidemia": "no",
            "high_blood_pressure": "yes",
            "diabetes": "no",
            "obesity": "no",
            "heart_attack": "no",
            "stroke": "no",
            "other_cardiac": "no",
            "pulmonary/asthma": "no",
            "alzheimer_or_dementia": "no",
            "kidney_disease": "no",
            "liver_disease": "no",
            "endocrine_condition": "no",
            "neurological_condition": "no",
            "traumatic_brain_injury": "no",
            "joint_disease": "yes",
            "cancer": "no",
            "no_chronic_med._condition": "no",
            "unknown_chronic_med._condition": "no",
            "smokes": "no",
            "receives_smoking_medication": "no",
            "receives_smoking_counseling": "no",
            "serious_mental_illness": "yes",
            "principal_diagnosis_class": "mental_illness",
            "additional_diagnosis_class": "substance-related_disorder",
            "criminal_justice_status": "no"
            }



response = requests.post(url, json=patient).json()
response



if response['insurance_status'] == True:
    print(f"Probability that the patient has insurance is  : {response['Insurance applicability']}")
    print("Medical insurance coverage has been provided.")
else:
    print(f"Probability that the patient has insurance is  : {response['Insurance applicability']}")
    print("No insurance coverage has been provided")
