import unittest
from src import nada
from src import nadi
class TestNadaNadi(unittest.TestCase):
	mnada = nada
	mnadi = nadi
	def test_nada(self):
		self.assertEqual(self.mnada.foo(), "nada")
	def test_nadi(self):
		self.assertEqual(self.mnadi.foo(), "nada")
