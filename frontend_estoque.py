import tkinter as tk
from tkinter import ttk, messagebox
import requests

# URL da sua API. Certifique-se de que o IP do servidor está correto.
# Exemplo: se o servidor for 192.168.1.5, a URL seria "http://192.168.1.5:8000/api/products"
API_URL = "http://127.0.0.1:8000/api/products"

# Nome do Estabelecimento (pode ser alterado facilmente aqui)
ESTABLISHMENT_NAME = "CIATRON COMPONENTES"


#Busca todos os produtos da API e retorna como uma lista de dicionários.
def get_all_products():
    
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança um erro para status de erro (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar à API: {e}")
        return []

def show_products():
    #Limpa a tabela e preenche com os dados da API."""
    products = get_all_products()
    if not products:
        return

    # Limpar a tabela
    for item in product_tree.get_children():
        product_tree.delete(item)

    # Preencher a tabela com os produtos
    for product in products:
        product_tree.insert('', tk.END, values=(product['id'], product['name'], product['description'], product['price'], product['stock_quantity']))
    
def save_product():
    #Adiciona ou atualiza um produto no banco de dados via API.#
    try:
        # Ponto de validação no frontend
        name = name_entry.get()
        desc = desc_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()

        if not name or not desc or not price or not stock:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Erro de Validação", "Preço deve ser um número e Quantidade deve ser um número inteiro!")
            return
            
        product_data = {
            "name": name,
            "description": desc,
            "price": price,
            "stock_quantity": stock
        }

        product_id = id_entry.get()

        if product_id == "Novo":
            response = requests.post(API_URL, json=product_data)
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        else:
            response = requests.put(f"{API_URL}/{product_id}", json=product_data)
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        
        response.raise_for_status()
        show_products()
        clear_fields()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao processar a requisição: {e}")
def delete_product():
    #Exclui o produto selecionado na tabela via API."""
    selected_item = product_tree.selection()
    if not selected_item:
        messagebox.showwarning("Atenção", "Selecione um produto para excluir.")
        return
    
    confirm = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este produto?")
    if confirm:
        item_id = product_tree.item(selected_item, 'values')[0]
        try:
            response = requests.delete(f"{API_URL}/{item_id}")
            response.raise_for_status()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            show_products()
            clear_fields()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir produto: {e}")

def load_product_to_form(event):
    #Carrega os dados do produto selecionado na tabela para o formulário."""
    selected_item = product_tree.selection()
    if not selected_item:
        return
    
    values = product_tree.item(selected_item, 'values')
    
    id_entry.config(state='normal')
    id_entry.delete(0, tk.END)
    id_entry.insert(0, values[0])
    id_entry.config(state='readonly')
    
    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[1])
    
    desc_entry.delete(0, tk.END)
    desc_entry.insert(0, values[2])
    
    price_entry.delete(0, tk.END)
    price_entry.insert(0, values[3])
    
    stock_entry.delete(0, tk.END)
    stock_entry.insert(0, values[4])

def clear_fields():
    #Limpa todos os campos de entrada do formulário."""
    id_entry.config(state='normal')
    id_entry.delete(0, tk.END)
    id_entry.insert(0, "Novo")
    id_entry.config(state='readonly')
    name_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

# --- Configuração da Janela Principal ---
root = tk.Tk()
root.title(f"Sistema de Controle de Estoque | {ESTABLISHMENT_NAME}")
root.geometry("1000x600")

# --- Estrutura da Interface ---
# Frame para o formulário de cadastro
form_frame = ttk.LabelFrame(root, text="Cadastrar/Atualizar Produto", padding=10)
form_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Frame para a tabela de produtos
list_frame = ttk.LabelFrame(root, text="Produtos em Estoque", padding=10)
list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Componentes do Formulário ---
ttk.Label(form_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
id_entry = ttk.Entry(form_frame, width=10)
id_entry.grid(row=0, column=1, padx=5, pady=5)
id_entry.insert(0, "Novo")
id_entry.config(state='readonly') # ID é apenas para visualização

ttk.Label(form_frame, text="Nome:").grid(row=0, column=2, padx=5, pady=5)
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_frame, text="Descrição:").grid(row=0, column=4, padx=5, pady=5)
desc_entry = ttk.Entry(form_frame, width=40)
desc_entry.grid(row=0, column=5, padx=5, pady=5)

ttk.Label(form_frame, text="Preço:").grid(row=1, column=0, padx=5, pady=5)
price_entry = ttk.Entry(form_frame, width=15)
price_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Quantidade:").grid(row=1, column=2, padx=5, pady=5)
stock_entry = ttk.Entry(form_frame, width=15)
stock_entry.grid(row=1, column=3, padx=5, pady=5)

# --- Botões de Ação ---
add_button = ttk.Button(form_frame, text="Adicionar", command=save_product)
add_button.grid(row=1, column=4, padx=5, pady=5)

update_button = ttk.Button(form_frame, text="Atualizar", command=save_product)
update_button.grid(row=1, column=5, padx=5, pady=5)

delete_button = ttk.Button(form_frame, text="Excluir", command=delete_product)
delete_button.grid(row=1, column=6, padx=5, pady=5)

# --- Tabela (TreeView) para Exibir os Produtos ---
columns = ('id', 'name', 'description', 'price', 'stock_quantity')
product_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
product_tree.pack(fill=tk.BOTH, expand=True)

# Ligar o evento de seleção na tabela à função para carregar os dados
product_tree.bind('<<TreeviewSelect>>', load_product_to_form)

# Definição das colunas da tabela
# ... (restante do seu código)


# Definição das colunas da tabela
product_tree.heading('id', text='ID')
product_tree.heading('name', text='Nome')
product_tree.heading('description', text='Descrição')
product_tree.heading('price', text='Preço')
product_tree.heading('stock_quantity', text='Quantidade')

product_tree.column('id', width=50, stretch=tk.NO, anchor='center')
product_tree.column('name', width=200, stretch=tk.NO)
product_tree.column('description', width=300, stretch=tk.YES)
product_tree.column('price', width=100, stretch=tk.NO, anchor='center')
product_tree.column('stock_quantity', width=100, stretch=tk.NO, anchor='center')

# --- Executa a função para carregar os produtos ao iniciar ---
show_products()

# --- Inicia o loop principal da aplicação ---
root.mainloop()

# teste para commit #