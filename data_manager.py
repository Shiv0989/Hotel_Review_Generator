import pandas as pd

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)

    def filter_data(self, hotel, date, service, time):
        return self.df[(self.df['HOTEL NAME'] == hotel) &
                       (self.df['DATE'] == date) &
                       (self.df['TYPE OF SERVICE'] == service) &
                       (self.df['TIME'] == time)]

    def update_data(self, new_data):
        self.df = self.df.append(new_data, ignore_index=True)
        self.df.to_excel(self.file_path, index=False)
