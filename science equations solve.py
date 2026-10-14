# Python can be used to solve some complex scientific equations. Here is an example of solving a relativistic momentum equation using Python.

import numpy as np

# Define physical constants and variables
m = 9.109e-31  # mass of an electron (kg)
v = 1.0e8      # velocity (m/s)
c = 3.0e8      # speed of light (m/s)

# Translate the formula: p = (m * v) / sqrt(1 - (v^2 / c^2))
p = (m * v) / np.sqrt(1 - (v**2 / c**2))
f = (m * v) / ((1 - (v**2 / c**2)) ** 0.5)


print(f"Relativistic momentum: {p} kg·m/s")
print(f"Relativistic momentum (alternative calculation): {f} kg·m/s")


# Here is another example of calculating the force exerted by a bicep during a pushup, taking into account various physical factors.

import numpy as np # numpy has no use in the following code but it is imported for future use in case we want to use numpy functions for calculations.

def calculate_extreme_bicep_force(
    weight_kg=40, 
    height_m=1.62, 
    velocity_mps=1, 
    mu_floor=0.6, 
    num_ions=650
):
    # 1. Macroscopic Constants
    g = 9.80665              # Acceleration due to gravity (m/s^2)
    rho_air = 1.225          # Air density at sea level (kg/m^3)
    Cd_human = 1.0           # Drag coefficient of a human torso
    A_torso = 0.5            # Frontal surface area facing the floor (m^2)
    
    # 2. Microscopic / Electrostatic Constants
    e_charge = 1.602e-19     # Elementary charge of an ion (Coulombs)
    k_coulomb = 8.98755e9    # Coulomb's constant (N·m^2/C^2)
    r_cellular_distance = 1e-8 # Average distance between cell & floor boundaries (10 nm)

    # --- Calculations ---
    
    # Force 1: Gravity & Weight
    F_gravity = weight_kg * g
    # Hands bear ~70% of weight during the peak phase
    F_normal_hands = F_gravity * 0.70 
    
    # Force 2: Air Resistance (Fluid Drag)
    F_air_drag = 0.5 * rho_air * (velocity_mps ** 2) * Cd_human * A_torso
    
    # Force 3: Floor Friction (Horizontal equilibrium stabilizer)
    F_friction = mu_floor * F_normal_hands
    
    # Force 4: Electrostatic Ion Interactions 
    # Net charge assuming a minor uncompensated ionic polar imbalance at the surface
    total_charge_hands = num_ions * e_charge
    total_charge_floor = num_ions * e_charge
    F_electrostatic = (k_coulomb * total_charge_hands * total_charge_floor) / (r_cellular_distance ** 2)
    
    # Total effective vertical ground reaction force acting on the hands
    # Electrostatic forces act at atomic distances; drag opposes upward velocity
    F_total_hands = F_normal_hands + F_air_drag + F_electrostatic
    
    # 3. Biomechanical Leverage
    # Moment arm of the forearm length (~0.25m) vs Bicep tendon insertion (~0.04m)
    forearm_length = 0.25
    bicep_insertion_arm = 0.04
    
    # Total mechanical torque required at the elbow joint
    Torque_elbow = F_total_hands * forearm_length
    
    # Raw total force required by the arm flexor/extensor complex
    F_arm_complex = Torque_elbow / bicep_insertion_arm
    
    # 4. Bicep Isolation Factor
    # The bicep acts as an antagonist stabilizer during a pushup, taking roughly 7% of the load
    bicep_activation_ratio = 0.07
    F_bicep = F_arm_complex * bicep_activation_ratio
    
    return {
        "Gravity Force (Total Weight)": round(F_gravity, 4),
        "Air Drag Force": round(F_air_drag, 6),
        "Floor Friction Force": round(F_friction, 4),
        "Cellular Ionic Electrostatic Force": F_electrostatic,
        "Total Force Applied by Bicep": round(F_bicep, 4)
    }

# Execute calculation for a standard person
results = calculate_extreme_bicep_force()

for factor, value in results.items():
      print(f"{factor}: {value} Newtons")



for item, value in calculate_extreme_bicep_force().items():
    print(f"{item}: {value} Newtons")


# If pushup is done at very high velocity then:

# Keep your 40 kg weight completely constant, but do the pushup at 500 m/s
extreme_results = calculate_extreme_bicep_force(weight_kg=40, velocity_mps=500)

print(f"New Bicep Force: {extreme_results['Total Force Applied by Bicep']} Newtons")





import math


def relativistic_momentum(m, v, c=299792458):
  """Calculates the relativistic momentum of an object.

    m: rest mass in kilograms
    v: velocity in meters per second
    c: speed of light in meters per second (default is 299,792,458 m/s)
    """
  gamma = 1.0 / math.sqrt(1.0 - (v**2 / c**2))
  return gamma * m * v


# Below is another example of using the relativistic momentum function to calculate the momentum of an object moving at a significant fraction of the speed of light.

# Example: 1 kg object moving at half the speed of light
mass = 1.0  # kg
velocity = 0.5 * 299792458  # 0.5c in m/s

p = relativistic_momentum(mass, velocity)
print(f"Relativistic momentum: {p:.2f} kg·m/s")

