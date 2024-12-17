#!/usr/bin/env python3

from cadre_test_app import Cadre_Test_App
from cadre.controllers import get_controllers_tsts

locals().update(get_controllers_tsts(Cadre_Test_App(None)))
