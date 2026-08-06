/**
 * Base44 Edge Middleware: BDT+ Symmetrical Rule Matcher
 * 
 * UPDATED (Pass 1 Fixes):
 *   - Uses SDK PascalCase entity name (BdtTransactions) instead of snake_case
 *   - Fixed field names to match entity schema: total_amount_dkk, vat_rate_applied
 *   - Added missing fields: buyer_id, business_id, timestamp
 */
export async function handleBDTTransaction(req, res) {
  const { transaction_id, buyer_id, business_id, items, is_cross_border, is_ioss_registered, current_maint_spend } = req.body;

  const DANISH_VAT = 0.25;
  const FLAT_DUTY_EUR = 3.0; // 2026 EU Customs Reform rate
  const EUR_TO_DKK = 7.46;
  const CAP_LIMIT_DKK = 250.0;

  // 1. CE Check
  const uncertifiedItem = items.find(i => !i.ce_marked && i.country_of_origin !== 'EU');
  if (uncertifiedItem) {
    await base44.entities.BdtTransactions.create({
      buyer_id: buyer_id || null,
      business_id: business_id || null,
      compliance_status: 'BLOCKED_MISSING_CE',
      total_amount_dkk: items.reduce((acc, i) => acc + i.price_dkk, 0),
      vat_rate_applied: DANISH_VAT,
      timestamp: new Date().toISOString()
    });

    return res.status(400).json({
      status: 'BLOCKED_MISSING_CE',
      reason: `CE Marking mandatory. Blocked item: ${uncertifiedItem.description}`
    });
  }

  // 2. Compute Totals
  const subtotal = items.reduce((acc, i) => acc + i.price_dkk, 0);
  const vat = subtotal * DANISH_VAT;
  
  const hsCodes = new Set(items.map(i => i.hs_code));
  const duty = is_cross_border ? (hsCodes.size * FLAT_DUTY_EUR * EUR_TO_DKK) : 0;
  
  const finalTotal = subtotal + vat + duty;
  const status = is_cross_border && !is_ioss_registered ? 'PENDING_IOSS' : 'VALIDATED';

  // 3. Record Validated Transaction (schema-compliant field names)
  await base44.entities.BdtTransactions.create({
    buyer_id: buyer_id || null,
    business_id: business_id || null,
    compliance_status: status,
    total_amount_dkk: finalTotal,
    vat_rate_applied: DANISH_VAT,
    timestamp: new Date().toISOString()
  });

  return res.status(200).json({
    status: status,
    subtotal_dkk: subtotal.toFixed(2),
    vat_dkk: vat.toFixed(2),
    duty_dkk: duty.toFixed(2),
    total_final_dkk: finalTotal.toFixed(2)
  });
}
