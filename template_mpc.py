import do_mpc


def template_mpc(model):
    mpc = do_mpc.controller.MPC(model)
    setup_mpc = {
        'n_horizon': 10,
        'n_robust': 1,
        't_step': 0.1,
        'nlpsol_opts': {'ipopt.linear_solver': 'ma27'},
    }
    mpc.set_param(**setup_mpc)
    mterm = model.aux['cost']
    lterm = model.aux['cost'] # terminal cost

    mpc.set_objective(mterm=mterm, lterm=lterm)
    mpc.set_rterm()