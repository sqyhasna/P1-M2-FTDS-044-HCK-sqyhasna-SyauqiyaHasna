import streamlit as st
import pandas as pd
import pickle

with open('P1M2_Syauqiya_Hasna_model.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    st.title('Student Academic Status Prediction')

    with st.form('form_student'):
        marital_status = st.number_input('Marital Status: ', min_value=1, value=1)
        application_mode = st.number_input('Application Mode: ', min_value=1, value=17)
        application_order = st.number_input('Application Order: ', min_value=0, value=1)
        course = st.number_input('Course: ', min_value=1, value=171)
        daytime_evening_attendance = st.selectbox('Daytime Evening Attendance: ', [1, 0])
        previous_qualification = st.number_input('Previous Qualification: ', min_value=1, value=1)
        previous_qualification_grade = st.number_input('Previous Qualification Grade: ', min_value=0.0, value=120.0)
        nationality = st.number_input('Nationality: ', min_value=1, value=1)
        mothers_qualification = st.number_input("Mother's Qualification: ", min_value=1, value=19)
        fathers_qualification = st.number_input("Father's Qualification: ", min_value=1, value=12)
        mothers_occupation = st.number_input("Mother's Occupation: ", min_value=0, value=5)
        fathers_occupation = st.number_input("Father's Occupation: ", min_value=0, value=9)
        admission_grade = st.number_input('Admission Grade: ', min_value=0.0, value=120.0)
        displaced = st.selectbox('Displaced: ', [0, 1])
        educational_special_needs = st.selectbox('Educational Special Needs: ', [0, 1])
        debtor = st.selectbox('Debtor: ', [0, 1])
        tuition_fees_up_to_date = st.selectbox('Tuition Fees Up To Date: ', [1, 0])
        gender = st.selectbox('Gender: ', [0, 1])
        scholarship_holder = st.selectbox('Scholarship Holder: ', [0, 1])
        age_at_enrollment = st.number_input('Age At Enrollment: ', min_value=15, max_value=100, value=20)
        international = st.selectbox('International: ', [0, 1])
        curricular_units_1st_sem_credited = st.number_input('Curricular Units 1st Sem Credited: ', min_value=0, value=0)
        curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled: ', min_value=0, value=6)
        curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations: ', min_value=0, value=6)
        curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved: ', min_value=0, value=5)
        curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade: ', min_value=0.0, value=12.0)
        curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Sem Without Evaluations: ', min_value=0, value=0)
        curricular_units_2nd_sem_credited = st.number_input('Curricular Units 2nd Sem Credited: ', min_value=0, value=0)
        curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled: ', min_value=0, value=6)
        curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations: ', min_value=0, value=6)
        curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved: ', min_value=0, value=5)
        curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade: ', min_value=0.0, value=12.0)
        curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Sem Without Evaluations: ', min_value=0, value=0)
        unemployment_rate = st.number_input('Unemployment Rate: ', value=10.8)
        inflation_rate = st.number_input('Inflation Rate: ', value=1.4)
        gdp = st.number_input('GDP: ', value=1.74)

        submit = st.form_submit_button('Predict')

    data_inf = {
        'marital_status': marital_status,
        'application_mode': application_mode,
        'application_order': application_order,
        'course': course,
        'daytime_evening_attendance': daytime_evening_attendance,
        'previous_qualification': previous_qualification,
        'previous_qualification_grade': previous_qualification_grade,
        'nationality': nationality,
        'mothers_qualification': mothers_qualification,
        'fathers_qualification': fathers_qualification,
        'mothers_occupation': mothers_occupation,
        'fathers_occupation': fathers_occupation,
        'admission_grade': admission_grade,
        'displaced': displaced,
        'educational_special_needs': educational_special_needs,
        'debtor': debtor,
        'tuition_fees_up_to_date': tuition_fees_up_to_date,
        'gender': gender,
        'scholarship_holder': scholarship_holder,
        'age_at_enrollment': age_at_enrollment,
        'international': international,
        'curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
        'curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
        'curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations,
        'curricular_units_2nd_sem_credited': curricular_units_2nd_sem_credited,
        'curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
        'curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations,
        'unemployment_rate': unemployment_rate,
        'inflation_rate': inflation_rate,
        'gdp': gdp
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submit:
        y_pred_inf = model.predict(data_inf)

        result = {
            0: 'Dropout',
            1: 'Enrolled',
            2: 'Graduate'
        }

        st.write('### Prediction: ', result[int(y_pred_inf[0])])

if __name__ == "__main__":
    run()
