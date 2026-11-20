-- ==========================================
-- 1. BONUS ABUSE & IB CHURNING DETECTION
-- Flags accounts utilizing bonuses with rapid trades (< 2 mins)
-- ==========================================
SELECT 
    login, 
    COUNT(ticket) AS suspicious_trades,
    SUM(volume) AS total_churned_volume,
    SUM(profit_loss) AS net_profit
FROM mt5_trades 
WHERE bonus_utilized = 'Yes' AND duration_minutes < 2.00
GROUP BY login
ORDER BY suspicious_trades DESC
LIMIT 20;

-- ==========================================
-- 2. WASH TRADING / HEDGING DETECTION
-- Flags accounts placing both Buy & Sell on the same symbol
-- with near-zero net PnL (-20 to +20) to generate fake volume
-- ==========================================
SELECT 
    login,
    symbol,
    COUNT(ticket) AS total_trades,
    SUM(volume) AS total_volume,
    SUM(profit_loss) AS net_profit
FROM mt5_trades
GROUP BY login, symbol
HAVING COUNT(DISTINCT type) = 2 
   AND SUM(profit_loss) BETWEEN -20 AND 20
ORDER BY total_volume DESC
LIMIT 10;