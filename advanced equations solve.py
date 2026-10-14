import numpy as np


def calculate_bicep_force_multi_velocity(
    weight_kg=40,
    height_m=1.62,
    velocities_mps=np.linspace(0, 500, 50),  # 50 velocities from 0 to 500 m/s


    # In the given code the sequence from 0 to 500 with total 50 terms is an arithmetic progression with a common difference of 10.204081632653061. This means that each subsequent term in the sequence is obtained by adding this common difference to the previous term. The sequence starts at 0 and ends at 500, with a total of 50 terms, and the values are evenly spaced across this range.





    mu_floor=0.6,
    num_ions=650,
):

    """In the AP above the calculations for common difference and all terms is as following:

    The formula for the nth term of an arithmetic progression (AP) is given by : An = A1 + (n - 1) * d, where:
    An = nth term
    A1 = first term
    n = number of terms
    d = common difference

    Given values:
• First term A1 = 0
• Last term An = 500
• Total elements (n): 50
Plugging these into the formula:

500 = 0 + (50 - 1) * d
500 = 49 * d
500 / 49 = d
d ≈ 10.204081632653061

Now second term = A2 = A1 + d = 0 + 10.204081632653061 ≈ 10.204081632653061

and Second-to-Last Term A49 = A1 + (49 - 1) * d = 0 + 48 * 10.204081632653061 ≈ 489.7959183673469:
     
 """
    # 1. Macroscopic Constants
    g = 9.80665  # Acceleration due to gravity (m/s^2)
    rho_air = 1.225  # Air density at sea level (kg/m^3)
    Cd_human = 1.0  # Drag coefficient

    # Height-based scaling (Biomechanical dynamic adaptation)
    forearm_length = height_m * 0.155  # ~15.5% of total height
    A_torso = 0.5 * (height_m / 1.62)  # Scaled frontal area

    # 2. Microscopic / Electrostatic Constants
    e_charge = 1.602e-19  # Elementary charge (C)
    k_coulomb = 8.98755e9  # Coulomb's constant (N·m^2/C^2)
    r_cellular_distance = 1e-8  # Separation distance (10 nm)

    # --- Calculations ---

    # Force 1: Gravity & Weight
    F_gravity = weight_kg * g
    F_normal_hands = F_gravity * 0.70  # 70% supported by hands

    # Force 2: Air Resistance (Fluid Drag calculated for ALL velocities simultaneously)
    # velocities_mps is a NumPy array, so (velocities_mps ** 2) computes element-wise
    F_air_drag = 0.5 * rho_air * (velocities_mps**2) * Cd_human * A_torso

    # Force 3: Floor Friction
    F_friction = mu_floor * F_normal_hands

    # Force 4: Electrostatic Ion Interaction
    total_charge = num_ions * e_charge
    F_electrostatic = (k_coulomb * (total_charge**2)) / (
        r_cellular_distance**2
    )

    # Total effective force on hands across all velocities
    F_total_hands = F_normal_hands + F_air_drag + F_electrostatic

    # 3. Biomechanical Leverage
    bicep_insertion_arm = 0.04  # Tendon distance from joint (m)
    Torque_elbow = F_total_hands * forearm_length
    F_arm_complex = Torque_elbow / bicep_insertion_arm

    # 4. Bicep Isolation Force
    bicep_activation_ratio = 0.07
    F_bicep = F_arm_complex * bicep_activation_ratio

    return {
        "velocities": velocities_mps,
        "air_drag": F_air_drag,
        "bicep_force": F_bicep,
    }


# Execute calculation across multiple velocities
results = calculate_bicep_force_multi_velocity(
    weight_kg=40,
    height_m=1.62,
    #velocities_mps=np.array([0,3,52,....]),  # Specific array of speeds in m/s.It can be  used when we want to give the specific values and not the range of values.
)

# Print results using a loop over zipped NumPy arrays
for v, drag, force in zip(
    results["velocities"], results["air_drag"], results["bicep_force"]
):
    print(
        f"Velocity: {v:>3} m/s | Air Drag: {drag:>10.2f} N | Bicep Force: {force:>10.2f} N"
    )