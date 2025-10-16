
import tkinter as tk
from tkinter import messagebox
import ipaddress
import sys

def calcular_subrede():
    try:
        ip_str = entry_ip.get()  # Obtém o IP do campo de entrada
        cidr_str = entry_cidr.get()  # Obtém o CIDR do campo de entrada
        
        if not ip_str or not cidr_str:
            messagebox.showerror("Erro", "Preencha ambos os campos!")
            return
        
        rede = ipaddress.ip_network(f"{ip_str}/{cidr_str}", strict=False)
        
        resultado = f"""
        --- Informações da Sub-rede ---
        Endereço de Rede: {rede.network_address}
        Endereço de Broadcast: {rede.broadcast_address}
        Máscara de Sub-rede: {rede.netmask}
        Prefixo CIDR: {rede.with_prefixlen}
        Número de IPs totais na rede: {rede.num_addresses}
        Número de hosts utilizáveis: {rede.num_addresses - 2}
        Faixa de IPs utilizáveis: {list(rede.hosts())[:10]}... (e mais)
        """
        
        messagebox.showinfo("Resultado", resultado)  # Exibe o resultado em uma caixa de diálogo
    
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro: {e}. Verifique o IP e CIDR.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de Sub-redes IP")

# Labels e entradas
tk.Label(root, text="Endereço IP (ex: 192.168.1.0):").pack()
entry_ip = tk.Entry(root, width=30)
entry_ip.pack()

tk.Label(root, text="Prefixo CIDR (ex: 24):").pack()
entry_cidr = tk.Entry(root, width=30)
entry_cidr.pack()

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_subrede)
btn_calcular.pack()

# Inicia a janela
root.mainloop()
