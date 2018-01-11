from config import *
import csv
import unittest

threshold = 10000

def count_truthy(rows, key):
    return len([row for row in rows if row[key]])

def percent_truthy(rows, key):
    return float(count_truthy(rows, key)) / len(rows)

class TestDataMethods(unittest.TestCase):
    
    def setUp(self):
        with open(path_to_output) as f:
            rows = []
            for line in csv.DictReader(f, delimiter="\t"):
                rows.append(line)
                if len(rows) >= threshold:
                    break
                
        self.rows = rows
        self.num_rows = len(rows)

    def test_primary_names(self):
        percent = percent_truthy(self.rows, "primary_name")
        self.assertEqual(percent, 1)

    def test_enwiki_title(self):
        percent = percent_truthy(self.rows, "enwiki_title")
        self.assertGreaterEqual(percent, 0.25)

    def test_other_names(self):
        percent = percent_truthy(self.rows, "alternative_names")
        self.assertGreaterEqual(percent, 0.5)

    def test_country(self):
        percent = percent_truthy(self.rows, "country")
        self.assertGreaterEqual(percent, 0.5)

    def test_country_code(self):
        percent = percent_truthy(self.rows, "country_code")
        self.assertGreaterEqual(percent, 0.5)

    def test_elevation(self):
        percent = percent_truthy(self.rows, "elevation")
        self.assertGreaterEqual(percent, 0.005)

    def test_wikidata_classes(self):
        percent = percent_truthy(self.rows, "wikidata_classes")
        self.assertGreaterEqual(percent, 0.5)

    def test_elevation(self):
        percent = percent_truthy(self.rows, "elevation")
        self.assertGreaterEqual(percent, 0.005)
        
    def test_geonames_id(self):
        percent = percent_truthy(self.rows, "geonames_id")
        self.assertGreaterEqual(percent, 0.5)

    def test_latitude(self):
        percent = percent_truthy(self.rows, "latitude")
        self.assertGreaterEqual(percent, 1) 

    def test_longitude(self):
        percent = percent_truthy(self.rows, "longitude")
        self.assertGreaterEqual(percent, 1)

    def test_population(self):
        percent = percent_truthy(self.rows, "population")
        self.assertGreaterEqual(percent, 0.25) 

if __name__ == '__main__':
    unittest.main()
