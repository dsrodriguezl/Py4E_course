try:
    edad = input("¿Cual es tu edad? (años)",)
    altura = input("¿Cual es tu altura? (metros)")
    
    edad = float(edad)
    altura = float(altura)
except:
    print("Error, ha especificado su edad y/o altura cómo texto")
    print("Por favor, indique un número")

if edad > 8 and altura > 1.4:
    print("Puedes subir a la montaña rusa!!")
    
    if edad < 8:
        print("Lo siento eres demasiado jopven para subir a la montaña rusa :(")
        
        if altura < 1.4:
            print(
                "Lo siento eres demasiado bajo para subir a la montaña rusa :(")


