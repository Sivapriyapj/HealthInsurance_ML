
### test dataset
#(df_test.iloc[0]).to_dict()
from flask import Flask,request,jsonify
import pickle
import xgboost as xgb



input_file = 'model_Final.bin'
f_in = open(input_file,'rb')
df_test,y_test,dv,model_Final = pickle.load(f_in)
f_in.close()


df_test,y_test,dv, model_Final

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



app = Flask('Health_Insurance_checker')
@app.route('/predict', methods=['POST'])

def predict():
    patient = request.get_json()

    X = dv.transform([patient])
    X_value = xgb.DMatrix(X, label = y_test, feature_names=dv.feature_names_)

    y_pred = model_Final.predict(X_value)
    insurance_status = y_pred >= 0.5
    result = {
        "Insurance applicability" : float(y_pred),
        "insurance_status" : bool(insurance_status)
    }
    return jsonify(result)


if __name__ == "__main__":   
    app.run(debug=True, host= '0.0.0.0', port=9696)