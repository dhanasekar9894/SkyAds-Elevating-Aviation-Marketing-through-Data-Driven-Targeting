
import pickle
import numpy as np
from joblib import dump
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#function for prediction
def taking_product_or_not_prediction(input_data):
  
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make predictions
    prediction = loaded_model.predict(input_data_reshaped)

    # Set threshold
    threshold = 0.5
    print(prediction)

    # Convert to binary prediction
    if prediction > threshold:
        return 'most likely to buy the product'
    else:
        return 'less chances of buying the product'
    
    
    
def main():
    
    #giving title
    st.title('aviation web app')
    
    #getting input data from user

    yearly_avg_Outstation_checkins = st.text_input("yyearly_avg_Outstation_checkins")
    member_in_family = st.text_input("member_in_family")
    preferred_location_type = st.text_input("preferred_location_type")
    total_likes_on_outofstation_checkin_received = st.text_input("total_likes_on_outofstation_checkin_received")
    week_since_last_outstation_checkin = st.text_input("week_since_last_outstation_checkin")
    following_company_page = st.text_input("following_company_page")
    montly_avg_comment_on_company_page = st.text_input("montly_avg_comment_on_company_page")
    working_flag = st.text_input("working_flag")
    travelling_network_rating = st.text_input("travelling_network_rating")
    Adult_flag = st.text_input("Adult_flag")
    Daily_Avg_mins_spend_on_traveling_page = st.text_input("Daily_Avg_mins_spend_on_traveling_page")
    Yearly_avg_view_on_travel_page = st.text_input("Yearly_avg_view_on_travel_page")
    total_likes_on_outstation_checkin_given = st.text_input("total_likes_on_outstation_checkin_given")
    Yearly_avg_comment_on_travel_page = st.text_input("Yearly_avg_comment_on_travel_page")
    
    
    #code for prediction
    taken_product_or_not = ''
    
    #creating a button for prediction
    
    if st.button('Prediction Result'):
        taken_product_or_not = taking_product_or_not_prediction([yearly_avg_Outstation_checkins,member_in_family,preferred_location_type,total_likes_on_outofstation_checkin_received,week_since_last_outstation_checkin,following_company_page,montly_avg_comment_on_company_page,working_flag,travelling_network_rating,Adult_flag,Daily_Avg_mins_spend_on_traveling_page,Yearly_avg_view_on_travel_page,total_likes_on_outstation_checkin_given,Yearly_avg_comment_on_travel_page])
    
    
    st.success(taken_product_or_not)
    
    
    
if __name__ == '__main__':
    main()