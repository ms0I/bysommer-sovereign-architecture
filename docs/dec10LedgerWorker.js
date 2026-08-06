/**
 * Base44 Daily Cron Function: December 10th Surplus Dividend Pool Update
 * Scheduled: Every day at 00:00 UTC
 */
export async function handleDec10SurplusAccrual(req, res) {
  const MONTHLY_BASE_DKK = 225.0;
  const DAILY_OPERATING_COST_DKK = 5.20; // Verified current actual daily cost
  
  const dailyBase = MONTHLY_BASE_DKK / 30.0; // 7.50 DKK
  const dailyAccrual = Math.max(0, dailyBase - DAILY_OPERATING_COST_DKK); // 2.30 DKK/day

  // Fetch all registered citizens
  const users = await base44.db.users.findMany();
  
  if (!users || users.length === 0) {
    return res.status(200).json({
      status: "SKIPPED_NO_USERS",
      message: "Database returned 0 users. Please seed the 'users' collection.",
      daily_surplus_rate_dkk: dailyAccrual.toFixed(2)
    });
  }

  const today = new Date();
  const isPayoutDay = (today.getMonth() === 11 && today.getDate() === 10); // Dec 10

  let totalDistributed = 0.0;
  let updatedCount = 0;

  for (const user of users) {
    const currentPool = user.dec_10_surplus_pool_dkk || 0.0;

    if (isPayoutDay) {
      // Annual Distribution Payout Event
      const payoutAmount = currentPool + dailyAccrual;
      totalDistributed += payoutAmount;

      await base44.db.users.update(user.id, {
        true_discretionary_income_dkk: (user.true_discretionary_income_dkk || 0) + payoutAmount,
        dec_10_surplus_pool_dkk: 0.0
      });
    } else {
      // Daily Accrual Loop (+2.30 DKK/day)
      await base44.db.users.update(user.id, {
        dec_10_surplus_pool_dkk: Number((currentPool + dailyAccrual).toFixed(2))
      });
    }
    updatedCount++;
  }

  return res.status(200).json({
    status: isPayoutDay ? "DECEMBER_10_DIVIDEND_DISTRIBUTED" : "DAILY_ACCRUAL_ACCUMULATED",
    citizens_processed: updatedCount,
    daily_accrual_per_citizen_dkk: dailyAccrual.toFixed(2),
    total_distributed_today_dkk: totalDistributed.toFixed(2)
  });
}
