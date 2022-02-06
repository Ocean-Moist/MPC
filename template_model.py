import do_mpc
import numpy as np

def template_model():
     # Define the model

    model_type = 'continuous'
    model = do_mpc.model.Model(model_type)

    # wheel radius
    r = 0.1254  # 6 in to m

    # radius of rotation/wheelbase
    l = 0.69  # 27 in to m

    theta = model.set_variable(var_type='_x', var_name='theta', shape=(1,1))

    x_dot = model.set_variable(var_type='_x', var_name='x_dot', shape=(1,1))
    y_dot = model.set_variable(var_type='_x', var_name='y_dot', shape=(1,1))
    theta_dot = model.set_variable(var_type='_x', var_name='theta_dot', shape=(1,1))

    # right motor input radians/s
    v_r = model.set_variable(var_type='_u', var_name='v_r')
    # left motor input radians/s
    v_l = model.set_variable(var_type='_u', var_name='v_l')

    # right hand side of the model
    model.set_rhs('x_dot', r / 2 * (v_r + v_l) * np.cos(theta))
    model.set_rhs('y_dot', r / 2 * (v_r + v_l) * np.sin(theta))
    model.set_rhs('theta_dot', r / l * (v_r - v_l))

    model.setup()
    return model