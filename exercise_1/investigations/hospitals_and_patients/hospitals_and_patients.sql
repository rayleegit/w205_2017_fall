# hospital and patients query calculate average 'Hospital overall rating'
# for each 'Patient experience national comparison' value

SELECT patient_experience_national_comparison,
  avg(hospital_overall_rating) as avg_rating
FROM hospitals_and_patients
GROUP BY patient_experience_national_comparison
ORDER BY avg_rating DESC;

