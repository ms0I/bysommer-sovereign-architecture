"""
SOMMER Sovereign Architecture - Module 3
December 10th Sovereign Ledger Worker & Surplus Dividend Accrual
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any, List

@dataclass
class OperationalCostProfile:
    monthly_base_fee_dkk: float = 225.0  # Fixed citizen baseline (200-250 DKK/mo)
    actual_serverless_cost_dkk: float = 112.50
    actual_admin_cost_dkk: float = 43.00
    actual_network_bandwidth_dkk: float = 14.50

class Dec10LedgerWorker:
    """
    Computes daily operational savings delta and updates annual December 10th Surplus Dividend pools.
    """
    def __init__(self, target_payout_month: int = 12, target_payout_day: int = 10):
        self.target_month = target_payout_month
        self.target_day = target_payout_day

    def calculate_daily_surplus(self, profile: OperationalCostProfile) -> float:
        """
        Calculates daily non-profit operational surplus:
        Daily Base - Daily Actual Expenditures = Daily Dividend Accrual
        """
        daily_base = profile.monthly_base_fee_dkk / 30.0
        total_monthly_actual = (
            profile.actual_serverless_cost_dkk +
            profile.actual_admin_cost_dkk +
            profile.actual_network_bandwidth_dkk
        )
        daily_actual = total_monthly_actual / 30.0
        
        daily_surplus = max(0.0, daily_base - daily_actual)
        return round(daily_surplus, 4)

    def days_until_payout(self, current_date: date) -> int:
        """Calculates exact days remaining until December 10th."""
        target_year = current_date.year
        target_date = date(target_year, self.target_month, self.target_day)
        
        if current_date > target_date:
            target_date = date(target_year + 1, self.target_month, self.target_day)
            
        return (target_date - current_date).days

    def process_daily_cron(self, user_id: str, current_accumulated_pool_dkk: float, profile: OperationalCostProfile, today: date) -> Dict[str, Any]:
        daily_accrual = self.calculate_daily_surplus(profile)
        updated_pool = round(current_accumulated_pool_dkk + daily_accrual, 2)
        days_left = self.days_until_payout(today)
        is_payout_day = (today.month == self.target_month and today.day == self.target_day)

        return {
            "user_id": user_id,
            "date": today.isoformat(),
            "daily_accrual_dkk": daily_accrual,
            "new_total_pool_dkk": updated_pool,
            "days_until_dec10": days_left,
            "payout_triggered": is_payout_day,
            "payout_amount_dkk": updated_pool if is_payout_day else 0.0,
            "status": "PAYOUT_EXECUTED" if is_payout_day else "ACCUMULATING"
        }

# --- Quick Test Execution ---
if __name__ == "__main__":
    worker = Dec10LedgerWorker()
    costs = OperationalCostProfile()
    sim_date = date(2026, 8, 6) # Aug 6, 2026
    
    res = worker.process_daily_cron(
        user_id="usr_sommer_01",
        current_accumulated_pool_dkk=1240.0,
        profile=costs,
        today=sim_date
    )
    print("Daily Ledger Run:", res)
