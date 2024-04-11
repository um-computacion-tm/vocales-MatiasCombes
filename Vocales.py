import unittest

def contar_vocales(mi_string):
    mi_string = mi_string.lower()
    resultado = {}
    for letra in mi_string:
        if letra in 'aeiou':
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales (unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado,{})

    def test_contar_voca(self):
        resultado = contar_vocales('cegar')
        self.assertEqual(resultado,{'a':1, 'e':1})

    def test_contar_voca(self):
        resultado = contar_vocales('murcielago')
        self.assertEqual(resultado,{'a':1, 'e':1, 'i':1, 'o':1, 'u':1})

    def test_contar_voca(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado,{'a':2})

    def test_contar_voca(self):
        resultado = contar_vocales('faro')
        self.assertEqual(resultado,{'a':1, 'o':1})

    def test_contar_voca(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado,{'a':3, 'o':1})

    def test_contar_VocaMayus(self):
        resultado = contar_vocales('cAsA')
        self.assertEqual(resultado,{'a':2})
    
    def test_contar_MayusVoca(self):
        resultado = contar_vocales('AiaUe')
        self.assertEqual(resultado,{'a':2, 'e':1, 'i':1, 'u':1})
    


unittest.main()

