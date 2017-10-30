# best states: transform 'HCAHPS' table 'hcahps_consistency_score' field
# from 'string' to 'int'

CREATE TABLE best_states AS
SELECT hospital_name, state, cast(hcahps_consistency_score as INT) as hcahps_consistency_score
FROM survey_responses;

