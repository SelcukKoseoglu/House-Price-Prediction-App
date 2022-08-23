# Import Deep Learning packages
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
  layers.Dense(50, activation='relu', input_dim=24),
  layers.Dense(50, activation='relu', input_dim=64),
  layers.Dense(128, activation='relu', input_dim=128),
  layers.Dense(64, activation='relu', input_dim=64),
    layers.Dropout(0.2),

  layers.Dense(1, activation='linear')
])


optimizer = tensorflow.keras.optimizers.Adam(
    learning_rate=0.01)

model.compile(loss='mse', optimizer=optimizer)

model.load_weights('./weights/weights_final.h5')



