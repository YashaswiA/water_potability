import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model_water.pkl')

# Define the Streamlit app
def main():
    # Set the title and description of your app
    st.title('Model Deployment with Streamlit')
    st.write('Enter the required inputs and click the "Predict" button.')

    # Create input fields for user input
    ph = st.number_input('pH:')
    hardness = st.number_input('Hardness:')
    solids = st.number_input('Solids:')
    chloramines = st.number_input('Chloramines:')
    sulfate = st.number_input('Sulfate:')
    conductivity = st.number_input('Conductivity:')
    organic_carbon = st.number_input('Organic_carbon:')
    trihalomethanes = st.number_input('Trihalomethanes:')
    turbidity = st.number_input('Turbidity:')
    # Add more input fields for other features

    # Create a button to trigger the prediction
    if st.button('Predict'):
        # Prepare the input data
        features = [ph, hardness, solids, chloramines, sulfate, conductivity,    
                    organic_carbon, trihalomethanes, turbidity] 
        # Add more features as per your model
        input_data = np.array(features).reshape(1, -1)

        # Make predictions using the loaded model
        prediction = model.predict(input_data)

        # Display the prediction result
        if prediction == 0:
            st.write('Prediction: Not Potable')
        else:
            st.write('Prediction: Potable')

# Run the Streamlit app
if __name__ == '__main__':
    main()
