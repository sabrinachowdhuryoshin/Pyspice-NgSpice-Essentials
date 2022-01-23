## Simulation of a Simple Voltage Divider Circuit

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

logger = Logging.setup_logging()

############################################################
# # Make a Circuit with DC Sweep # #
############################################################

# create the circuit
circuit = Circuit('Circuit with DC sweep')

# define the 1N4148PH (signal diode)
circuit.model('MyDiode', 'D', IS=4.352@u_nA, RS=0.6458@u_Ohm, BV=110@u_V, IBV=0.0001@u_V, N=1.906)

# add components to the circuit
circuit.V('i', 'imaginary', circuit.gnd, 10@u_V) # the voltage source i is connected between an imaginary node and gnd
circuit.R(1, 2, circuit.gnd, 1@u_kOhm)
circuit.Diode(1, 1, 2, model='MyDiode')

circuit.B('BS', 1, circuit.gnd, v="v(imaginary)")


# print the circuit:
print("\nThe Circuit/Netlist: \n", circuit)

# create a simulator object (with parameters e.g temp)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# print the circuit + simulator details:
print("The Simulator: \n", simulator)

# run DC sweep analysis
analysis = simulator.dc(Vinput=slice(0, 5, 0.1))
print("Node:", str(analysis["1"]), np.array(analysis["1"]))
print("Node:", str(analysis["2"]), np.array(analysis["2"]))

# plot graph
fig = plt.figure()
plt.plot(np.array(analysis["1"]), np.array(analysis["2"]))
plt.xlabel("Input Voltage (node 1)")
plt.xlabel("Input Voltage (node 2)")
plt.show()

# save graph
my_path = os.path.abspath(__file__) 

# Figures out the absolute path for you in case your working directory moves around
fig.savefig(my_path + '/Sim_Output.png', dpi=300)
plt.close(fig)