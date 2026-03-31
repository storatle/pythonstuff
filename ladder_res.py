def ladder_resistance(Rs, Rp, steps):
    """
    Calculates the equivalent resistance of a ladder circuit.

    :param Rs: Series resistance
    :param Rp: Parallel resistance
    :param steps: Number of ladder steps
    :return: Equivalent resistance of the ladder network
    """
    if steps == 0:
        return 0  # No resistance if there are no steps
    elif steps == 1:
        return Rs + Rp  # Base case: Single step

    # Recursive formula: Req = Rs + (Rp * Req_next) / (Rp + Req_next)
    Req_next = ladder_resistance(Rs, Rp, steps - 1)
    return Rs + (Rp * Req_next) / (Rp + Req_next)

# Example Usage
Rs = 18.45e-3  # Series resistor (Ω)
Rp = 29e-3  # Parallel resistor (Ω)
steps = 5  # Number of ladder steps

Req = ladder_resistance(Rs, Rp, steps)
print(f"Equivalent Resistance of {steps}-step Ladder Circuit: {Req:.6f} Ω")
