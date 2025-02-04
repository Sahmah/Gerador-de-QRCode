#Todo programa tem uma base de dados (ENTRADA)
#Linguagem de programação (PROCESSAMENTO)
#Resultado (SAÍDA)
import streamlit as st
import qrcode
from PIL import Image
import io

st.title('Gerador de QR Code')

url = st.text_input('Cole sua URL aqui:', placeholder='https://exemplo.com')

if url:
    # Gerar QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Converter para formato PIL Image
    pil_img = img.get_image()
    
    # Exibir imagem
    st.image(pil_img, caption='Seu QR Code Gerado', use_container_width=True)
    
    # Criar botão de download
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Baixar QR Code",
        data=byte_im,
        file_name="qrcode.png",
        mime="image/png",
    )



