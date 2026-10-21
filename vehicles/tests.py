import pandas as pd
from django.test import TestCase, Client
from django.urls import reverse
from .dashboard import frequency_table


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

    def test_dashboard_view_status_and_template(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "vehicles/index.html")
        self.assertIn("frequency_table", response.context)
        self.assertContains(response, "Vehicle Machine Learning Dashboard")
        self.assertContains(response, "Frequency Tables (One-way)")
