
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Define input data
input_data = (0,110, 1110, 1230, 1230, 0, 0, 330, 0, 440, 0, 10, 10, 0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make predictions
prediction = loaded_model.predict(input_data_reshaped)

# Set threshold
threshold = 0.5
print(prediction)

# Convert to binary prediction
if prediction > threshold:
    print("most likely to buy the product")
else:
    print("less chances of buying the product")