import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_negatiivisella_tilavuudella(self):
        negatiivinen_varasto = Varasto(-10)

        self.assertAlmostEqual(negatiivinen_varasto.tilavuus, 0)

    def test_varasto_negatiivisella_saldolla(self):
        negatiivinen_varasto = Varasto(10, -10)

        self.assertAlmostEqual(negatiivinen_varasto.saldo, 0)
    def test_varasto_ylimenevalla_saldolla(self):
        ylimeneva_varasto = Varasto(10, 20)

        self.assertAlmostEqual(ylimeneva_varasto.saldo, 10)
    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.lisaa_varastoon(-10)


        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisaa_varastoon_maara_joka_mahtuu(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisaa_varastoon_maara_joka_ei_mahdu(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_necgatiivinen(self):
        self.varasto.lisaa_varastoon(10)
        arvo = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(arvo, 0)
    def test_ota_varastosta_toimii(self):
        self.varasto.lisaa_varastoon(10)
        arvo = self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(arvo, 5)
    def test_ota_varastosta_yli_saldon(self):
        self.varasto.lisaa_varastoon(10)
        arvo = self.varasto.ota_varastosta(200)

        self.assertAlmostEqual(arvo, 10)
    def test_printtaus_toimii(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
