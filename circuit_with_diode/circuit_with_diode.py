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