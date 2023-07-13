# flake8: noqa: F401
# Modular imports
import importlib.util as iutil
import warnings

# Classic control is in gym and thus necessary for the base version to run
from carl.envs.gymnasium import *

# Environment loading
box2d_spec = iutil.find_spec("Box2D")
found = box2d_spec is not None
if found:
    from carl.envs.gymnasium.box2d import *
else:
    warnings.warn(
        "Module 'Box2D' not found. If you want to use these environments, please follow the installation guide."
    )

brax_spec = iutil.find_spec("brax")
found = brax_spec is not None
if found:
    from carl.envs.brax import *

    pass
else:
    warnings.warn(
        "Module 'Brax' not found. If you want to use these environments, please follow the installation guide."
    )

# TODO: This is currently out because of Java issues. 
# try:
#     from carl.envs.mario import *
# except:
#     warnings.warn(
#         "Module 'Mario' not found. Please follow installation guide for ToadGAN environment."
#     )

dm_control_spec = iutil.find_spec("dm_control")
found = dm_control_spec is not None
if found:
    from carl.envs.dmc import *
else:
    warnings.warn(
        "Module 'dm_control' not found. If you want to use these environments, please follow the installation guide."
    )

rna_spec = iutil.find_spec("distance")
found = rna_spec is not None
if found:
    from carl.envs.rna import *
else:
    warnings.warn(
        "Could not load RNA env. If you want to use this environment, please follow the installation guide."
    )
