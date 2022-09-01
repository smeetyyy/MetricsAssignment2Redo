import unittest
import json
from selenium import webdriver



class Tester(unittest.TestCase):
    "Class to Calculate Performance"

    def setUp(self):
        "doc string"
        self.driver = webdriver.Chrome(r"C:\Users\stefa\Desktop\Metrics2\webdriver\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verification_errors = []

    def test_er(self):
        """
        This function runs performance 10 times and generates
        json, .csv and .txt files. It aslo calculates mean average
        of the performance
        :return:
        """
        driver = self.driver
        total = {}

        # this creates an output.txt file and appends the name and duration
        with open("output.txt", "w") as json_file:
            for result in range(10):
                driver.get("https://en.wikipedia.org/wiki/Software_metric")
                result = driver.execute_script("return window.performance.getEntries()")


                for current in result:
                    url = current["name"]
                    current_list = total.get(url, [])
                    current_list.append(current["duration"])
                    total[url] = current_list
                    json_file.write(f"{current['name']}, {current['duration']}\n")



        # This creates a csv file and calculates the average duration and appends it to the csv file
        with open("mycsv.csv", "w") as csv_file:
            for key, value in total.items():
                average = sum(value) / len(total)
                csv_file.write(f"{key}, {average}\n")



        # This makes a JSON output file and prettifies it
        with open("json_output" + ".json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verification_errors)


if __name__ == "__main__":
    unittest.main()
