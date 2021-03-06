## Simulation of a Simple Voltage Divider Circuit

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import PySpice
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

logger = Logging.setup_logging()
############################################################
# # Make a Circuit with a Diode # #
############################################################

# create the circuit
circuit = Circuit('Circuit with a Diode')
libraries_path = find_libraries()
spice_library = SpiceLibrary(libraries_path)

# add components to the circuit
circuit.V('input', 1, circuit.gnd, 10@u_V)
circuit.R(1, 2, circuit.gnd, 1@u_kOhm)

# # method 0: locally defined
# # define the 1N4148 (signal diode)
# circuit.model('MyDiode', 'D', IS=4.352@u_nA, RS=0.6458@u_Ohm, BV=110@u_V, IBV=0.0001@u_V, N=1.906)
# circuit.Diode(1, 1, 2, model='MyDiode')

# method 1: 
# use circuit.include() from the pyspice functions
circuit.include(spice_library['1N4148'])
circuit.X('importDiode', '1N4148', 1, 2)

# # method 2: 
# # use circuit.include() from the pyspice functions
# new_line = ".include lib\1N4148.lib"
# circuit.raw_spice += new_line + os.linesep
# circuit.X('importDiode', '1N4148', 1, 2)

# print the circuit:
# print("\nThe Circuit/Netlist: \n", circuit)

# create a simulator object (with parameters e.g temp)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# print the circuit + simulator details:
print("The Simulator: \n", simulator)

# run DC sweep analysis
analysis = simulator.dc(Vinput=slice(-4, 4, 0.01))  # slice = start:step:stop (inclusive)

# plot graph
fig = plt.figure()
plt.plot(np.array(analysis["1"]), np.array(analysis["2"]))
plt.xlabel("Input Voltage (node 1)")
plt.ylabel("Output Voltage (node 2)")
plt.show()
