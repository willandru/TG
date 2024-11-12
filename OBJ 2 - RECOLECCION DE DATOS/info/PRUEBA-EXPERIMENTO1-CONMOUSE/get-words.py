import pdfplumber

# Ruta al archivo PDF
pdf_path = 'l5.pdf'

# Abrir el archivo PDF
with pdfplumber.open(pdf_path) as pdf:
    # Extraer texto de cada página
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text()

# Aquí puedes guardar el texto en una estructura, como una lista o archivo
# Por ejemplo, guardar en un archivo de texto
with open('texto_extraido.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)

# Mostrar el texto extraído SIN remoover saltos de linea
print(all_text)



####LIMPEAR LOS DATOS -> remover los saltos de linea
import re

# Procesar el texto para eliminar saltos de línea innecesarios
def clean_text(text):
    # Eliminar saltos de línea dobles
    text = re.sub(r'\n\n+', '\n', text)
    # Reemplazar saltos de línea simples por espacios
    text = re.sub(r'\n+', ' ', text)
    return text.strip()

# Aplicar limpieza al texto extraído
cleaned_text = clean_text(all_text)

# Guardar el texto limpio en un archivo
with open('texto_limpio_5.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_text)
print(cleaned_text)