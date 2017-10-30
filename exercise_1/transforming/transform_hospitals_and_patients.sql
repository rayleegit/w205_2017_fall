# hospitals and patients: transform 'Hospital General Information' table
# 'Hospital overall rating' from 'string' to 'int'

CREATE TABLE hospitals_and_patients AS
SELECT hospital_name,
  cast(hospital_overall_rating as INT) as hospital_overall_rating,
  patient_experience_national_comparison
FROM hospitals;

