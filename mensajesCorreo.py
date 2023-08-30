import yagmail

# Credenciales de tu cuenta de correo
sender_email = 'juanchoyasig@gmail.com'
app_password = 'iilkvoephyxeozmu'  # O puedes usar un token OAuth2

# Destinatario del correo electrónico
recipient_email = 'jcyasig2@espe.edu.ec'

# Inicializar yagmail
yag = yagmail.SMTP(sender_email, app_password)

# Enviar el correo electrónico
subject = 'Asunto del correo'
contents = 'Hola, este es el contenido del correo.'
yag.send(to=recipient_email, subject=subject, contents=contents)

print('Correo enviado con éxito.')

# Cerrar la conexión
yag.close()