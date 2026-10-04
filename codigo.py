# PASSO A PASSO DO PROCESSO
# Titulo - Sistema de vendas
# Seção cadastrar - Vendas
    # Campo data
    # Campo vendedor - Ana, Bruno, Carla
    # Campo produto - notebook, fone, celular
    # Campo quantidade
    # Campo valor
    # Botão - Cadstrar Venda
        # quando eu clicar no botão - adicionar na tabela de venda
# Seção Vendas Cadastradas
    # Tabela com as vendas
# Seção Dashboard
    # Card/metrica - Faturamento total
    # Grafico de barra/coluna - venda por vendedor
    # Grafico de pizza - venda por produto


# Ferramentas: pip install Streamlit (site), pandas (base de dados), plotly (criar os graficos) express (graficos pré prontos)
# rodar no terminal streamlit run codigo.py para abrir o site

import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv") #carregar a tabela aqui em cima, pq o codigo roda de cima para baixo


# Titulos das seções + formulário
st.write("# Sistema de Vendas")
# st.sidebar() serve para colocar tudo na barra lateral
st.sidebar.write("## Cadastrar de Vendas")
data = st.sidebar.date_input("data") # cada campo sera uma variavel pq precisamos armazenar as informações no formulario e gerar uma base de dados
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) # colocar a lista de opções
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1) # para os numeros sejam inteiros "step=1"
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")
    # logica de cadastro do botão, aqui tambem pode colocar uma trava de obrigatorio de preenchimento usando uma condicional
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor] #lista do que precisa ser preenchido, srt para o streamlit reconhecer como texto assim como o Pandas reconhece
    ultima_linha = len(tabela_vendas) # sempre olha o tamanho da tabela
    tabela_vendas.loc[ultima_linha] = nova_venda # adiciona o novo cadastro na tabela
    tabela_vendas.to_csv("vendas.csv", index=False) # comando para atualizar a base de dados que já tinhamos em .csv
    st.success("Venda cadastrada!") #mostra uma mensagem de que o botão funcionou no cadastro


st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) #o streamlit puxa as planilhas que o pandas disponibilizou lá em cima no site - pandas ler como texto, streamlit ler como data


st.write("## Dashboard")
    # Card/metrica - Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", faturamento)


    # Grafico de barra/coluna - venda por vendedor (sempre em duas etapas, vc cria dois passo: o grafico e exibe o grafico)
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)


    # Grafico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) #hole é para deixar um "buraco dentro do grafico" = grafico de rosca
st.plotly_chart(grafico2)


#disponibilizar o conteudo online 
    # github = https://github.com/
    # disponibilizar os arquivos que estamos trabalhando no python