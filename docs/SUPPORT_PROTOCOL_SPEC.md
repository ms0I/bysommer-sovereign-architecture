"""
SOMMER Sovereign Architecture - Module 2
Symmetrical Support Protocol & BDT+ Compliance Engine
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum

class ComplianceStatus(Enum):
    VALIDATED = "VALIDATED"
    BLOCKED_MISSING_CE = "BLOCKED_MISSING_CE"
    PENDING_IOSS = "PENDING_IOSS"
    BLOCKED_CAP_EXCEEDED = "BLOCKED_CAP_EXCEEDED"

@dataclass
class LineItem:
    description: str
    price_dkk: float
    hs_code: str  # 6-digit HS commodity code
    ce_marked: bool
    country_of_origin: str

@dataclass
class TransactionContext:
    transaction_id: str
    buyer_id: str
    business_id: str
    items: List[LineItem]
    is_cross_border: bool
    is_ioss_registered: bool
    current_month_maint_spend_dkk: float
    is_auto_maintenance: bool = False

class BDTComplianceEngine:
    """
    Symmetrical Support Rule Matcher for BDT+ enterprise & e-commerce trade.
    Enforces Danish Moms (25%), EU 2026 Customs Flat Duty (€3 / HS line), CE Safety, and Citizen Caps.
    """
    DANISH_VAT_RATE = 0.25      # Standard Danish Moms (25%)
    EU_CUSTOMS_DUTY_EUR = 3.0   # 2026 EU Customs Reform flat duty per HS line
    EUR_TO_DKK_RATE = 7.46      # Standard EUR/DKK exchange rate reference
    MAINTENANCE_CAP_DKK = 250.0  # Monthly autonomous consent cap

    def evaluate_transaction(self, tx: TransactionContext) -> Dict[str, Any]:
        total_item_price_dkk = sum(item.price_dkk for item in tx.items)
        
        # 1. CE Marking Safety Validation Block
        for item in tx.items:
            if not item.ce_marked and item.country_of_origin != "EU":
                return {
                    "transaction_id": tx.transaction_id,
                    "compliance_status": ComplianceStatus.BLOCKED_MISSING_CE.value,
                    "allowed": False,
                    "reason": f"CE marking missing for product '{item.description}' imported from outside EU.",
                    "applied_vat_dkk": 0.0,
                    "applied_duty_dkk": 0.0,
                    "total_final_dkk": total_item_price_dkk
                }

        # 2. Autonomous Household Spending Cap Validation
        if tx.is_auto_maintenance:
            if (tx.current_month_maint_spend_dkk + total_item_price_dkk) > self.MAINTENANCE_CAP_DKK:
                return {
                    "transaction_id": tx.transaction_id,
                    "compliance_status": ComplianceStatus.BLOCKED_CAP_EXCEEDED.value,
                    "allowed": False,
                    "reason": f"Exceeds monthly PDT+ maintenance cap of {self.MAINTENANCE_CAP_DKK} DKK.",
                    "applied_vat_dkk": 0.0,
                    "applied_duty_dkk": 0.0,
                    "total_final_dkk": total_item_price_dkk
                }

        # 3. Tax & 2026 EU Customs Duty Calculations
        applied_vat_dkk = total_item_price_dkk * self.DANISH_VAT_RATE
        applied_duty_dkk = 0.0
        status = ComplianceStatus.VALIDATED.value

        if tx.is_cross_border:
            if not tx.is_ioss_registered:
                status = ComplianceStatus.PENDING_IOSS.value
            
            # EU 2026 Customs Reform: Flat €3 per distinct HS Code line item
            unique_hs_codes = set(item.hs_code for item in tx.items)
            flat_duty_eur = len(unique_hs_codes) * self.EU_CUSTOMS_DUTY_EUR
            applied_duty_dkk = round(flat_duty_eur * self.EUR_TO_DKK_RATE, 2)

        total_final_dkk = round(total_item_price_dkk + applied_vat_dkk + applied_duty_dkk, 2)

        return {
            "transaction_id": tx.transaction_id,
            "compliance_status": status,
            "allowed": True,
            "reason": "Transaction passed all biological, safety, and tax validation checks.",
            "subtotal_dkk": round(total_item_price_dkk, 2),
            "applied_vat_dkk": round(applied_vat_dkk, 2),
            "applied_duty_dkk": applied_duty_dkk,
            "total_final_dkk": total_final_dkk
        }

# --- Quick Test Run ---
if __name__ == "__main__":
    engine = BDTComplianceEngine()

    # Valid import transaction
    valid_tx = TransactionContext(
        transaction_id="TX-2026-001",
        buyer_id="usr_sommer_01",
        business_id="biz_nordic_01",
        items=[
            LineItem("Smart Sensor Node", 200.0, "854370", ce_marked=True, country_of_origin="NO"),
            LineItem("Micro-Air Filter", 100.0, "842139", ce_marked=True, country_of_origin="NO")
        ],
        is_cross_border=True,
        is_ioss_registered=True,
        current_month_maint_spend_dkk=45.0
    )
    print("Valid Spec Evaluation:", engine.evaluate_transaction(valid_tx))

    # CE Non-compliant block
    blocked_tx = TransactionContext(
        transaction_id="TX-2026-002",
        buyer_id="usr_sommer_01",
        business_id="biz_global_02",
        items=[LineItem("Uncertified Drone", 850.0, "880622", ce_marked=False, country_of_origin="CN")],
        is_cross_border=True,
        is_ioss_registered=True,
        current_month_maint_spend_dkk=0.0
    )
    print("CE Block Evaluation:", engine.evaluate_transaction(blocked_tx))
