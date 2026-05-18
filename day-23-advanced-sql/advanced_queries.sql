SELECT
    risk_level,
    COUNT(*) AS community_count,
    AVG(diabetes_rate) AS average_diabetes_rate
FROM community_risk
GROUP BY risk_level
ORDER BY average_diabetes_rate DESC;