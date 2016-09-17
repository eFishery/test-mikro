from unittest import TestCase

from test_mikro.send_command import send_command

class TestSendCommand(TestCase):
    def test_is_string(self):
        s = send_command('','AT')
        self.assertTrue(isinstance(s, basestring))