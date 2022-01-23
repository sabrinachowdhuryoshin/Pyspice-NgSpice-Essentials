## Simulation of Circuit with Current Dependent Voltage Source

import  PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit('Circuit with CCVS')
circuit.R(1, 1, 2, 2@u_Ω)
circuit.R(2, 2, circuit.gnd, 20@u_Ω)
circuit.R(3, 2, 3, 5@u_Ω)
circuit.R(4, 4, circuit.gnd, 10@u_Ω)
circuit.R(5, 4, 5, 2@u_Ω)
circuit.V(1, 1, circuit.gnd, 20@u_V)
circuit.V('test', 3, 4, 0@u_V)
circuit.H(1, 5, circuit.gnd, 'Vtest', 8)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()
for node in analysis.nodes.values(): 
    print('Node {}: {:4.1f} V'.format(str(node), float(node)))

for node in analysis.branches.values(): 
    print('Node {}: {:5.2f} A'.format(str(node), float(node))) 