Importação das Bibliotecas

Importamos streamlit como st para criar a interface web.
qrcode é usado para gerar o QR Code.
PIL (Python Imaging Library) é importado para manipular a imagem gerada do QR Code.
io é utilizado para converter a imagem para um formato de arquivo que possa ser baixado.

Título do App
Usamos st.title('Gerador de QR Code') para definir o título da página.

Entrada de URL
url = st.text_input('Cole sua URL aqui:', placeholder='https://exemplo.com'): Criamos um campo de entrada de texto onde o usuário pode colar a URL para gerar o QR Code.

Gerando o QR Code
Verificamos se o usuário inseriu uma URL (if url:). Se sim:
Criamos o objeto qr = qrcode.QRCode(...), configurando parâmetros como o tamanho da caixa, a correção de erro e a borda.
Usamos qr.add_data(url) para adicionar a URL ao QR Code.
Chamamos qr.make(fit=True) para ajustar o QR Code ao tamanho adequado.
Geramos a imagem com img = qr.make_image(...).

Exibindo a Imagem do QR Code
Convertimos a imagem do QR Code para o formato PIL usando pil_img = img.get_image().
Exibimos o QR Code na interface com st.image(pil_img, caption='Seu QR Code Gerado', use_container_width=True).

Botão de Download
Para permitir o download do QR Code gerado, criamos um arquivo em memória com io.BytesIO().
Usamos pil_img.save(buf, format="PNG") para salvar a imagem gerada no formato PNG no buffer.
Com st.download_button(...), criamos um botão de download que permite ao usuário baixar o QR Code em formato PNG.
