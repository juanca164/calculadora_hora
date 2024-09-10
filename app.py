import streamlit as st

def calculo_hora_extra(sueldo_base, horas_extras, horas_trabajadas_semana, recargo_hora):
    DIAS_MES = 30
    DIAS_SEMANA = 28
    SEMANAS_MES = 4
    hora_normal = (sueldo_base / DIAS_MES) * DIAS_SEMANA / (horas_trabajadas_semana * SEMANAS_MES)
    valor_hora_extra = hora_normal * (1 + recargo_hora) * horas_extras
    return valor_hora_extra

st.title("Cálculo de Horas Extras")

sueldo_base = st.number_input("Ingrese el sueldo base mensual", min_value=0.0)
horas_extras = st.number_input("Ingrese cantidad de horas extras trabajadas", min_value=0.0)
horas_trabajadas_semana = st.number_input("Ingrese cuántas horas trabaja a la semana", min_value=0.0)
recargo_hora = st.number_input("Ingrese el recargo por hora extra (por ejemplo, 0.50 para 50%)", min_value=0.0)

if st.button("Calcular"):
    valor_hora_extra = calculo_hora_extra(sueldo_base, horas_extras, horas_trabajadas_semana, recargo_hora)
    st.success(f"El valor total por las horas extras trabajadas es: ${valor_hora_extra:.2f}")
