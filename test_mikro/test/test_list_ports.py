from unittest import TestCase

import test_mikro

class TestListPorts(TestCase):
    def test_is_array(self):
        s = test_mikro.list_ports()
        self.assertTrue(isinstance(s, list))