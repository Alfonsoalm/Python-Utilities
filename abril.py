import pandas as pd
import random

# Configuración de semilla para reproducibilidad
random.seed(42)

# Definir productos con categorías (asegurándonos de tener 13)
productos = [
    {"Nombre del Producto": "Madera de Pino", "Categoría": "Madera"},
    {"Nombre del Producto": "Madera de Eucalipto", "Categoría": "Madera"},
    {"Nombre del Producto": "Madera de Roble", "Categoría": "Madera"},
    {"Nombre del Producto": "Pellets", "Categoría": "Biomasa"},
    {"Nombre del Producto": "Astillas", "Categoría": "Biomasa"},
    {"Nombre del Producto": "Biomasa Sólida", "Categoría": "Biomasa"},
    {"Nombre del Producto": "Carbón Vegetal", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Resina Natural", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Compost Orgánico", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Fibras Naturales", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Tableros de Aglomerado", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Tableros de Contrachapado", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Corteza de Árbol", "Categoría": "Productos Derivados"},
    {"Nombre del Producto": "Leña", "Categoría": "Productos Derivados"}
]

# Limitar a 13 productos
productos = productos[:13]

# Asignar Producto ID
for idx, producto in enumerate(productos, start=1):
    producto["Producto ID"] = idx

# Crear DataFrame de Productos con Precio y Costo
productos_df = pd.DataFrame(productos)

# Definir clientes reales
nombres_clientes = [
    "Forestal Iberia S.A.",
    "Maderas del Norte",
    "Biomasa España",
    "EcoTableros S.L.",
    "NaturPellet",
    "Resinas Mediterráneo",
    "Leñas y Astillas SL",
    "Compost y Fibras S.A.",
    "Pellet Power",
    "Maderas del Sur"
]

# Crear DataFrame de Clientes
clientes_df = pd.DataFrame({
    "Cliente ID": range(1, len(nombres_clientes) + 1),
    "Nombre del Cliente": nombres_clientes,
    "Ciudad": [
        "Madrid", "Barcelona", "Sevilla", "Valencia", "Zaragoza",
        "Bilbao", "Málaga", "Murcia", "Palma", "Las Palmas"
    ]
})

# Función para generar ID Pedido
def generar_id_pedido(cliente_id, fecha_pedido, indice):
    fecha_sin_guiones = fecha_pedido.replace("-", "")
    return f"C{cliente_id:02d}-{fecha_sin_guiones}-{indice:03d}"

# Generar Pedidos para Abril
def generar_pedidos_abril():
    pedidos_data = []
    mes_num = 4  # Abril
    for i in range(1, 101):  # 100 pedidos
        cliente_id = random.randint(1, len(nombres_clientes))
        producto_id = random.randint(1, len(productos))
        dia = random.randint(1, 28)
        fecha_pedido = f"2024-{mes_num:02d}-{dia:02d}"
        cantidad = random.randint(1, 100)
        estado_pedido = random.choice(["En Proceso", "Completado", "Cancelado"])
        id_pedido = generar_id_pedido(cliente_id, fecha_pedido, i)
        
        pedidos_data.append({
            "ID Pedido": id_pedido,
            "Fecha de Pedido": fecha_pedido,
            "Cliente ID": cliente_id,
            "Producto ID": producto_id,
            "Cantidad": cantidad,
            "Estado del Pedido": estado_pedido
        })
    return pd.DataFrame(pedidos_data)

# Generar DataFrame de Pedidos de Abril
pedidos_abril_df = generar_pedidos_abril()

# Guardar Pedidos de Abril en CSV
pedidos_abril_df.to_csv("Pedidos_Abril.csv", index=False)

print("Archivo 'Pedidos_Abril.csv' generado correctamente.")
