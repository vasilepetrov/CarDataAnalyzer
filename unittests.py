import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import json
from Task import CarData


class TestCarDataMethods(unittest.TestCase):
    # Sample data for mocking
    mock_data = {
        "cars": [
            {"make": "Toyota", "model": "Corolla", "year": 2005, "horse_power": 100, "weight": 1500},
            {"make": "Ford", "model": "Fusion", "year": 2007, "horse_power": 110, "weight": 1600},
            {"make": "Chevrolet", "model": "Malibu", "year": 2005, "horse_power": 120, "weight": 1500},
        ]
    }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data))
    def test_load_car_data(self, mock_file):
        car_data = CarData()
        car_data.load_car_data()
        self.assertIsInstance(car_data.data, pd.DataFrame)
        self.assertEqual(len(car_data.data), 3)  # as we have 3 records in mock_data

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data))
    def test_print_unique_cars(self, mock_file):
        car_data = CarData()
        car_data.load_car_data()
        with patch("builtins.print") as mock_print:
            car_data.print_unique_cars()
            mock_print.assert_called_once_with("Number of unique cars: 3")  # based on mock_data

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data))
    def test_print_avg_horsepower(self, mock_file):
        car_data = CarData()
        car_data.load_car_data()
        with patch("builtins.print") as mock_print:
            car_data.print_avg_horsepower()
            mock_print.assert_called_once_with("Average horsepower of cars: 110.00")  # based on mock_data

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data))
    def test_print_top_heaviest_cars(self, mock_file):
        car_data = CarData()
        car_data.load_car_data()
        with patch("builtins.print") as mock_print:
            car_data.print_top_heaviest_cars()
            self.assertEqual(mock_print.call_count, 2)  # Ensure it prints title and data

    # More tests...


if __name__ == '__main__':
    unittest.main()
