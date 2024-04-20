import streamlit as st
import pickle

def load_model():
    try:
        model = pickle.load(open('logreg_model.pkl', 'rb'))
        return model
    except FileNotFoundError:
        st.error("Error: Model file not found. Please ensure that 'logreg_model.pkl' exists.")
        return None
    except Exception as e:
        st.error("An error occurred while loading the model:", e)
        return None

def main():
    st.title("Machine Learning Model Demo")
    
    model = load_model()
    if model is not None:
        # Use the model for predictions
        st.write("Model loaded successfully!")
        # Your code to use the model goes here

if __name__ == "__main__":
    main()
