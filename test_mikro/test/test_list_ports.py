from unittest import TestCase

from test_mikro.list_ports import list_ports

class TestListPorts(TestCase):
    def test_is_array(self):
        s = list_ports()
        self.assertTrue(isinstance(s, list))