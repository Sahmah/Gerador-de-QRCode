## Importação das Bibliotecas
streamlit como st para criar a interface web.
<div>
qrcode é usado para gerar o QR Code.
<div>
PIL (Python Imaging Library) é importado para manipular a imagem gerada do QR Code.
<div>
io é utilizado para converter a imagem para um formato de arquivo que possa ser baixado.
</div>
  
## Título do App
Usamos st.title('Gerador de QR Code') para definir o título da página.

## Entrada de URL
url = st.text_input('Cole sua URL aqui:', placeholder='https://exemplo.com'): Criamos um campo de entrada de texto onde o usuário pode colar a URL para gerar o QR Code.

## Gerando o QR Code
Verificamos se o usuário inseriu uma URL (if url:). Se sim:
<div>
Criamos o objeto qr = qrcode.QRCode(...), configurando parâmetros como o tamanho da caixa, a correção de erro e a borda.
  <div>
Usamos qr.add_data(url) para adicionar a URL ao QR Code.
    <div>
Chamamos qr.make(fit=True) para ajustar o QR Code ao tamanho adequado.
      <div>
Geramos a imagem com img = qr.make_image(...).
</div>
      
## Exibindo a Imagem do QR Code
Convertemos a imagem do QR Code para o formato PIL usando pil_img = img.get_image().
  <div>
Exibimos o QR Code na interface com st.image(pil_img, caption='Seu QR Code Gerado', use_container_width=True).
</div>

## Botão de Download
Para permitir o download do QR Code gerado, criamos um arquivo em memória com io.BytesIO().
  <div>
Usamos pil_img.save(buf, format="PNG") para salvar a imagem gerada no formato PNG no buffer.
      <div>
Com st.download_button(...), criamos um botão de download que permite ao usuário baixar o QR Code em formato PNG.
</div>
