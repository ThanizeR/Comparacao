from tensorflow.keras.models import load_model

# Carregar o modelo
model = load_model("pneumonia.h5")

# Exibir a arquitetura do modelo
model.summary()
