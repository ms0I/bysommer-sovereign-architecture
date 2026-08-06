/**
 * Base44 Serverless Function: Planetary Safeguard Webhook Handler
 * Receives external WHO telemetry events and updates Planetary Shield state.
 * 
 * UPDATED (Pass 1 Fixes):
 *   - Uses SDK PascalCase entity name (PlanetaryCouncilTelemetry)
 *   - Restored missing input fields: wastewater_viral_load, pdt_anomaly_rate
 *   - Added missing action map entries: redirect_synth_bio_lines, update_bdt_transit_rules
 *   - Added pdt_anomaly_rate > 15% trigger condition for GLOBAL_DECREE
 */
export async function handlePlanetaryTelemetry(req, res) {
  const {
    source_id,
    r0_vector,
    wastewater_viral_load,
    pdt_anomaly_rate,
    affected_geographies,
    who_authenticated
  } = req.body;

  if (!who_authenticated) {
    return res.status(401).json({ error: "Unauthorized WHO signature." });
  }

  let status = "GREEN";
  let reasons = [];

  // R0 vector threshold checks
  if (r0_vector >= 2.5) {
    status = "GLOBAL_DECREE";
    reasons.push(`R0 vector ${r0_vector} >= 2.5`);
  } else if (r0_vector > 1.0) {
    status = "REGIONAL_WARNING";
    reasons.push(`R0 vector ${r0_vector} > 1.0`);
  }

  // PDT anomaly rate threshold (regional PDT anomaly spike > 15%)
  if (pdt_anomaly_rate !== undefined && pdt_anomaly_rate > 15.0) {
    status = "GLOBAL_DECREE";
    reasons.push(`PDT anomaly rate ${pdt_anomaly_rate}% > 15.0% threshold`);
  }

  // Wastewater viral load monitoring
  if (wastewater_viral_load !== undefined && wastewater_viral_load > 10000) {
    if (status === "GREEN") status = "REGIONAL_WARNING";
    reasons.push(`Wastewater viral load ${wastewater_viral_load} copies/L elevated`);
  }

  // Update Base44 Telemetry Collection (SDK PascalCase entity name)
  const record = await base44.entities.PlanetaryCouncilTelemetry.create({
    alert_status: status,
    pathogen_r0_vector: r0_vector,
    who_approved: who_authenticated,
    affected_geographies: affected_geographies
  });

  // Complete action map per PLANETARY_SHIELD_SPEC
  const actions_triggered = {
    micro_quarantines: status !== "GREEN",
    in_silico_workspace: status !== "GREEN",
    redirect_synth_bio_lines: status === "GLOBAL_DECREE",
    update_bdt_transit_rules: status === "GLOBAL_DECREE"
  };

  return res.status(200).json({
    message: "Planetary Shield state updated.",
    alert_status: status,
    r0_vector: r0_vector,
    wastewater_viral_load: wastewater_viral_load,
    pdt_anomaly_rate: pdt_anomaly_rate,
    reasons: reasons,
    actions_triggered: actions_triggered
  });
}
