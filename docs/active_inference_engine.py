
import math
import time
from typing import Dict, Any, Tuple

class ActiveInferenceEngine:
    """
    3D Spherical Active Inference & Spiking Neural Network (SNN) Event-Gating Core.
    Tracks baseline drift, calculates free energy, and triggers zero-knowledge telemetry flags.
    """
    def __init__(self, user_id: str, decay_rate: float = 0.05):
        self.user_id = user_id
        self.decay_rate = decay_rate
        
        # Internal homeostatic priors (mean, std_dev)
        self.priors: Dict[str, Tuple[float, float]] = {
            "hrv": (55.0, 10.0),       # ms
            "temp": (36.6, 0.3),       # °C
            "resp_rate": (14.0, 2.0),  # breaths/min
            "spo2": (98.5, 1.0)        # %
        }
        
        # SNN Spike Memory Thresholds
        self.membrane_potential = 0.0
        self.spike_threshold = 2.5
        self.refractory_period = False

    def _calculate_feature_kl_divergence(self, obs: float, mean: float, std: float) -> float:
        """Calculates Gaussian log-likelihood penalty (accuracy error)."""
        variance = std ** 2
        return 0.5 * (((obs - mean) ** 2) / variance + math.log(2 * math.pi * variance))

    def compute_free_energy(self, telemetry: Dict[str, float]) -> float:
        """
        Computes Variational Free Energy F across incoming biometric telemetry.
        """
        free_energy = 0.0
        for metric, val in telemetry.items():
            if metric in self.priors:
                mean, std = self.priors[metric]
                free_energy += self._calculate_feature_kl_divergence(val, mean, std)
        return round(free_energy, 4)

    def process_telemetry_event(self, telemetry: Dict[str, float]) -> Dict[str, Any]:
        """
        Evaluates active inference free energy and processes SNN event-gating spike logic.
        """
        free_energy = self.compute_free_energy(telemetry)
        
        # Integrate into membrane potential
        delta_f = max(0.0, free_energy - 2.0)  # Free energy baseline offset
        self.membrane_potential += delta_f
        
        spike_triggered = False
        if self.membrane_potential >= self.spike_threshold:
            spike_triggered = True
            self.membrane_potential = 0.0  # Reset potential post-spike
            
        # Passive leakage decay
        self.membrane_potential = max(0.0, self.membrane_potential - self.decay_rate)
        
        return {
            "user_id": self.user_id,
            "timestamp": time.time(),
            "free_energy_score": free_energy,
            "membrane_potential": round(self.membrane_potential, 3),
            "anomaly_detected": spike_triggered,
            "telemetry_gated": spike_triggered,
            "action_required": "WHO_TELEMETRY_SYNC" if spike_triggered else "HOMEOSTATIC_OK"
        }

# --- Quick Test Execution ---
if __name__ == "__main__":
    engine = ActiveInferenceEngine(user_id="usr_sommer_01")
    
    # Standard homeostatic input
    normal_reading = {"hrv": 54.0, "temp": 36.6, "resp_rate": 14.0, "spo2": 98.0}
    print("Normal Sample:", engine.process_telemetry_event(normal_reading))
    
    # Anomaly/Febrile drift input
    drift_reading = {"hrv": 32.0, "temp": 38.4, "resp_rate": 22.0, "spo2": 95.0}
    print("Drift Sample:", engine.process_telemetry_event(drift_reading))
