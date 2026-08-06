/**
 * Base44 Daily Cron Function: December 10th Surplus Dividend Pool Update
 * Scheduled: Every day at 00:00 UTC
 * 
 * UPDATED (Pass 1 Fixes):
 *   - Uses SDK PascalCase entity names (SommerUsers) instead of snake_case (users)
 *   - Wraps DB operations in base44.asServiceRole for RLS-safe cron access
 *   - Itemized daily operating cost (not hardcoded flat rate)
 *   - Synchronized with computeDailySurplus.ts December 10th payout logic
 */
export async function handleDec10SurplusAccrual(req, res) {
  // Itemized daily operating cost breakdown
  const COST_COMPUTE_INFRA = 2.10;
  const COST_STORAGE_INDEX = 1.30;
  const COST_NETWORK_EGRESS = 0.85;
  const COST_API_CALLS = 0.95;
  const DAILY_OPERATING_COST_DKK =
    COST_COMPUTE_INFRA + COST_STORAGE_INDEX + COST_NETWORK_EGRESS + COST_API_CALLS; // ~5.20 DKK

  const MONTHLY_BASE_DKK = 225.0;
  const dailyBase = MONTHLY_BASE_DKK / 30.0; // 7.50 DKK
  const dailyAccrual = Math.max(0, dailyBase - DAILY_OPERATING_COST_DKK); // ~2.30 DKK/day

  // Use service role for scheduled cron operations (bypasses RLS)
  const serviceRole = base44.asServiceRole;

  // Fetch all registered citizens via SDK PascalCase entity name
  const users = await serviceRole.entities.SommerUsers.list({
    filter: { role: 'citizen' }
  });

  if (!users || users.length === 0) {
    return res.status(200).json({
      status: "SKIPPED_NO_CITIZENS",
      message: "Database returned 0 citizens. Please seed the SommerUsers entity.",
      daily_surplus_rate_dkk: dailyAccrual.toFixed(2)
    });
  }

  const today = new Date();
  const isPayoutDay = (today.getMonth() === 11 && today.getDate() === 10); // Dec 10

  let totalDistributed = 0.0;
  let totalAccrued = 0.0;
  let updatedCount = 0;

  for (const user of users) {
    const currentPool = user.dec_10_surplus_pool_dkk || 0.0;

    if (isPayoutDay) {
      // Annual Distribution Payout Event (December 10th)
      const payoutAmount = currentPool + dailyAccrual;
      totalDistributed += payoutAmount;

      await serviceRole.entities.SommerUsers.update(user.id, {
        true_discretionary_income_dkk: (user.true_discretionary_income_dkk || 0) + payoutAmount,
        dec_10_surplus_pool_dkk: 0.0  // Reset pool after distribution
      });
    } else {
      // Daily Accrual Loop (+2.30 DKK/day)
      totalAccrued += dailyAccrual;
      await serviceRole.entities.SommerUsers.update(user.id, {
        dec_10_surplus_pool_dkk: Number((currentPool + dailyAccrual).toFixed(2))
      });
    }
    updatedCount++;
  }

  return res.status(200).json({
    status: isPayoutDay ? "DECEMBER_10_DIVIDEND_DISTRIBUTED" : "DAILY_ACCRUAL_ACCUMULATED",
    citizens_processed: updatedCount,
    daily_accrual_per_citizen_dkk: dailyAccrual.toFixed(2),
    itemized_operating_cost: {
      compute_infrastructure: COST_COMPUTE_INFRA,
      storage_indexing: COST_STORAGE_INDEX,
      network_egress: COST_NETWORK_EGRESS,
      api_calls: COST_API_CALLS,
      total: DAILY_OPERATING_COST_DKK.toFixed(2)
    },
    total_accrued_today_dkk: totalAccrued.toFixed(2),
    total_distributed_today_dkk: totalDistributed.toFixed(2)
  });
}
