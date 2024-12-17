import unittest
from cadre import Cadre
from cadre.framework import framework_from_config
from cadre.controllers import load_controllers


class CadreFlask(Cadre):

    application = 'cadre_test_app'

    def __init__(self):
        Cadre.__init__(self, None)
        self.framework = framework_from_config(self.application,
                                               {self.application:
                                                {'framework': 'flask'}})
        load_controllers(self.framework, self.application)


class TestCadreFlask(unittest.TestCase):

    def setUp(self):
        self.cadre = CadreFlask()

    def test_setup_routes(self):
        self.cadre.framework._setup_routes()
