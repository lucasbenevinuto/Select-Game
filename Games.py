import pandas as pd
pd.option_context('display.max_columns', None, 'display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)
games = pd.read_csv('vgsales.csv')
games = games.loc[:, ['Name', 'Platform', 'Year', 'Genre', 'Publisher']]
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def menu_plataform():
    esc = selected_platform.get()
    
    if esc == "Todos":
        result_df = gamesg
    else:
        result_df = gamesg.loc[games['Platform'] == esc]

def menu_genero():
    genre_name = selected_genre.get()
    esc = genre_mapping[genre_name]

    if esc == 13:
        result_df = gamesg
    else:
        selected_genre_name = genre_mapping_inverse[esc]
        result_df = gamesg.loc[gamesg['Genre'] == selected_genre_name]

def exibir_resultado():
    esc_platform = selected_platform.get()
    esc_genre = selected_genre.get()

    if esc_platform == "Todos" and esc_genre == "Todos":
        result_df = gamesg
    elif esc_platform == "Todos":
        selected_genre_name = genre_mapping_inverse[genre_mapping[esc_genre]]
        result_df = gamesg.loc[gamesg['Genre'] == selected_genre_name]
    elif esc_genre == "Todos":
        result_df = gamesg.loc[gamesg['Platform'] == esc_platform]
    else:
        selected_genre_name = genre_mapping_inverse[genre_mapping[esc_genre]]
        result_df = gamesg.loc[(gamesg['Platform'] == esc_platform) & (gamesg['Genre'] == selected_genre_name)]

        # Especificar o caminho do arquivo Excel
    caminho_arquivo_excel = 'jogos.xlsx'

    # Salvar o DataFrame como um arquivo Excel
    result_df.to_excel(caminho_arquivo_excel, index=False)

    text_box.delete(1.0, tk.END)  # Limpa o conteúdo atual da caixa de texto
    text_box.insert(tk.END, result_df) 


# Carregue seu DataFrame gamesg aqui
gamesg = games

platforms = [
    '2600', 'NES', 'PC', 'DS', 'SNES', 'GEN', 'GG', 'NG', 'SCD', 'SAT',
    'PS', '3DO', 'TG16', 'N64', 'PCFX', 'DC', 'WS', 'PS2', 'GBA', 'XB',
    'GC', 'PSP', 'X360', 'PS3', 'Wii', '3DS', 'PSV', 'WiiU', 'PS4', 'XOne', 'Todos'
]

# Dicionário para exibir os gêneros na interface
genre_mapping = {
    'Action': 1, 'Role-Playing': 2, 'Sports': 3, 'Shooter': 4,
    'Misc': 5, 'Fighting': 6, 'Platform': 7, 'Simulation': 8,
    'Racing': 9, 'Puzzle': 10, 'Adventure': 11, 'Strategy': 12, 'Todos': 13
}

# Cria o dicionário inverso para mapear números de volta para os nomes dos gêneros
genre_mapping_inverse = {v: k for k, v in genre_mapping.items()}

# Cria a janela principal
root = tk.Tk()
root.title("GAME FOR YOU")

# Cria uma label
label = tk.Label(root, text="Esse programa vai selecionar sua plataforma e genero de desejo e vai disponibilizar uma tabela em excel para uma melhor consulta \n Escolha um gênero e plataforma:")
label.pack()

# Cria opções de gênero usando um combobox (caixa de seleção)
selected_genre = tk.StringVar()
selected_platform = tk.StringVar()
genre_combobox = ttk.Combobox(root, textvariable=selected_genre, values=list(genre_mapping.keys()))
genre_combobox.pack()
platform_combobox = ttk.Combobox(root, textvariable=selected_platform, values=platforms)
platform_combobox.pack()


# Cria um botão para confirmar a escolha
botao = tk.Button(root, text="Exibir Resultado", command=exibir_resultado)
botao.pack()

# Cria uma caixa de texto com barra de rolagem para exibir o DataFrame
text_box = ScrolledText(root, width=150, height=40)
text_box.pack()

# Inicia o loop principal da interface
root.mainloop()
