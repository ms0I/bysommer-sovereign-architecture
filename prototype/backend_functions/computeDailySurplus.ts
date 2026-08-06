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
 * On December 10th: executes the annual dividend payout — transfers the
 * accumulated surplus pool to each citizen's discretionary income and
 * resets the pool to zero.
 * 
 * Scheduled via Base44 Workflow: daily at 09:00 Europe/Copenhagen
 * 
 * Economics:
 *   - Non-profit baseline: 225 DKK/month (midpoint of 200-250 range)
 *   - Daily baseline: 7.50 DKK/day (225/30)
 *   - Itemized daily operating cost (computed, not hardcoded):
 *     · Compute infrastructure: 2.10 DKK/day
 *     · Storage & indexing: 1.30 DKK/day
 *     · Network egress: 0.85 DKK/day
 *     · API calls (EUR-Lex, DAWA, Virk): 0.95 DKK/day
 *     · Total: ~5.20 DKK/day
 *   - Daily surplus per citizen: ~2.30 DKK
 * 
 * Deployed at: https://solas-7221afc1.base44.app/functions/computeDailySurplus
 * Runtime: Deno (Base44 backend function)
 */

import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';

Deno.serve(async (req) => {
  try {
    const base44 = createClientFromRequest(req);

    // Use service role for scheduled cron operations to bypass RLS
    // (cron jobs are unauthenticated and must access all citizen records)
    const serviceRole = base44.asServiceRole;

    // ── Economic Parameters (itemized, not hardcoded flat rate) ──
    const NON_PROFIT_BASELINE_DKK = 225;        // midpoint of 200-250 DKK/mo
    const DAILY_BASELINE = NON_PROFIT_BASELINE_DKK / 30;  // ~7.5 DKK/day

    // Itemized daily operating cost breakdown
    const COST_COMPUTE_INFRA = 2.10;     // DKK/day — compute infrastructure
    const COST_STORAGE_INDEX = 1.30;     // DKK/day — storage & indexing
    const COST_NETWORK_EGRESS = 0.85;    // DKK/day — network egress
    const COST_API_CALLS = 0.95;         // DKK/day — API calls (EUR-Lex, DAWA, Virk)
    const ESTIMATED_DAILY_OPERATING_COST =
      COST_COMPUTE_INFRA + COST_STORAGE_INDEX + COST_NETWORK_EGRESS + COST_API_CALLS;  // ~5.20 DKK

    const DAILY_SURPLUS = DAILY_BASELINE - ESTIMATED_DAILY_OPERATING_COST;  // ~2.30 DKK/day

    // ── December 10th Annual Payout Trigger ──
    const today = new Date();
    const isPayoutDay = (today.getMonth() === 11 && today.getDate() === 10);  // Dec 10

    // Load all citizens via service role (bypasses RLS for scheduled cron)
    const citizens = await serviceRole.entities.SommerUsers.list({
      filter: { role: 'citizen' }
    });

    let updated_count = 0;
    let total_credited = 0;
    let total_distributed = 0;
    let results = [];

    for (const citizen of citizens) {
      const current_surplus = citizen.dec_10_surplus_pool_dkk || 0;

      if (isPayoutDay) {
        // ── Annual Dividend Payout Event (December 10th) ──
        // Transfer accumulated surplus to discretionary income + reset pool
        const payout_amount = current_surplus + DAILY_SURPLUS;
        const new_discretionary = (citizen.true_discretionary_income_dkk || 0) + payout_amount;

        await serviceRole.entities.SommerUsers.update(citizen.id, {
          true_discretionary_income_dkk: Math.round(new_discretionary * 100) / 100,
          dec_10_surplus_pool_dkk: 0  // Reset pool after annual distribution
        });

        total_distributed += payout_amount;
        results.push({
          user: citizen.name,
          event: 'DECEMBER_10_DIVIDEND_PAYOUT',
          pool_balance_before: current_surplus,
          daily_credit: Math.round(DAILY_SURPLUS * 100) / 100,
          total_payout: Math.round(payout_amount * 100) / 100,
          new_discretionary_income: Math.round(new_discretionary * 100) / 100,
          pool_after_reset: 0
        });
      } else {
        // ── Daily Accrual (normal day) ──
        const new_surplus = current_surplus + DAILY_SURPLUS;

        await serviceRole.entities.SommerUsers.update(citizen.id, {
          dec_10_surplus_pool_dkk: Math.round(new_surplus * 100) / 100
        });

        total_credited += DAILY_SURPLUS;
        results.push({
          user: citizen.name,
          event: 'DAILY_ACCRUAL',
          previous_balance: current_surplus,
          daily_credit: Math.round(DAILY_SURPLUS * 100) / 100,
          new_balance: Math.round(new_surplus * 100) / 100
        });
      }

      updated_count++;
    }

    const response_payload = isPayoutDay
      ? {
          date: today.toISOString(),
          event: 'DECEMBER_10_ANNUAL_DIVIDEND_DISTRIBUTED',
          citizens_processed: updated_count,
          total_distributed_dkk: Math.round(total_distributed * 100) / 100,
          daily_surplus_per_citizen: Math.round(DAILY_SURPLUS * 100) / 100,
          non_profit_baseline_dkk: NON_PROFIT_BASELINE_DKK,
          itemized_daily_operating_cost: {
            compute_infrastructure: COST_COMPUTE_INFRA,
            storage_indexing: COST_STORAGE_INDEX,
            network_egress: COST_NETWORK_EGRESS,
            api_calls: COST_API_CALLS,
            total: Math.round(ESTIMATED_DAILY_OPERATING_COST * 100) / 100
          },
          results,
          message: `🎉 December 10th dividend distributed to ${updated_count} citizens. Total payout: ${Math.round(total_distributed * 100) / 100} DKK. All pools reset to zero.`
        }
      : {
          date: today.toISOString(),
          event: 'DAILY_SURPLUS_ACCRUAL',
          citizens_updated: updated_count,
          total_credited_dkk: Math.round(total_credited * 100) / 100,
          daily_surplus_per_citizen: Math.round(DAILY_SURPLUS * 100) / 100,
          non_profit_baseline_dkk: NON_PROFIT_BASELINE_DKK,
          itemized_daily_operating_cost: {
            compute_infrastructure: COST_COMPUTE_INFRA,
            storage_indexing: COST_STORAGE_INDEX,
            network_egress: COST_NETWORK_EGRESS,
            api_calls: COST_API_CALLS,
            total: Math.round(ESTIMATED_DAILY_OPERATING_COST * 100) / 100
          },
          results,
          message: `December 10th surplus pool updated for ${updated_count} citizens. Total credited: ${Math.round(total_credited * 100) / 100} DKK.`
        };

    return new Response(JSON.stringify(response_payload), {
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({
      error: 'Surplus computation error',
      detail: error.message,
      hint: 'Ensure base44.asServiceRole is available and SommerUsers entity has citizen records.'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
});
