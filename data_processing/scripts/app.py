import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    st.title("Modeling Tomorrow: Predictive Analysis and Forecasting of Child Mortality ")
    st.markdown(
        """
        <style>
            @keyframes fadeInOut {
                0% {
                    background-color: black;
                }
                50% {
                    background-color: #00000080; /* Slightly transparent black */
                }
                100% {
                    background-color: black;
                }
            }

            div.fade-background {
                animation: fadeInOut 5s infinite;
            }
        </style>

        <div class="fade-background" style="padding: 10px; border-radius: 10px">
            <h2 style="color: white; text-align: center;">Modeling Tomorrow predictor </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    prediction_option = st.selectbox('Choose Prediction Option', ['World Child Mortality', 'By Country', 'By Region', 'SDG for Region'])

    if prediction_option == 'World Child Mortality':
        years = st.text_input("Years", "Type Here")
        output = ""

        if st.button("Predict"):
            data = pd.read_csv("world.csv") 
            x = np.array(data['Year']).reshape(-1, 1)
            y = np.array(data['Lower']).reshape(-1, 1)

            # Linear Regression
            model = LinearRegression()
            model.fit(x, y)

            # Prediction
            try:
                year_to_predict = float(years)  # Convert the input to float
            except ValueError:
                st.warning("Please enter a valid integer for 'Years'.")
                return

            prediction = model.predict(np.array([[year_to_predict]]))
            output = f'The Mortality Rate for the world{year_to_predict} will be: {prediction[0]}'
            st.success(output)

    
if __name__ == '__main__':
    main()
