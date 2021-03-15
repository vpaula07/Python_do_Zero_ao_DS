import pandas as pd

data = pd.read_csv('/home/vanessa/repos/Python_do_Zero_ao_DS/kc_house_data.csv')

#print(data)

# mostra na tela os tipos de variáveis em cada coluna
#print(data.head())

#função que converte de object(string) para date
#data['date'] = pd.to_datetime(data['date'])

# mostra na tela os tipos de variáveis em cada coluna
#print(data.head())

#====================================
#Como converter os tipos de variáveis
#=====================================

#Inteiro -> float
#data['bedrooms'] = data['bedrooms'].astype(float)

#Float -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(int)

#Inteiro -> String
#data['bedrooms'] = data['bedrooms'].astype(str)

#String -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(int)

#print(data.dtypes)

#===========================
#Manipulando as variáveis
#===========================
#Criar(colunas de variáveis e novas linhas)
#Deletar(colunas de variáveis e novas linhas)
#Selecionar: ( 4 formas de selecionas dados):

# Forma 01: Direto pelo nome das colunas
#print(data[['price', 'id', 'date']])

# Forma 02: Pelos índices das linhas e colunas
# dados [ linhas, colunas]
#print(data.iloc[0:5, :])

# Forma 03: Pelos índices das linhas e nome das colunas
#cols = ['price', 'id', 'date']
#print(data.loc[0:10, cols])

#Forma 04: Indíces Booleanos
#print(data.columns)

#cols = [True, True, True, False, False, False, False, False, False, True, False,
        #False, False, False, False, False, False, True, True, False, False]

#print(data.loc[0:10, cols])

#====================================
# Executando o Processo planejado
# Respondendo as perguntas de negócio
#====================================

# 1.Qual a data do imóvel mais antigo no portfólio?
#data['date'] = pd.to_datetime(data['date'])
#print(data.sort_values('date', ascending=True))

# 2. Quantos imóveis possuem o número máximo de andares?
#Encontrar os números de andares e determinar o maior
#Contar quantos imóveis eu tenho por andar

#print(data['floors'].unique())
#print(data['floors']==3.5)
#print(data[data['floors']==3.5][['floors','id']])
#print(data[data['floors']==3.5].shape)


# 3. Criar uma classificação para os imóveis, separando os em baixo e alto padrão,
# de acordo com preço
# Acima de 540.000 -> high standard
# Abaixo de 540.000 -> low standard
#data['level'] = 'standard'
#print(data.columns)
#print(data.head())

data.loc[data['price']>540000, 'level']='high_level'
data.loc[data['price']< 540000, 'level']= 'low_level'
print(data.head())

# 4. Gostaria de um relatório ordenado pelo preço e contento as seguintes informações:
# id do imóvel
# data que o imóvel ficou disponível para compra
# numero de quartos
# tamanho total do terreno
# preço
# Classificação do imóvel(alto/baixo padrão)

#report = data[['id', 'date', 'price', 'bedrooms','sqft_lot', 'level']].sort_values('price', ascending=False)

#print(report.head())

#report.to_csv('report_aula02.csv', index=False)

# 5. Gostaria de um mapa indicando onde as casas estão localizados
# Plotly - Biblioteca que armazena uma função que desenha mapa
# ScatterMapBox - Função que desenha um mapa
import plotly.express as px

data_mapa = data[['id', 'lat','long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat = 'lat', lon = 'long',
                         hover_name= 'id',
                         hover_data = ['price'],
                         color_discrete_sequence=['fuchsia'],
                         zoom=3,
                         height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0,'t':0, 'l':0, 'b':0})
mapa.show()
mapa.write_html('mapa_house_rocket.html')



