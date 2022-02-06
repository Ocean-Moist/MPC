from template_model import template_model
from template_mpc import template_mpc
from template_simulator import template_simulator

model = template_model()
mpc = template_mpc(model)
sim =  template_simulator(model)

# initial states


while True:

