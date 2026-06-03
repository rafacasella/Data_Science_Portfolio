import asyncio
import re
from datetime import datetime
from urllib.parse import urljoin  # Força a montagem correta de URLs independentemente do encoding
from playwright.async_api import async_playwright

#Configurações iniciais:
username = "realDonaldTrump"
lista_palavras = ["Iran", "conflict", "Hormuz", "oil", "taxes", "tariffs"]
intervalo_checagem = 67

async def monitorar_truth_social():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Inicializando monitoramento...")

    # Montagem matemática/estrutural da URL para burlar bugs
    base_site = "https://truthsocial.com"
    caminho_perfil = f"@{username}"

    # O urljoin garante por padrão a inserção da barra de separação de diretório
    url_perfil = urljoin(base_site + "/", caminho_perfil)

    # Duplo fator de checagem física de strings
    if "com/@" not in url_perfil:
        print("⚠️ Corrigindo dinamicamente falha de encoding do interpretador...")
        url_perfil = "https://truthsocial.com" + chr(47) + f"@{username}" # chr(47) é o código ASCII exato da barra '/'
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Nova URL forçada via tabela ASCII: {url_perfil}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )

        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        page = await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        dados_rede = {"posts": []}

        async def capturar_resposta(response):
            if "/api/v1/accounts/" in response.url and "/statuses" in response.url:
                try:
                    json_dados = await response.json()
                    if isinstance(json_dados, list):
                        dados_rede["posts"] = json_dados
                except Exception:
                    pass

        page.on("response", capturar_resposta)
        ultimo_id_visto = None

        while True:
            try:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Enviando requisição para: {url_perfil}")
                dados_rede["posts"] = []

                await page.goto(url_perfil, wait_until="domcontentloaded", timeout=35000)
                await page.wait_for_timeout(6000)

                novos_posts_detectados = []

                if dados_rede["posts"]:
                    for post in dados_rede["posts"]:
                        id_post = str(post.get("id"))
                        texto_html = post.get("content", "")
                        texto_limpo = re.sub(r'<[^>]+>', '', texto_html).strip()
                        link_post = post.get("url")

                        if id_post.isdigit():
                            novos_posts_detectados.append({
                                "id": id_post,
                                "texto": texto_limpo,
                                "link": link_post
                            })

                if novos_posts_detectados:
                    novos_posts_detectados.sort(key=lambda x: int(x["id"]))

                    if ultimo_id_visto is None:
                        ultimo_id_visto = novos_posts_detectados[-1]["id"]
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sincronizado com sucesso via API!")
                        print(f"Monitorando termos: {lista_palavras}\n")
                        await asyncio.sleep(intervalo_checagem)
                        continue

                    for post in novos_posts_detectados:
                        if int(post["id"]) > int(ultimo_id_visto):
                            texto_minusculo = post["texto"].lower()
                            termo_encontrado = [p for p in lista_palavras if p.lower() in texto_minusculo]

                            if termo_encontrado:
                                print(f"\n📢 [ALERTA DETECTADO] [{datetime.now().strftime('%H:%M:%S')}]")
                                print(f"Termos acionados: {termo_encontrado}")
                                print(f"Texto puro:\n{post['texto']}")
                                print(f"Link: {post['link']}")
                                print("-" * 50)

                            ultimo_id_visto = post["id"]
                else:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Feed verificado. Aguardando novas postagens...")

            except Exception as e:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Alerta de rede nesta rodada: {e}")

            await asyncio.sleep(intervalo_checagem)

if __name__ == "__main__":
    asyncio.run(monitorar_truth_social())