SELECT COUNT(*) AS total_trips
FROM trips;
SELECT ROUND(SUM(total_amount), 2) AS total_revenue
FROM trips;
SELECT
    ROUND(AVG(fare_amount), 2) AS avg_fare,
    ROUND(AVG(trip_distance), 2) AS avg_distance
FROM trips;
SELECT
    "PULocationID",
    COUNT(*) AS trip_count
FROM trips
GROUP BY "PULocationID"
ORDER BY trip_count DESC
LIMIT 10;
SELECT
    "DOLocationID",
    COUNT(*) AS trip_count
FROM trips
GROUP BY "DOLocationID"
ORDER BY trip_count DESC
LIMIT 10;
SELECT
    payment_type,
    COUNT(*) AS count
FROM trips
GROUP BY payment_type
ORDER BY count DESC;
SELECT
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour,
    COUNT(*) AS trips
FROM trips
GROUP BY hour
ORDER BY trips DESC;