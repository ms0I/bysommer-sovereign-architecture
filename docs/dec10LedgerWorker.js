/**
 * Base44 Daily Cron Function: December 10th Surplus Dividend Pool Update
 * Scheduled: Every day at 00:00 UTC
 */
export async function handleDec10SurplusAccrual(req, res) {
  const MONTHLY_BASE_DKK = 225.0;
  const ACTUAL_MONTHLY_COST_DKK = 170.0; // Serverless + Network + Infrastructure
  
  const dailyBase = MONTHLY_BASE_DKK / 30.0;
  const dailyActual = ACTUAL_MONTHLY_COST_DKK / 30.0;
  const dailyAccrual = Math.max(0, dailyBase - dailyActual);

  const users = await base44.db.users.findMany();
  const today = new Date();
  const isPayoutDay = (today.getMonth() === 11 && today.getDate() === 10); // Dec 10

  for (const user of users) {
    const newPool = (user.dec_10_surplus_pool_dkk || 0) + dailyAccrual;

    if (isPayoutDay) {
      // Execute non-profit distribution to citizen discretionary balance
      await base44.db.users.update(user.id, {
        true_discretionary_income_dkk: (user.true_discretionary_income_dkk || 0) + newPool,
        dec_10_surplus_pool_dkk: 0.0
      });
    } else {
      // Accumulate daily dividend
      await base44.db.users.update(user.id, {
        dec_10_surplus_pool_dkk: Number(newPool.toFixed(2))
      });
    }
  }

  return res.status(200).json({
    status: isPayoutDay ? "DECEMBER_10_DIVIDEND_PAID" : "DAILY_ACCRUAL_COMPLETED",
    accrued_today_dkk: dailyAccrual.toFixed(4),
    processed_users: users.length
  });
}
