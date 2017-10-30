# hospital variability: transform 'Timely and Effective Care - Hospital' table
# 'Score' field from 'string' to 'int'

CREATE TABLE hospital_variability AS
SELECT hospital_name, measure_name, cast(score as INT) as score
FROM effective_care;

