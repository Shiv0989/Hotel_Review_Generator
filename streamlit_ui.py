import streamlit as st

class StreamlitUI:
    def __init__(self, data_manager, api_client):
        self.data_manager = data_manager
        self.api_client = api_client

    def run(self):
        st.title('Hotel Review Summary Generator')

        # Created dropdowns for user input
        df = self.data_manager.df
        hotel_names = df['HOTEL NAME'].unique().tolist()
        selected_hotel = st.selectbox('Select Hotel', hotel_names)

        dates = df['DATE'].unique().tolist()
        selected_date = st.selectbox('Select Date', dates)

        service_types = df['TYPE OF SERVICE'].unique().tolist()
        selected_service_type = st.selectbox('Select Type of Service', service_types)

        times = df['TIME'].unique().tolist()
        selected_time = st.selectbox('Select Time', times)

        # Generate summary button for existing reviews
        if st.button('Generate Summary'):
            filtered_data = self.data_manager.filter_data(selected_hotel, selected_date, selected_service_type, selected_time)
            if not filtered_data.empty:
                combined_reviews = ' '.join(filtered_data['REVIEW'].tolist())
                summary = self.api_client.generate_summary_with_gpt3(None, combined_reviews)
                st.write(summary)
            else:
                st.write('No reviews found for the selected options.')

        # Expand Review Points into Detailed Review
        st.subheader("Expand Review Points into Detailed Review")
        with st.form("expand_review_form"):
            review_points = st.text_area("Enter short points for the review")
            submitted_expand = st.form_submit_button("Expand Review")
            
            if submitted_expand:
                # Get combined reviews from the DataFrame
                combined_reviews = ' '.join(df['REVIEW'].tolist())
                expanded_review = self.api_client.generate_summary_with_gpt3(review_points, combined_reviews)
                st.text_area("Expanded Review", expanded_review, height=150)

        # Add new entries section
        if st.checkbox('Add new entries'):
            with st.form("new_data_form", clear_on_submit=True):
                # Create input fields for each column
                new_hotel_name = st.text_input('Hotel Name')
                new_date = st.text_input('Date')
                new_service_type = st.text_input('Type of Service')
                new_time = st.text_input('Time')
                new_review = st.text_area('Review')

                # Submit button for the form
                submitted = st.form_submit_button('Submit New Entry')
                if submitted:
                    # Append new data to the DataFrame
                    new_data = {'HOTEL NAME': new_hotel_name, 'DATE': new_date, 
                                'TYPE OF SERVICE': new_service_type, 'TIME': new_time, 
                                'REVIEW': new_review}
                    self.data_manager.update_data(new_data)
                    st.success('Data added successfully!')
