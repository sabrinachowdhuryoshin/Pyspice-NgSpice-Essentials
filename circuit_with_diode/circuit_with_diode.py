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

    return sim_res_dict

############################################################
# # Make a Circuit with a Diode # #
############################################################

# create the circuit
circuit = Circuit('Circuit with a Diode')

# define the 1N4148PH (signal diode)
circuit.model('MyDiode', 'D', IS=4.352@u_nA, RS=0.6458@u_Ohm, BV=110@u_V, IBV=0.0001@u_V, N=1.906)

# add components to the circuit
circuit.V('input', 1, circuit.gnd, 10@u_V)
circuit.R(1, 1, 2, 9@u_kOhm)
circuit.R(2, 3, circuit.gnd, 1@u_kOhm)
circuit.Diode(1, 2, 3, model='MyDiode')
circuit.Diode(2, 3, circuit.gnd, model='MyDiode')

# print the circuit:
print("\nThe Circuit/Netlist: \n", circuit)

# # create a simulator object (with parameters e.g temp)
# simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# # print the circuit + simulator details:
# print("The Simulator: \n", simulator)

# # run analysis
# analysis = simulator.operating_point()
# out_dict = format_output(analysis)
# print(out_dict)