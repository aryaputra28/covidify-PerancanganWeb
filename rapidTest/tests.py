from django.test import TestCase, Client
from django.urls import resolve
from .views import rapidTest, form_Rapid, api_rapid
from .models import Rapid

class RapidAppTest(TestCase):
    maxDiff = None
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


    # views api_rapid
    def test_apakah_url_dataRapid_ada(self):
        response = Client().get('/dataRapid/')
        self.assertEqual(response.status_code,200)

    def test_apakah_menggunakan_fungsi_api_rapid(self):
        found = resolve('/dataRapid/')
        self.assertEqual(found.func, api_rapid)
    
    def test_content_type_api_rapid(self):
        response = Client().get('/dataRapid/')
        self.assertEqual(response['content-type'], 'text/json-comment-filtered')


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


    
    # def test_apakah_data_json_sesuai(self):
    #     Rapid.objects.create(nama_tempat= "Labklin Kimia Farma Pontianak", tanggal_pelaksanaan_mulai= '2020-1-1', 
    #                          tanggal_pelaksanaan_akhir= '2020-12-31', biaya= 150.000, 
    #                          alamat= "Jl. Prof. M.Yamin No.A7, Sungai Bangkong, Kec. Pontianak Sel., Kota Pontianak, Kalimantan Barat")
    #     obj = Rapid.objects.all()
    #     # self.assertEqual(obj, [{"model": "rapidTest.rapid", "pk": 1, "fields": {"nama_tempat": "Labklin Kimia Farma Pontianak", 
    #     #                         "tanggal_pelaksanaan_mulai": "2020-1-1", "tanggal_pelaksanaan_akhir": "2020-12-31", 
    #     #                         "biaya": "150.000", "alamat": "Jl. Prof. M.Yamin No.A7, Sungai Bangkong, Kec. Pontianak Sel., Kota Pontianak, Kalimantan Barat"}}])
    #     self.assertEqual(obj, <QuerySet [<Rapid: Rapid obj (1)>]>)







    # def test_apakah_pemanggilan_data_json_sesuai(self):
    #     response = Client().get('/dataRapid/')
    #     self.assertJSONEqual(response.content.decode("utf-8"), {"model": "rapidTest.rapid", "pk": 1, "fields": {"nama_tempat": "RS Restu Kasih", "tanggal_pelaksanaan_mulai": "2020-09-17", 
    #                                                             "tanggal_pelaksanaan_akhir": "2020-12-31", "biaya": "150.000", 
    #                                                             "alamat": "Jalan Raya Bogor KM.19 No.3A, Kramat Jati, RT.3/RW.1, Kramat Jati, Kec. Kramat jati, Kota Jakarta Timur, Daerah Khusus Ibukota Jakarta 13510, Kota Jakarta Timur 13510"}}, 
    #                                                             {"model": "rapidTest.rapid", "pk": 2, "fields": {"nama_tempat": "RS Sumber Waras", "tanggal_pelaksanaan_mulai": "2020-09-17", 
    #                                                             "tanggal_pelaksanaan_akhir": "2020-12-31", "biaya": "135.000", "alamat": "Jl. Kyai Tapa No 1 RT 10 RW 10, Tomang, Kecamatan Grogol petamburan, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11440, Kota Jakarta Barat 11440"}}, 
    #                                                             {"model": "rapidTest.rapid", "pk": 3, "fields": {"nama_tempat": "Labklin Kimia Farma Semarang Sutomo", "tanggal_pelaksanaan_mulai": "2020-09-17", 
    #                                                             "tanggal_pelaksanaan_akhir": "2020-12-31", "biaya": "150.000", "alamat": "Jl. Pemuda No.135, Sekayu, Kec. Semarang Tengah, Kota Semarang, Jawa Tengah 50132, Kota Semarang"}})  

    # def test_apakah_pemanggilan_data_json_tidak_sesuai(self):
    #     mod = Rapid.objects.all()
    #     m = mod.model
    #     self.assertEqual(m, Rapid)

        # response = Client().get('/dataRapid/')  
        # self.assertJSONNotEqual(response.content.decode("utf-8"),{"model":"abc"})

    
    
    # def test_POSTing_a_new_item(self):
    #     listt = Rapid.objects.create()
    #     response = Client().get('/dataRapid/')
    #     response2 = self.client.post(response,
    #                 {"nama_tempat": "RS", "tanggal_pelaksanaan_mulai": "2020-09-17", 
    #                  "tanggal_pelaksanaan_akhir": "2020-12-31", "biaya": 150.000, 
    #                  "alamat": "Jalan i"})
    #     self.assertEqual(response2.status_code,200)
    #     new_item = listt.item_set.get()
    #     self.assertEqual(new_item.model, rapidTest.rapid)