import streamlit as st
from dados_api import previsao_temperatura

# Cidades
cidades = {
"Santana de Parnaiba" : [-23.44678351765508, -46.91831900177454],
"Saitama" : [35.860756629776105, 139.64480161732098],
"Não-Me-Toque" : [-28.45918282618845, -52.82177167384556],
"Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu" : [-40.34957381466233, 176.55004287282233],
"Anta Gorda" : [-28.97147247722383, -52.00486736474428]
}

#----------------------------------- SIDEBAR
st.sidebar.title("Previsão do tempo")
st.sidebar.image("logo.png")
cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude , longitude = cidades[cidade]

#--------------------------- BODY 
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

# Previsão da temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():
    with st.container(border=True):
        st. subheader(d['dia_semana' ])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura media", f"{d['temperatura_media']:.2f}º")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)