# best states query

SELECT state, count(*) state_count
FROM best_states
WHERE hcahps_consistency_score = 20
GROUP BY state
ORDER by state_count DESC;

