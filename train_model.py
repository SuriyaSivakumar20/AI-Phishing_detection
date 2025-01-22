import tensorflow as tf
from sklearn.model_selection import train_test_split

def build_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    from preprocess import preprocess_data
    features, labels = preprocess_data("data/processed/urls_features.csv")
    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2)

    model = build_model(X_train.shape[1:])
    model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
    model.save("models/phishing_model.h5")
    print("Model trained and saved successfully!")
