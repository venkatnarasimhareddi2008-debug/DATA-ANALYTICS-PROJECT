--loyalty score assigning
WITH GlobalConstants AS (

    SELECT 
        MAX(PREVIOUS_PURCHASES) AS max_prev_purchases,
        MAX(PURCHASE_AMOUNT) AS max_purchase_amount
    FROM DATA
),
ComponentCalculations AS (
    SELECT 
        c.CUSTOMER_ID,
        c.CATEGORY,
        c.LOCATION,
        c.PREVIOUS_PURCHASES,
        
        (c.PREVIOUS_PURCHASES::FLOAT / gc.max_prev_purchases) AS repeat_score,
        
        CASE 
            WHEN LOWER(c.FREQUENCY_OF_PURCHASES) = 'weekly' THEN 1.0
            WHEN LOWER(c.FREQUENCY_OF_PURCHASES) = 'fortnightly' THEN 0.8
            WHEN LOWER(c.FREQUENCY_OF_PURCHASES) = 'monthly' THEN 0.6
            WHEN LOWER(c.FREQUENCY_OF_PURCHASES) = 'quarterly' THEN 0.3
            ELSE 0.1 
        END AS frequency_score,

        CASE WHEN UPPER(c.SUBSCRIPTION_STATUS) = 'YES' THEN 1.0 ELSE 0.0 END AS subscription_score,
        
        (c.PURCHASE_AMOUNT::FLOAT / gc.max_purchase_amount) AS spending_score,
        
        CASE WHEN UPPER(c.DISCOUNT_APPLIED) = 'YES' THEN 1.0 ELSE 0.0 END AS discount_dependency
        
    FROM data c, GlobalConstants gc
),
FinalTCSCalculation AS (
  
    SELECT 
        CUSTOMER_ID,
        CATEGORY,
        LOCATION,
        PREVIOUS_PURCHASES,
        repeat_score,
        spending_score,
        discount_dependency,
        (
            (0.30 * repeat_score) + 
            (0.25 * frequency_score) + 
            (0.20 * subscription_score) + 
            (0.15 * spending_score) - 
            (0.10 * discount_dependency)
        ) AS raw_tcs_score
    FROM ComponentCalculations
)
SELECT 
    CUSTOMER_ID,
    CATEGORY,
    LOCATION,
    PREVIOUS_PURCHASES,
    ROUND(raw_tcs_score::NUMERIC, 3) AS tcs_loyalty_score,
    CASE 
        WHEN raw_tcs_score >= 0.60 THEN 'True Loyal Customer'
        WHEN raw_tcs_score >= 0.40 THEN 'Semi-Loyal'
        WHEN raw_tcs_score >= 0.20 THEN 'Discount Sensitive'
        ELSE 'Sale-Only Customer'
    END AS customer_type
FROM FinalTCSCalculation
ORDER BY tcs_loyalty_score DESC;



WITH RegionalMetrics AS (
    SELECT 
        LOCATION,
        COUNT(CUSTOMER_ID) AS total_transactions,
        SUM(PURCHASE_AMOUNT) AS total_revenue,
  
        SUM(CASE WHEN UPPER(DISCOUNT_APPLIED) = 'YES' THEN 1 ELSE 0 END)::FLOAT 
            / COUNT(CUSTOMER_ID) AS promo_volume_share
    FROM DATA
    GROUP BY LOCATION
)

--checking market type
SELECT 
    LOCATION,
    total_transactions,
    ROUND(total_revenue::NUMERIC, 2) AS total_revenue,
    ROUND((promo_volume_share * 100)::NUMERIC, 1) AS promo_dependency_pct,
    
    CASE 
        WHEN promo_volume_share <= 0.30 THEN 'Organic Stronghold (Genuine Pull)'
        WHEN promo_volume_share > 0.30 AND promo_volume_share <= 0.47 THEN 'Stable Balanced Market'
        ELSE 'Promotion Dependent (Danger Zone)'
    END AS market_demand_type
FROM RegionalMetrics
ORDER BY total_revenue DESC;


--seasons and categories associated
SELECT 
    SEASON,
    CATEGORY,
    COUNT(CUSTOMER_ID) AS total_orders,
 
    AVG(PREVIOUS_PURCHASES) AS avg_previous_purchases
FROM DATA
GROUP BY SEASON, CATEGORY
ORDER BY SEASON, avg_previous_purchases ASC;




SELECT 
    GENDER,
    CATEGORY,
    COUNT(CUSTOMER_ID) AS total_orders,
  
    AVG(PREVIOUS_PURCHASES) AS avg_repeat_count
FROM DATA
GROUP BY GENDER, CATEGORY
ORDER BY avg_repeat_count DESC;