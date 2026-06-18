# Crear listas
train_losses = [0.9, 0.8, 0.7, 0.6]
model_names = ["ResNet-50", "VGG-16", "Inception-v3"]
mixed_data = [42, 3.14, "Deep Learning", True]

# Acceso por índice a elementos
print(f"Pérdida en la primera época: {train_losses[2]}")
print(f"Pérdida en la última época: {train_losses[-1]}")

# Slicing
first_three_elements = train_losses[:3]
print(f"Primeras tres pérdidas: {first_three_elements}")
last_three_elements = train_losses[-3:]
print(f"Últimas tres pérdidas: {last_three_elements}")