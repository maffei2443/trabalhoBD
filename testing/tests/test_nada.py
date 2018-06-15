import unittest
from src import nada  # Importa o arquivo nadda.py
from src import nadi  # Importa a variavel nadi, que eh exportada pelo __init__.py de src/
class TestNadaNadi(unittest.TestCase):
	"""Exemplos de teste envolvendo importação de módulos próprios.."""
	mnada = nada
	mnadi = nadi
	def test_nada(self):
		self.assertEqual(self.mnada.foo(), "nada")
	def test_nadi(self):
		self.assertEqual(self.mnadi.foo(), "nada")
