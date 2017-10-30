# best hospitals query

SELECT hospital_name, hcahps_consistency_score
FROM best_hospitals
WHERE hcahps_consistency_score = 20
ORDER BY hcahps_consistency_score ASC;

