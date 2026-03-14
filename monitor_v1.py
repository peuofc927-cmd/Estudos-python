import urllib.request

def verificar_site(url):
    print(f"Verificando status de: {url}...")
    try:
        # Tenta conectar ao site com um tempo limite de 5 segundos
        status = urllib.request.urlopen(url, timeout=5).getcode()
        if status == 200:
            return "✅ O site está ON-LINE e operando normalmente!"
    except Exception as erro:
        return f"❌ O site está OFF-LINE ou inacessível. (Erro: {erro})"

# --- ÁREA DE TESTE ---
# Vamos testar com o seu portfólio que acabamos de publicar!
meu_site = "https://peuofc927-cmd.github.io/meu-portf-lio/"

print("-" * 40)
resultado = verificar_site(meu_site)
print(resultado)
print("-" * 40)