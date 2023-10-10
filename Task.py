import json
import pandas as pd
import logging

"""Initialise logging"""
logging.basicConfig(level=logging.INFO)


class CarData:
    """This is a class used to process the car data from the json file"""

    def __init__(self):
        """Initialize the data object (which is later converted into a pandas DataFrame)"""
        self.data = None

    def load_car_data(self):
        """This method loads the car data from the json file."""
        try:
            # Try to load the data from the json file
            with open('cars.txt', 'r') as car_data:
                json_car_data = json.load(car_data)
                self.data = pd.DataFrame(json_car_data['cars'])
            logging.info('Data loaded successfully from the file')
        except Exception as exc:
            # Handle any issue that prevents the data from loading
            logging.error(f"{str(exc)} error occurred while loading the data.")
            raise

    def display_data(self):
        """Display the first 5 rows of the car data DataFrame"""
        if self.data is not None:
            print(self.data.head())
        else:
            logging.info("No data has been loaded and cannot be displayed.")

    def print_unique_cars(self):
        """Print the number of unique cars by taking into account the make, model and year of prodcution"""
        try:
            # Try to remove duplicate rows and print the number of unique cars
            unique_cars = self.data.drop_duplicates(subset=['make', 'model', 'year'])
            print(f"Number of unique cars: {len(unique_cars)}")
        except KeyError as e:
            # Handle potential missing columns
            logging.error(f"The car data does not contain the expected column. The missing ones are: {str(e)}")
        except TypeError as e:
            # Handle potential data type errors
            logging.error(f"Encountered a data type error {str(e)}")
        except Exception as e:
            # Handle any other potential issues
            logging.error(f"An unexpected error occurred: {str(e)}")

    def print_avg_horsepower(self):
        """Calculates the mean of the horse_power_column and prints it"""
        try:
            # Try to calculate the average horse powers and print the number
            avg_hp = self.data['horse_power'].mean()
            print(f"Average horsepower of cars: {avg_hp:.2f}")
        except KeyError:
            # Handle a missing column
            logging.error("The car data does not have a horse_power column.")
        except TypeError:
            # Handle a data type error
            logging.error("The data type of the column can't be averaged (non-numeric data)")
        except Exception as e:
            # Handle any other possible issue
            logging.error(f"{str(e)} error occurred while trying to calculate the average horse power.")

    def print_top_heaviest_cars(self):
        """Looks into the weight column and select the 5 heaviest cars and prints their make, model and weight"""
        try:
            # Try to find the 5 heaviest cars and print them out
            top_heavy_cars = self.data.nlargest(5, 'weight')
            print("Top 5 heaviest cars:")
            print(top_heavy_cars[['make', 'model', 'weight']])
        except KeyError:
            # Handle missing columns
            logging.error("The car data has no weight column")
        except ValueError:
            # Handle data type errors
            logging.error("The data in the weight column can't be ranked (non-numeric data)")
        except Exception as e:
            # Handle any other issue
            logging.error(f"{str(e)} error occurred while trying to rank the data in the weight column")

    def print_cars_per_manufacturer(self):
        """Looks into the make column and counts the number of unique cars using the .value_counts() pandas method"""
        try:
            # Try to count the cars per make
            count_per_make = self.data['make'].value_counts()
            print("Number of cars per manufacturer:")
            print(count_per_make)
        except KeyError:
            # Handle a missing column
            logging.error("The car data does not contain a make column")
        except Exception as e:
            # Handle any other potential issue
            logging.error(f"{str(e)} error occurred while trying to count the cars per manufacturer.")

    def print_cars_per_year(self):
        """Looks into the year column and prints out the number of cars per year"""
        try:
            # Try to count the cars manufactured per year
            count_per_year = self.data['year'].value_counts()
            print("Number of cars per production year:")
            print(count_per_year)
        except KeyError:
            # Handle a missing column
            logging.error("The car data does not contain an year column")
        except Exception as e:
            # Handle any other issue
            logging.error(f"{str(e)} error occurred while trying to count the cars manufactured per year")

    def save_to_csv(self, output_file='cars.csv'):
        """Saves the DataFrame to a .csv file"""
        try:
            # Try to save the data to a .csv file
            self.data.to_csv(output_file, index=False)
            logging.info(f'Data saved to {output_file}')
        except IOError as e:
            # Handles an IO error
            logging.error(f"Failed to save data to {output_file}: {str(e)}")
        except Exception as e:
            # Handles any other possible issue
            logging.error(f"{str(e)} error occurred while saving the data")


def main():
    processor = CarData()
    processor.load_car_data()
    processor.display_data()
    processor.print_unique_cars()
    processor.print_avg_horsepower()
    processor.print_top_heaviest_cars()
    processor.print_cars_per_manufacturer()
    processor.print_cars_per_year()
    processor.save_to_csv()


if __name__ == "__main__":
    main()
