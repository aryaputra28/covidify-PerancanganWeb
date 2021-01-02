from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Rumah_Sakit
from .forms import Form_RS
from .views import tambahRS, listRS, api_rs

class TestModel(TestCase): #test untuk cek apakah data berhasil dimasukan ke database
    def test_apakah_ada_model_rumah_sakit(self):
        Rumah_Sakit.objects.create(provinsi = "DKI Jakarta", nama_rs = "RS SUlianti Saroso", 
                                    alamat = "Jl. Baru Sunter Permai Raya, Papanggo", 
                                    telepon = "216401411", website = "https://rspi-suliantisaroso.com/")
        hitung_jumlah_data = Rumah_Sakit.objects.all().count()
        self.assertEquals(hitung_jumlah_data, 1)

class TestForm(TestCase):
    def test_form_rs_valid(self):
        form_rs = Form_RS(data={"provinsi":"DKI Jakarta", "nama_rs":"RS SUlianti Saroso",
                                    "alamat":"Jl. Baru Sunter Permai Raya, Papanggo", "telepon":"216401411", 
                                    "website":"https://rspi-suliantisaroso.com/"})
        
        self.assertTrue(form_rs.is_valid())
    
    def test_form_rs_invalid(self):
        form_rs = Form_RS(data={})
        self.assertFalse(form_rs.is_valid())

class TestURL(TestCase):
    def setUp(self):
        self.rs = Rumah_Sakit.objects.create(provinsi = "DKI Jakarta", nama_rs = "RS SUlianti Saroso", 
                                    alamat = "Jl. Baru Sunter Permai Raya, Papanggo", 
                                    telepon = "216401411", website = "https://rspi-suliantisaroso.com/")
        self.tambahRS = reverse("list_rs:tambahRS")
        self.listRS = reverse("list_rs:listRS")
        self.data = reverse("list_rs:data")
    
    def test_apakah_fungsi_tambah_rs_ada(self):
        found = resolve(self.tambahRS)
        self.assertEqual(found.func, tambahRS)
    
    def test_apakah_fungsi_list_rs_ada(self):
        found = resolve(self.listRS)
        self.assertEqual(found.func, listRS)
    
    def test_apakah_fungsi_api_rs_ada(self):
        found = resolve(self.data)
        self.assertEqual(found.func, api_rs)
    

class TestView(TestCase):
      
    def test_apakah_di_halaman_list_rs_ada_templatenya(self):
        response = Client().get('/listRS/')
        self.assertTemplateUsed(response, 'list_rs/list_rs.html')
    
    def test_apakah_di_halaman_tambah_rs_ada_templatenya(self):
        response = Client().get('/tambahRS/')
        self.assertTemplateUsed(response, 'list_rs/tambah_rs.html')
    

    
    


