# Hotel Review Generator

## Project Description:

The Hotel Review Summary Generator is a Streamlit-based application tailored for auditors in the hospitality industry. It harnesses OpenAI's GPT-3 to transform selected review parameters or brief points into detailed, insightful summaries. Besides, the application offers functionality to filter and summarize reviews based on criteria like hotel name, date, service type, and time, enabling users to focus on specific aspects of customer feedback. This tool is essential for auditors and hotel management teams, providing a quick and efficient way to interpret customer feedback and convert it into actionable insights for service improvement. 

## Installation:

To set up the project locally, follow these steps:

-> Clone the repository

-> Navigate to the project directory

-> Install the required dependencies:

```python
pip install -r requirements.txt
```


This command will install all the necessary libraries.

## Usage:

To run the application, start the Streamlit server:
```python
streamlit run main.py
```

The application should now be running on http://localhost:8501. Open this URL in a web browser.

## Structure:

The application is structured into several modules:

1.) data_manager.py: Manages data loading, filtering, and updating.

2.) api_client.py: Handles interactions with the OpenAI API.

3.) streamlit_ui.py: Contains the Streamlit interface components.

4.) main.py: The entry point for the application.

```
.main/              
│
├── README.md       
│
├── data_manager.py          
│
├── api_client.py      
│
├── streamlit_ui.py         
│
├── main.py         
          
```

## License:

Hotel Review Generator is [MIT Licensed](https://github.com/Shiv0989/Hotel_Review_Generator/blob/main/LICENSE).
