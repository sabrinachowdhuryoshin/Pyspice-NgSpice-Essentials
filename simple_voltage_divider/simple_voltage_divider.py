## Simulation of a Simple Voltage Divider Circuit

import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

logger = Logging.setup_logging()

# function

def format_output(analysis):
    '''
    Gets dictionary containing SPICE sim values.
    The dictionary is created by pairing each of the nodes to its corresponding 
    output voltage value array. 
    This provides a more manageable format.
    '''
# create dictionary
sim_res_dict = {}

# loop through each nodes
for node in analysis.nodes.values():

        # extract node name
        data_label = "%s" % str(node)

        # save node value/ array of values
        sim_res_dict[data_label] = np.array(node)

# create the circuit
circuit = Circuit('Voltage Divider')

# add components to the circuit
circuit.V('input', 'in', circuit.gnd, 10@u_V)
circuit.R(1, 'in', 'out', 9@u_kOhm)
circuit.R(2, 'out', circuit.gnd, 1@u_kOhm)

# print the circuit:
print("\nThe Circuit/Netlist: \n", circuit)

# create a simulator object (with parameters e.g temp)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# print the circuit + simulator details:
print("The Simulator: \n", simulator)

# run analysis
analysis = simulator.operating_point()
out_dict = format_output(analysis)
print(out_dict)

