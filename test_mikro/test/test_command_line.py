from unittest import TestCase

from test_mikro.command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()