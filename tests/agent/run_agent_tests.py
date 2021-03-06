import subprocess

import sys
py_path = '../../scripts/'
sys.path.insert(0, py_path)

import utils as ut
from colors import *

py_version = 'python3'

#
# Compile and run all the agent class specific tests
#

# Compile
subprocess.call([py_version + ' compilation.py'], shell=True)

# Test suite 1
ut.msg('Agent class functionality tests', CYAN)
subprocess.call(['./agent_test'], shell=True)

# Test suite 2
ut.msg('Agent state getter/setter tests', CYAN)
subprocess.call(['./agent_states_test'], shell=True)
