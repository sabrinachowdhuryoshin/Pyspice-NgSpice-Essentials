## Simulation of a Simple Voltage Divider Circuit

import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

logger = Logging.setup_logging()

# create the circuit
circuit = Circuit('Voltage Divider')

# add components to the circuit
circuit.V('input', 'in', circuit.gnd, 10@u_V)
circuit.R(1, 'in', 'out', 9@u_kOhm)
circuit.R(2, 'out', circuit.gnd, 1@u_kOhm)

# create a simulator object (with parameters e.g temp)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# print the circuit:
print("\nThe Circuit/Netlist: \n", circuit)

exit()

