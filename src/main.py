import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset using Pandas
dataset = pd.read_csv('../data/data_train.csv')

# Get the features and target
X = dataset['X'].values.reshape(-1, 1) 
y = dataset['y'].values.reshape(-1, 1) 

# Split into training and validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=42)
print(y_val)
# Define the model 
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,), name='dense_layer')
])

# Compile model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Training
model.fit(X_train, y_train, epochs=1000, batch_size=10, validation_data=(X_val, y_val))

# Check training result
predictions = model.predict(X_val)

# Print the first few predictions
print("Predictions:")
for i in range(len(X_val)):
    print(f"Input: {X_val[i][0]}, Prediction: {predictions[i][0]}, True Label: {y_val[i][0]}")

# Export the model as a SavedModel
export_dir = '../tensorflow_model/1'

# Define a serving function for the SavedModel
@tf.function(input_signature=[tf.TensorSpec(shape=[None, 1], dtype=tf.float32)])
def serving_fn(inputs):
    reshaped_inputs = tf.reshape(inputs, [-1, 1])
    predictions = model(reshaped_inputs)
    return {"output": predictions}

tf.saved_model.save(model, export_dir, signatures={
    "serving_default": serving_fn
})