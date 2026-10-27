import pandas as pd
from django.test import TestCase, Client
from django.urls import reverse
from .dashboard import frequency_table, filter_by_price


class VehicleDashboardTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_frequency_table_generation(self):
        sample_df = pd.DataFrame({
            "manufacturer": ["Toyota", "Honda", "Toyota", "Ford"]
        })
        html_table = frequency_table(sample_df)
        self.assertIn("Toyota", html_table)
        self.assertIn("Honda", html_table)
        self.assertIn("Ford", html_table)
        self.assertIn("table table-bordered table-striped table-sm", html_table)

    def test_filter_by_price(self):
        sample_df = pd.DataFrame({
            "manufacturer": ["CarCheap", "CarExpensive"],
            "selling_price": [3000, 15000]
        })
        html_table = filter_by_price(sample_df, min_price=5000)
        self.assertNotIn("CarCheap", html_table)
        self.assertIn("CarExpensive", html_table)
        self.assertIn("15000", html_table)
        self.assertIn("table table-bordered table-striped table-sm", html_table)

    def test_dashboard_view_status_and_template(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "vehicles/index.html")
        self.assertIn("frequency_table", response.context)
        self.assertIn("filtered_vehicles_table", response.context)
        self.assertContains(response, "Vehicle Machine Learning Dashboard")
        self.assertContains(response, "Frequency Tables (One-way)")
        self.assertContains(response, "Vehicles with Price Above $5,000")
