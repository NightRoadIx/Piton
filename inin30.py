# Importar la librería request
import requests

# De request lo que se hace es usar el método get para obtener algún archivo que este en línea
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# Con esto se muestra el resultado
type(res)
# En caso de que se haya localizado el archivo se coloca el código de estátus como OK
res.status_code == requests.codes.ok
# Obtener la longitud del texto leído
len(res.text)
# Mostrar un pedazo del texto localizado
print(res.text[:250])
