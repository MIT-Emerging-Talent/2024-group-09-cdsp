import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Load data and train model for world child mortality rate
def load_data_and_train_model(file_path):
    df = pd.read_csv(file_path)

    # Select features (X) and target variable (y)
    X = df[['Year']]  
    y = df['Median']  

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model: Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    # Evaluate the model
    mse = mean_squared_error(y_test, lr_model.predict(X_test))
    r2 = r2_score(y_test, lr_model.predict(X_test))

    return df, lr_model, mse, r2

# Function to make predictions
def make_predictions(model, years):
    return model.predict([[year] for year in years])

# Load data and train model for world child mortality rate
file_path_world = './main/data_processing/final_data/world-medium.csv'
df_world, lr_model_world, mse_world, r2_world = load_data_and_train_model(file_path_world)

# Read the data from the CSV file for countries
file_path_country = './main/data_processing/final_data/country-medium.csv'
df_country = pd.read_csv(file_path_country, encoding='latin1')

# Read the data from the CSV file for regions
file_path_region = file_path_region = './main/data_processing/final_data/Regionss-medium.csv'
df_region = pd.read_csv(file_path_region, encoding='latin1')

# Read the data from the CSV file for sustainable development goals
file_path_sdg = './main/data_processing/final_data/SDG-medium.csv'
df_sdg = pd.read_csv(file_path_sdg)

# Streamlit app
def main():
    st.title("Child Mortality Prediction")  
    html_temp = """
    <div >
       
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True) 

    st.sidebar.title("Select Data Presentation Option")
    data_options = ['World Child Mortality Rate', 'By Country', 'By Region', 'By Sustainable Development Goal']
    selected_data_option = st.sidebar.radio("", data_options)

    if selected_data_option == 'World Child Mortality Rate':
        # World Child Mortality Rate option
        st.subheader("World Child Mortality Rate")
        st.write(f'Mean Squared Error: {mse_world}')
        st.write(f'R-squared: {r2_world}')

        # User input for year
        selected_year = st.text_input("Enter Year (e.g., 2023.5):")

        if st.button("Predict child mortality"):
            try:
                selected_year = float(selected_year)  # Convert to float
                # Check if the year has a fractional part
                if selected_year == int(selected_year):
                    st.error("Please enter a fractional year (e.g., 2023.5). Whole numbers are not allowed.")
                elif selected_year < 1985.5 or selected_year > 2041.5:
                    st.error("Year is out of range. Please select a year between 1985.5 and 2041.5.")
                else:
                    # Predict mortality rate for the specified year
                    mortality_prediction = make_predictions(lr_model_world, [selected_year])[0]
                    st.write(f"Predicted Mortality Rate for the world in {selected_year}: {mortality_prediction}")
            except ValueError:
                st.warning("Please enter a valid year.")
    elif selected_data_option == 'By Country':
        # User input for country and year
        selected_country = st.selectbox("Select Country", df_country['Country.Name'].unique())
        selected_year_country = st.text_input("Enter Year (e.g., 2023.5):")

        if st.button("Predict child mortality"):
            try:
                selected_year_country = float(selected_year_country)
                if selected_year_country < 2021.5 or selected_year_country > 2041.5:
                    st.error("Year is out of range. Please select a year between 2021.5 and 2041.5.")
                else:
                    # Get the predicted mortality rate for the selected country and year
                    base_year = 2021.5
                    country_data = df_country[df_country['Country.Name'] == selected_country]
                    mortality_prediction_base = country_data[str(base_year)].values[0]
                    decay_factor = 0.95 ** (selected_year_country - base_year)
                    mortality_prediction_country = mortality_prediction_base * decay_factor
                    st.write(f"Predicted Mortality Rate for {selected_country} in {selected_year_country}: {mortality_prediction_country}")
            except ValueError:
                st.warning("Please enter a valid year.")
    elif selected_data_option == 'By Region':
        # User input for region and year
        selected_region = st.selectbox("Select Region", df_region['Region.Name'].unique())
        selected_year_region = st.text_input("Enter Year (e.g., 2023.5):")

        if st.button("Predict child mortality"):
            try:
                selected_year_region = float(selected_year_region)
                if selected_year_region < 2021.5 or selected_year_region > 2041.5:
                    st.error("Year is out of range. Please select a year between 2021.5 and 2041.5.")
                else:
                    # Get the predicted mortality rate for the selected region and year
                    base_year = 2021.5
                    region_data = df_region[df_region['Region.Name'] == selected_region]
                    mortality_prediction_base = region_data[str(base_year)].values[0]
                    decay_factor = 0.95 ** (selected_year_region - base_year)
                    mortality_prediction_region = mortality_prediction_base * decay_factor
                    st.write(f"Predicted Mortality Rate for {selected_region} in {selected_year_region}: {mortality_prediction_region}")
            except ValueError:
                st.warning("Please enter a valid year.")

    elif selected_data_option == 'By Sustainable Development Goal':
        # User input for region and year
        selected_region = st.selectbox("Select Region", df_sdg['Region.Name'].unique())
        selected_year_region = st.text_input("Enter Year (e.g., 2023.5):")

        if st.button("Predict child mortality"):
            try:
                selected_year_region = float(selected_year_region)
                if selected_year_region < 2021.5 or selected_year_region > 2041.5:
                    st.error("Year is out of range. Please select a year between 2021.5 and 2041.5.")
                else:
                    base_year = 2021.5
                    region_data = df_sdg[df_sdg['Region.Name'] == selected_region]  
                    mortality_prediction_base = region_data[str(base_year)].values[0]
                    decay_factor = 0.95 ** (selected_year_region - base_year)
                    mortality_prediction_region = mortality_prediction_base * decay_factor
                    st.write(f"Predicted Mortality Rate for {selected_region} in {selected_year_region}: {mortality_prediction_region}")
            except ValueError:
                st.warning("Please enter a valid year.")

if __name__ == "__main__":
    main()
