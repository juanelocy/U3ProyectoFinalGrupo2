import pywhatkit as kit

# Número de teléfono del destinatario (debe incluir el código de país)
ingreso_numero = input ("Ingrese el numero del destinatario (10 digitos): ")
numero_destinatario = "+593"+ingreso_numero

# Mensaje que deseas enviar
mensaje = input("Ingrese el mensaje a enviar: ")

# Hora en la que deseas enviar el mensaje (formato: HH:MM)
hora_envio = input("Ingrese la hora para enviar el mensaje (Formato 24h, HH:MM): ")

# Enviar el mensaje por WhatsApp
kit.sendwhatmsg(numero_destinatario, mensaje, int(hora_envio.split(":")[0]), int(hora_envio.split(":")[1]))