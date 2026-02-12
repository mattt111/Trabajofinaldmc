import streamlit as st

if 'opcion' not in st.session_state:
    st.session_state.opcion = "Home"  #Para que comienze en Home siempre que se abra
    st.sidebar.write("Selecciona una opción:")
Opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"]
)
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("Elaborador por:")
st.sidebar.write("Matt Arribasplata")
# home

if Opcion == "Home":
    # se crea 3 columnas para poder centrar la informacion
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Informacion del centro
        st.markdown("---")
        st.title("       Trabajo Final       ")
        st.markdown("---")
        st.write("Nombre Completo:Matt Patrick Arribasplata Mas")
        st.write("Nombre del curso o modulo:Python Fundamentals")
        st.write("Año: 2026")
        st.write(" Descripcion del trabajo:Este trabajo final pone aprueba todo lo que se aprendio en las 6 sesiones que vio.")
        st.write("Lista de tecnologías utilizadas:Se esta haciendo uso de Python, Streamlit")

#Haciendo el ejercicio 1

elif Opcion == "Ejercicio 1" :
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2 :
     st.markdown("---")
     st.title("Ejecicio 1")
     st.write("Verificador de presupuesto")
     st.markdown("---")   
        # Solicitud del presupuesto y gasto 
     presupuesto = st.number_input("Ingrese su presupuesto total:", min_value=0.0, step=100.0)
    gasto = st.number_input("Ingrese el gasto realizado:", min_value=0.0, step=100.0)
        
        #  Botón para ejecutar los valores
    if st.button("Evaluar Presupuesto"):
            diferencia = presupuesto - gasto
            # mensajes segun los resultados
            if gasto <= presupuesto:
                st.success(f"Esta bien estas dentro de tu Presupuesto")
                st.write(f"Te sobra: **{diferencia}**")
            else:
                st.warning(f"Aviso te estas excediendo")
                st.write(f"Por la cantidad de: {diferencia}")
#Resolviendo el ejercicio 2

elif Opcion == "Ejercicio 2":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2 :
        st.markdown("---")
        st.title("Ejercicio 2")
        st.markdown("---")
    st.header("Listas y Diccionarios")
    st.write("Registra tus actividades financieras y evalua tu presupuesto")
    st.markdown("---")

    # se hace la lista de memoria que almacenara todo
    if 'lista_actividades' not in st.session_state:
        st.session_state.lista_actividades = []

    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input("Nombre :",placeholder="Escribir aqui...")
        tipo = st.selectbox("Tipo:", ["Ingreso", "Gasto", "Inversión"])
    
    with col2:
        presupuesto = st.number_input("Presupuesto:", min_value=0.0, step=100.0)
        gasto_real = st.number_input("Gasto Real:", min_value=0.0, step=100.0)

    # Boton para la actividad 
    if st.button("Agregar Actividad"):
        nueva_actividad = {
            "Nombre": nombre,
            "Tipo": tipo,
            "Presupuesto": presupuesto,
            "Gasto Real": gasto_real
        }
        # Se añade en su memoria
        st.session_state.lista_actividades.append(nueva_actividad)
        st.success(f"Actividad '{nombre}' agregada correctamente.")

    st.markdown("---")

    # Mostrar la lista y evaluar los resultados 
    if st.session_state.lista_actividades:
        st.subheader (" Registro de Actividades")
        st.dataframe (st.session_state.lista_actividades)

        st.subheader(" Evaluación de Presupuesto")
        for actividad in st.session_state.lista_actividades :
            nombre_act = actividad["Nombre"]
            presupuestoparalalista =    actividad["Presupuesto"]
            gasto = actividad["Gasto Real"]
            
            diferencia = presupuestoparalalista - gasto

            if gasto <= presupuestoparalalista:
                st.success(f"✅ {nombre_act}: Cumple el presupuesto. (Sobra: {diferencia})")
            else:
                st.error(f"❌ {nombre_act}: Excedió el presupuesto. (Faltó: {abs(diferencia)})")
    else:
        st.info("Aún no has agregado ninguna actividad.")
        
        # Ejercicio 3

elif Opcion == "Ejercicio 3":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2 :
        st.markdown("---")
        st.title("Ejercicio 3")
        st.markdown("---")
        st.header("Funciones y Programación Funcional")
        st.markdown("---")

        def calcular_retorno(actividad, tasa, meses):
        # la formula
         retorno = actividad["Presupuesto"] * (tasa / 100) * meses
         return retorno

    # donde quiero que las celdas de interes y cantidad de meses
    col1, col2 = st.columns(2)
    with col1:
        tasa = st.number_input("Tasa de interés mensual (%):", min_value=0.0, value=1.0, step=0.1)
    with col2:
        meses = st.number_input("Cantidad de meses:", min_value=1, value=12, step=1)

    # Boton para el calculo
    if st.button("Calcular Retorno de Inversión"):
        
        # Verificamos si existen actividades registradas en la memoria
        if 'lista_actividades' not in st.session_state or len(st.session_state.lista_actividades) == 0:
            st.warning("No hay actividades registradas.  Ve al Ejercicio 2 y agrega algunas")
        else:
            # El programa funcional y se usa map y lambda
            resultados = list(map(
                lambda act: calcular_retorno(act, tasa, meses), 
                st.session_state.lista_actividades
            ))
            
            st.success("Cálculo realizado correctamente")
            st.markdown("Resultados Proyectados:")

 # Mostramos los resultados con la lista original de los calculos

            for i, actividad in enumerate(st.session_state.lista_actividades):
                nombre = actividad["Nombre"]
                presupuesto_original = actividad["Presupuesto"]
                ganancia = resultados[i]            
                st.write(f" {nombre} (Inversión: {presupuesto_original})")
                st.info(f" Retorno esperado en {meses} meses:  S/ {ganancia:.2f}")

#Ejercicio 4

elif Opcion == "Ejercicio 4":
    st.header("Programación Orientada a Objetos")
    st.markdown("---")
#La clase

    class Nombreclase:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
 


        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        # Resumen de la actividad
        def mostrar_info(self):

            estado = "Dentro del presupuesto" if self.esta_en_presupuesto() else "Presupuesto excedido"
            return f"Actividad: {self.nombre} | Tipo: {self.tipo} | Estado: {estado}"
    # proceso de los datos
    if 'lista_actividades' not in st.session_state or not st.session_state.lista_actividades:
        st.warning(" No hay datos.registra actividades en el Ejercicio 2")
    else:
        st.subheader("Listado de Objetos creados:")

        # convertir los diccionario sen objetos
        for datos in st.session_state.lista_actividades:


            obj_actividad = Nombreclase(
                datos["Nombre"], 
                datos["Tipo"], 
                datos["Presupuesto"], 
                datos["Gasto Real"]
            )
            # se usa los métodos de la clase para mostrar la info 

            resumen = obj_actividad.mostrar_info()
            if obj_actividad.esta_en_presupuesto():
                st.success(resumen) # verde si cumple 

            else:
                st.warning(resumen) # amarillo si excede 
            # Detalle adicional

            st.write(f"Presupuesto: {obj_actividad.presupuesto} | Gasto: {obj_actividad.gasto_real}")

            st.markdown("---")


