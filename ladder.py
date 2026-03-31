
import numpy as np

def ladder_impedance(Rs, Rp, Cp, steps, freq):

    """
    Calculates the equivalent impedance of a ladder circuit with a parallel capacitor.
    
    :param Rs: Series resistance (Ω)
    :param Rp: Parallel resistance (Ω)
    :param Cp: Parallel capacitance (F)
    :param steps: Number of ladder steps
    :param freq: Frequency (Hz)
    :return: Equivalent impedance (complex value)
    """
    omega = 2 * np.pi * freq  # Angular frequency
    Xp = 1 / (1j * omega * Cp)
    Zp = Rp * Xp / (Rp + Xp)

  #  Zp = 1 / ((1 / Rp) + (1j * omega * Cp))  # Parallel impedance formula

    if steps == 0:
        return 0  # No impedance if there are no steps
    if steps == 1:
        return Rs + Zp

    # Impedance of parallel branch: Rp || Cp
    # Recursive formula: Zeq = Rs + (Zp * Zeq_next) / (Zp + Zeq_next)
    Z_next = ladder_impedance(Rs, Rp, Cp, steps - 1, freq)
    Zeq = Rs + (Zp * Z_next) / (Zp + Z_next)

    return Zeq

def equivalent_capacitance(Zeq, freq):
    """
    Calculates the equivalent capacitance from the impedance.

    :param Zeq: Equivalent impedance (complex value)
    :param freq: Frequency (Hz)
    :return: Equivalent capacitance (F)
    """

    omega = 2 * np.pi * freq  # Angular frequency
    Im_Zeq = Zeq.imag  # Extract imaginary part

    if Im_Zeq == 0:
        return None  # No capacitive component

    Ceq = -1 / (omega * Im_Zeq)  # Compute equivalent capacitance
    return Ceq

       # Example Usage
Rs = 12.3e-3      # Series resistor (Ω)
Rp = 58e-3      # Parallel resistor (Ω)
Cp = 1.34e-9    # Parallel capacitor (1 µF)
steps = 10   # Number of ladder steps
freq = 1000  # Frequency (Hz)
 
Zeq = ladder_impedance(Rs, Rp, Cp, steps, freq)
Ceq = equivalent_capacitance(Zeq, freq)

print(f"Equivalent Impedance at {freq} Hz: {Zeq:.5f} Ω")
print(f"Equivalent Capacitance at {freq} Hz: {Ceq:.6f} F")
