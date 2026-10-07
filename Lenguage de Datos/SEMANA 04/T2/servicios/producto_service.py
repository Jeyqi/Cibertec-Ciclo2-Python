from datos.productos import productos


def obtener_productos():
    """Devuelve la lista completa de productos."""
    return productos


def buscar_producto_por_codigo(codigo):
    """Busca un producto por su código y lo retorna. Si no lo encuentra, retorna None."""
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def agregar_producto(codigo, nombre, precio, stock):
    """
    Agrega un nuevo producto a la lista.
    Retorna True si se agregó correctamente, o False si el código ya existe.
    """
    if buscar_producto_por_codigo(codigo) is not None:
        return False  # El código ya existe

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(nuevo_producto)
    return True


def eliminar_producto(codigo):
    """
    Elimina un producto por su código.
    Retorna True si logró eliminarlo, o False si no lo encontró.
    """
    producto = buscar_producto_por_codigo(codigo)
    if producto is not None:
        productos.remove(producto)
        return True
    return False