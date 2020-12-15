from django.test import TestCase, Client
from django.urls import resolve
from .views import rapidTest, form_Rapid
from .models import Rapid

class RapidAppTest(TestCase):
    # Rapid Test
    def test_apakah_url_rapidTest_ada(self):
        response = Client().get('/rapidTest/')
        self.assertEqual(response.status_code,200)

    def test_apakah_di_halaman_Rapid_Test_ada_templatenya(self):
        response = Client().get('/rapidTest/')
        self.assertTemplateUsed(response, 'rapidTest/rapidTest.html')

    def test_apakah_menggunakan_fungsi_rapidTest(self):
        found = resolve('/rapidTest/')
        self.assertEqual(found.func, rapidTest)

    def test_apakah_di_halaman_Rapid_Test_ada_text_dan_tombol(self):
        response = Client().get('/rapidTest/')
        html_kembalian = response.content.decode('utf8')
        self.assertIn("DAFTAR TEMPAT RAPID TEST", html_kembalian)
        self.assertIn("Nama Tempat", html_kembalian)
        self.assertIn("Tanggal Pelaksanaan", html_kembalian)
        self.assertIn("Biaya", html_kembalian)
        self.assertIn("Alamat", html_kembalian)
        self.assertIn("Add", html_kembalian)


    # Form Rapid
    def test_apakah_url_formRapid_ada(self):
        response = Client().get('/formRapid/')
        self.assertEqual(response.status_code,200)
    
    def test_apakah_di_halaman_Form_Rapid_ada_templatenya(self):
        response = Client().get('/formRapid/')
        self.assertTemplateUsed(response, 'rapidTest/formRapid.html')

    def test_apakah_menggunakan_fungsi_form_Rapid(self):
        found = resolve('/formRapid/')
        self.assertEqual(found.func, form_Rapid)

    def test_apakah_di_halaman_Form_Rapid_ada_text_dan_tombol(self):
        response = Client().get('/formRapid/')
        html_kembalian = response.content.decode('utf8')
        self.assertIn("TAMBAH TEMPAT RAPID TEST", html_kembalian)
        self.assertIn("Nama Tempat", html_kembalian)
        self.assertIn("Tanggal Pelaksanaan", html_kembalian)
        self.assertIn("Biaya", html_kembalian)
        self.assertIn("Alamat", html_kembalian)
        self.assertIn("Add", html_kembalian)
        self.assertIn("Back", html_kembalian)


    # Test Model
    def test_apakah_sudah_ada_model_Rapid(self):
        Rapid.objects.create(nama_tempat= "Labklin Kimia Farma Pontianak", tanggal_pelaksanaan_mulai= '2020-1-1', 
                             tanggal_pelaksanaan_akhir= '2020-12-31', biaya= 150.000, 
                             alamat= "Jl. Prof. M.Yamin No.A7, Sungai Bangkong, Kec. Pontianak Sel., Kota Pontianak, Kalimantan Barat")
        hitung_object = Rapid.objects.all().count()
        self.assertEqual(hitung_object,1)


    # Test Form
    def test_apakah_bisa_menyimpan_sebuah_POST_request(self):
        response = self.client.post('/formRapid/', data={'nama_tempat':'Labklin Kimia Farma Pontianak', 
                                                                   'tanggal_pelaksanaan_mulai': '2020-1-1',
                                                                   'tanggal_pelaksanaan_akhir': '2020-12-31', 'biaya':150.000,
                                                                   'alamat':'Jl. Prof. M.Yamin No.A7, Sungai Bangkong, Kec. Pontianak Sel., Kota Pontianak, Kalimantan Barat'})
        hitung_object = Rapid.objects.all().count()
        self.assertEqual(hitung_object,1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/rapidTest')

        new_response = self.client.get('/rapidTest/')
        html_response = new_response.content.decode('utf8')
        self.assertIn('DAFTAR TEMPAT RAPID TEST', html_response)   