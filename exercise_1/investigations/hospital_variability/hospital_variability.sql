# hospital variability query to summarize range of
# 'Timely and Effective Care - Hospital' table 'Score' field

SELECT DISTINCT measure_name, max(score) - min(score) as range
FROM hospital_variability
GROUP BY measure_name
ORDER BY range DESC;

