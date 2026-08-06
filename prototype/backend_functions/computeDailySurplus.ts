/**
 * SOMMER Sovereign Intelligence Architecture
 * Backend Function: computeDailySurplus
 * 
 * December 10th Surplus Computation Engine
 * 
 * Daily task: computes operational savings (non-profit baseline minus
 * actual daily operating cost) and credits the surplus to each citizen's
 * December 10th dividend pool.
 * 
 * Scheduled via Base44 Workflow: daily at 09:00 Europe/Copenhagen
 * 
 * Economics:
 *   - Non-profit baseline: 225 DKK/month (midpoint of 200-250 range)
 *   - Daily baseline: 7.50 DKK/day (225/30)
 *   - Estimated actual operating cost: 5.20 DKK/day
 *   - Daily surplus per citizen: ~2.30 DKK
 * 
 * Deployed at: https://solas-7221afc1.base44.app/functions/computeDailySurplus
 * Runtime: Deno (Base44 backend function)
 */

import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';

Deno.serve(async (req) => {
  try {
    const base44 = createClientFromRequest(req);

    // Load all citizens
    const citizens = await base44.entities.SommerUsers.list({
      filter: { role: 'citizen' }
    });

    // ── Economic Parameters ──
    const NON_PROFIT_BASELINE_DKK = 225;        // midpoint of 200-250 DKK/mo
    const DAILY_BASELINE = NON_PROFIT_BASELINE_DKK / 30;  // ~7.5 DKK/day
    const ESTIMATED_DAILY_OPERATING_COST = 5.2;  // actual cost
    const DAILY_SURPLUS = DAILY_BASELINE - ESTIMATED_DAILY_OPERATING_COST;  // ~2.3 DKK/day

    let updated_count = 0;
    let total_credited = 0;
    let results = [];

    for (const citizen of citizens) {
      const current_surplus = citizen.dec_10_surplus_pool_dkk || 0;
      const new_surplus = current_surplus + DAILY_SURPLUS;

      // Credit the daily surplus to the citizen's Dec 10 pool
      await base44.entities.SommerUsers.update(citizen.id, {
        dec_10_surplus_pool_dkk: Math.round(new_surplus * 100) / 100
      });

      updated_count++;
      total_credited += DAILY_SURPLUS;
      results.push({
        user: citizen.name,
        previous_balance: current_surplus,
        daily_credit: Math.round(DAILY_SURPLUS * 100) / 100,
        new_balance: Math.round(new_surplus * 100) / 100
      });
    }

    return new Response(JSON.stringify({
      date: new Date().toISOString(),
      citizens_updated: updated_count,
      total_credited_dkk: Math.round(total_credited * 100) / 100,
      daily_surplus_per_citizen: Math.round(DAILY_SURPLUS * 100) / 100,
      non_profit_baseline_dkk: NON_PROFIT_BASELINE_DKK,
      actual_daily_operating_cost_dkk: ESTIMATED_DAILY_OPERATING_COST,
      results,
      message: `December 10th surplus pool updated for ${updated_count} citizens. Total credited: ${Math.round(total_credited * 100) / 100} DKK.`
    }), { headers: { 'Content-Type': 'application/json' } });

  } catch (error) {
    return new Response(JSON.stringify({ error: 'Surplus computation error', detail: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
});
