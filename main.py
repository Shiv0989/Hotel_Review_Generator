from data_manager import DataManager
from api_client import APIClient
from streamlit_ui import StreamlitUI

def main():
    data_file_path = 'Your_File_Path'
    data_manager = DataManager(data_file_path)
    api_client = APIClient()
    ui = StreamlitUI(data_manager, api_client)
    ui.run()

if __name__ == "__main__":
    main()
