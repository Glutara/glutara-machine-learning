import tensorflow as tf
import pandas as pd

# Load the dataset using pandas
df = pd.read_csv('../data/data_train.csv')
features = df['X'].values.reshape(-1, 1)
labels = df['y'].values

class WeightedKNNModel(tf.Module):

    # Initiate model
    def __init__(self):
        self.training_features = None
        self.training_labels = None

    # Train the model by saving the dataset
    def train(self, training_features, training_labels):
        self.training_features = training_features
        self.training_labels = training_labels

    # Function to predict label using weighted KNN
    @tf.function(input_signature=[tf.TensorSpec(shape=[1,], dtype=tf.float32)])
    def predict(self, input):

        # Calculate distances and sort them
        distances = tf.norm(self.training_features - input, axis=1)
        sorted_indices = tf.argsort(distances)

        # Initialize value of k
        k = 4
        
        # Handle input according to its property
        mask = distances < 1e-5
        if tf.reduce_any(mask):
            # If any point is within epsilon, directly use that point's label
            result = tf.reduce_mean(tf.boolean_mask(self.training_labels, mask))
            result = tf.cast(result, tf.float32)
        else:
            # Otherwise, use weighted KNN. Get the nearest neighbors, and weight their distances
            neighbors = tf.gather(self.training_labels, sorted_indices[:k])
            neighbors_distances = tf.gather(distances, sorted_indices[:k])
            weights = 1.0 / (neighbors_distances + 1e-5) 
            result = tf.reduce_sum(tf.cast(neighbors, tf.float32) * weights) / tf.reduce_sum(weights)

        return tf.reshape(result, [1])

# Create, train, and save the model in Tensorflow SavedModel format
weighted_knn_model = WeightedKNNModel()
weighted_knn_model.train(features, labels)
tf.saved_model.save(weighted_knn_model, "../tensorflow_model/1", signatures={
    "serving_default": weighted_knn_model.predict
})

# Code for testing the model
# result = weighted_knn_model.predict(tf.constant([1.1241], dtype=tf.float32))
# print(result.numpy())