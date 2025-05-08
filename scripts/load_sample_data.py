#!/usr/bin/env python
"""
Script para cargar datos de ejemplo en la base de datos.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.db import get_db_connection, init_db

def cargar_datos_ejemplo():
    print("Inicializando base de datos...")
    init_db()
    
    productos = [
        ('001', 'Detergente Líquido 1L', 15.50, '/static/images/detergente.jpg'),
        ('002', 'Jabón en Polvo 500g', 8.75, '/static/images/jabon_polvo.jpg'),
        ('003', 'Suavizante Floral 750ml', 12.30, '/static/images/suavizante.jpg'),
        ('004', 'Limpiador Multiuso 500ml', 7.80, '/static/images/limpiador.jpg'),
        ('005', 'Desinfectante Lavanda 1L', 9.25, '/static/images/desinfectante.jpg'),
        ('006', 'Limpiavidrios 500ml', 6.90, '/static/images/limpiavidrios.jpg'),
        ('007', 'Esponja Doble Uso Pack x3', 3.75, '/static/images/esponjas.jpg'),
        ('008', 'Trapo de Piso', 5.20, '/static/images/trapo_piso.jpg'),
        ('009', 'Lustra Muebles 300ml', 8.40, '/static/images/lustra_muebles.jpg'),
        ('010', 'Cloro 1L', 4.90, '/static/images/cloro.jpg'),
        ('011', 'Insecticida Aerosol 400ml', 11.80, '/static/images/insecticida.jpg'),
        ('012', 'Papel Higiénico Pack x4', 7.30, '/static/images/papel_higienico.jpg'),
        ('013', 'Servilletas de Papel x50', 2.95, '/static/images/servilletas.jpg'),
        ('014', 'Bolsas de Basura x10', 3.50, '/static/images/bolsas_basura.jpg'),
        ('015', 'Desodorante para Baño', 5.75, '/static/images/desodorante_banio.jpg')
    ]
    
    print(f"Cargando {len(productos)} productos de ejemplo...")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM productos")
        
        for producto in productos:
            codigo, nombre, precio, imagen = producto
            cursor.execute(
                """
                INSERT INTO productos (codigo, nombre, precio, imagen)
                VALUES (%s, %s, %s, %s)
                """,
                (codigo, nombre, precio, imagen)
            )
        
        conn.commit()
        print(f"Se cargaron {len(productos)} productos correctamente.")
        
    except Exception as e:
        conn.rollback()
        print(f"Error al cargar datos: {e}")
        
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    cargar_datos_ejemplo() 