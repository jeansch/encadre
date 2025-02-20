#!/usr/bin/env python3

from encadre_test_app import Encadre_Test_App
from encadre.controllers import get_controllers_tsts

locals().update(get_controllers_tsts(Encadre_Test_App(None)))
