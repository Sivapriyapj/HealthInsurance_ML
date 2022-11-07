#!/usr/bin/env python
# coding: utf-8

# ## Training the final model

# ### Import libraries

print("Importing libraries")

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import auc,roc_auc_score,roc_curve
import pickle


# ### Read data
print("Reading data")



df = pd.read_csv('patient-characteristics-survey-pcs-2013-1.csv')



df.columns = df.columns.str.lower().str.replace(' ','_')
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] =df[c].str.lower().str.replace(' ','_')
categorical_columns


cols = ['program_category','age_group','sex','sexual_orientation','transgender','living_situation','veteran_status','employment_status',
       'number_of_hours_worked_each_week','educational_status',
       'special_educational_services', 'mental_illness',
       'intellectual_disability', 'autism_spectrum',
       'other_developmental_disabilities', 'alcohol_related_disorder',
       'drug_substance_related_disorder', 'mobility_impairment_disorder',
       'hearing_visual_impairment','hyperlipidemia', 'high_blood_pressure',
       'diabetes', 'obesity', 'heart_attack', 'stroke', 'other_cardiac',
       'pulmonary/asthma', 'alzheimer_or_dementia', 'kidney_disease',
       'liver_disease', 'endocrine_condition', 'neurological_condition',
       'traumatic_brain_injury', 'joint_disease', 'cancer',
       'no_chronic_med._condition', 'unknown_chronic_med._condition', 'smokes',
       'receives_smoking_medication', 'receives_smoking_counseling',
       'serious_mental_illness', 'principal_diagnosis_class',
       'additional_diagnosis_class','no_insurance','criminal_justice_status']


df = df[cols]


for i in cols:
    df = df[df[i] != "unknown"]
    



categorical= ['program_category','sexual_orientation','living_situation','employment_status','number_of_hours_worked_each_week','educational_status','special_educational_services','principal_diagnosis_class','additional_diagnosis_class','intellectual_disability','other_developmental_disabilities','mobility_impairment_disorder',
       'hearing_visual_impairment','age_group','sex','transgender','veteran_status','mental_illness','intellectual_disability','autism_spectrum','other_developmental_disabilities','alcohol_related_disorder','drug_substance_related_disorder','mobility_impairment_disorder','hearing_visual_impairment','hyperlipidemia','high_blood_pressure','diabetes','obesity','heart_attack','stroke','other_cardiac','pulmonary/asthma','alzheimer_or_dementia','kidney_disease','liver_disease','endocrine_condition','neurological_condition','traumatic_brain_injury','joint_disease','cancer','no_chronic_med._condition','unknown_chronic_med._condition','smokes','receives_smoking_medication','receives_smoking_counseling','serious_mental_illness','criminal_justice_status']




df.no_insurance = (df.no_insurance=="no").astype(int)


# ### Train_test split

print("Training the model")

df_full_train,df_test = train_test_split(
    df,
    test_size=0.2,
    random_state=1,
)
df_train,df_val = train_test_split(
    df_full_train,
    test_size=0.25,
    random_state=1,
)



len(df_full_train),len(df_train),len(df_test),len(df_val)



df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)



y_train = df_train.no_insurance.values

y_val = df_val.no_insurance.values

y_test = df_test.no_insurance.values



del df_train['no_insurance']
del df_val['no_insurance']
del df_test['no_insurance']



df_full_train.reset_index(drop =True)
df_full_train.isnull().sum()


dv = DictVectorizer(sparse=False)



train_dicts = df_train[categorical].to_dict(orient='records')
val_dicts = df_val[categorical].to_dict(orient='records')



X_train = dv.fit_transform(train_dicts)
X_val = dv.transform(val_dicts)


# ### Training the final model - XG Boost


dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=dv.feature_names_)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=dv.feature_names_)



watchlist = [(dtrain, 'train'), (dval, 'val')]



xgb_params_Final = {
    'eta': 0.05,
    'max_depth': 9,
    'min_child_weight': 10,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    'seed': 1,
}

model_Final = xgb.train(xgb_params_Final, dtrain,
                  num_boost_round=170, verbose_eval=10,
                  evals=watchlist)



y_pred_finalmodel = model_Final.predict(dval)
y_pred_finalmodel[:10]


print("Calculation AUC")

roc_auc_score(y_val, y_pred_finalmodel)


# ### Saving the model

output_file ='model_Final.bin'


print("Saving the model")

f_out = open(output_file,'wb')
pickle.dump((df_test,y_test,dv,model_Final),f_out)
f_out.close()


# ### Loading the model










