#DEFINICION DE VARIABLES DE HISTORIA
El_programa_ha_iniciado = False
elinput1fue__A = False
elinput1fue__B = False
eltextocompartido = False
elinput6fue__A = False
elinput6fue__B = False
elinput2fue__A = False
elinput2fue__B = False
elinput4fue__A = False
elinput4fue__B = False
elinput5fue__A = False
elinput5fue__B = False
elinput3fue__A = False
elinput3fue__B = False

#Segmentos de Texto
Texto1 = (""" 
Diego es un joven de 19 años que vive en la ciudad de Guatemala, de mirada seria y cabello oscuro, 
siempre llevando consigo una libreta repleta de anotaciones y sueños.
Diego proviene de una humilde familia, sus padres Luis y María, han trabajado incansablemente 
para apoyarlo en sus estudios, dentro de él hay una mezcla de emociones, ya que esta a punto de 
comenzar a ir a la universidad.

Ahora que Diego ha crecido quiere apoyar a sus papás, siente que es hora de asumir parte de la responsabilidad 
financiera, quiere aliviar la carga de sus padres y demostrarles que su esfuerzo valdría la pena.
""")
Input1_es_A = ("""
Entonces Diego Inicio sus clases 2 días después, el primer día de clases recibió las instrucciones y 
toda la información acerca de el horario, clases, maestros y exámenes. 
Pero aun tenia que conseguir un trabajo pronto.
""")
Texto2compartido = ("""
La búsqueda de trabajo resultó ser un camino lleno de obstáculos. Diego enviaba currículums una y otra vez, 
pero los correos sin respuesta y las puertas cerradas lo hacían cuestionar sus habilidades. 
La decepción lo atormentaba, y en las noches, mientras el silencio llenaba su habitación, a veces se preguntaba 
si podría cumplir con sus responsabilidades financieras y académicas. 

Hubo momentos en que tuvo que renunciar a salir con amigos o disfrutar de pequeños placeres para ahorrar. 
Se encontraba con problemas como comprar libros y comida con el dinero que llevaba a punto de acabarse, 
además de sus gastos diarios. Afortunadamente sus padres le daban para el alquiler.

A pesar de los momentos difíciles, Diego siguió luchando. Cada mañana, se miraba en el espejo y se recordaba 
a sí mismo que era capaz. Siguió asistiendo a clases, entregando currículums por todos lados.

Un día, mientras repartía currículums en una avenida comercial, Diego se encontró con Mateo, un joven 
emprendedor que estaba buscando un colaborador para su negocio de marketing digital. 
Mateo quedó impresionado por la determinación y el entusiasmo de Diego. Le ofreció un trabajo a tiempo parcial 
que le permitiría aplicar sus habilidades y ganar experiencia en el mundo real.
""")
Input1_es_B = ("""
Armado con una camisa bien planchada y currículum en mano, Diego decide comenzar su búsqueda de trabajo. 
Su primer intento es una panadería/cafetería que solicitaba un cajero, hace su prueba pero desafortunadamente 
le solicitan que necesita 2 meses de experiencia y algunos trabajos de contabilidad básica, 
Diego cumple con el segundo requisito pero necesita experiencia.
""")
Input6_es_A = ("""
Aunque esto significaba aún más dedicación de tiempo entre sus compromisos, Diego aceptó, sabiendo que esto 
podría beneficiarlo en el futuro.
Con el paso del tiempo se fueron conociendo mejor y se hicieron amigos muy rápidamente, resulto que Mateo 
estaba estudiando administración de empresas en la misma universidad en la que diego estudiaba diseño grafico.
El trabajo de Diego ayudo al crecimiento del negocio de Mateo y entonces se convirtieron en socios expandiendo 
el negocio a una pequeña empresa con trabajadores que operaba principalmente por redes sociales.
""")
Input6_es_B = ("""
No le inspiro confianza ya que sonaba bastante bueno para ser real, además era casi de su edad. 
Probablemente era una estafa o algo peor, fuera asi o no en esa semana se le acabo el dinero a Diego y tubo 
que regresar a casa de sus padres ya que no tenia dinero para subsistir solo.
Y desde ahí viaja en camioneta hasta la universidad todos los días hasta que mejore su situación.
""")
Input2_es_A = ("""
Visito tiendas y oficinas, enfrentando tanto rechazos como miradas juzgonas. Cada rechazo era un recordatorio 
de lo competitivo que era el mundo laboral, pero Diego no cedió ante la adversidad.
Llego a un taller de carpintería donde el encargado le dio su numero y le dijo que volviera mañana.
""")
Input2_es_B = ("""
Molesto y triste regreso a casa sin nada, se sentó en su escritorio y se puso a jugar en la computadora hasta 
que le dio hambre y luego se durmió. Paso 2 días sin salir de su casa, durante las noches, se sentaba en su 
escritorio, revisando su currículum una y otra vez, ajustando cada palabra para impresionar a los jefes.

Un día Diego se encontraba esperando la camioneta porque quedo en encontrarse con unos amigos para comer, 
mientras el esperaba llego una mujer a sentarse junto a el en la parada.
""")
Input4_es_A = ("""
Ese dia iniciaron sus clases en la universidad, recibió las instrucciones y toda la información. 
En la tarde paso con el señor para platicar. El le dijo que le ofrecía que empezara como acomodador, es decir 
su trabajo consistiría en acomodar los troncos, tablas y palos donde fuera necesario junto con otros 
acomodadores, si el demostraba de lo que era capaz, podría ser ascendido a otro puesto.
""")
Input4_es_B = ("""
Ese día iniciaron sus clases en la universidad, recibió las instrucciones y toda la información. 
En la tarde regreso a casa, ya no fue a ver lo del trabajo.
""")
Elotrotextocompartido = ("""
Decidió que mejor no, no era algo en lo que de verdad quisiera trabajar 
asi que era mejor esperar a otra oportunidad
""")
Input5_es_A = ("""
Paso 2 semanas como acomodador y por su buen trabajo su jefe, don Omar le pregunto que sabia hacer, 
entonces Diego le relato lo que decía su curriculum, finalmente obtuvo un trabajo a tiempo parcial como 
gerente en la tienda del aserradero. El alivio inundó su corazón, pero también sabía que su camino estaba 
lejos de ser fácil, era solo el comienzo.
""")
Input3_es_A = ("""
Tras una conversación casual, Diego descubrió que su nombre era Alejandra, era gerente de una exitosa empresa 
de publicidad. Impresionada por la dedicación y la pasión de Diego, Alejandra le ofreció una semana de prueba 
no remunerada en su empresa. Aunque no estaba seguro de cómo podría manejarlo junto con sus clases, Diego 
aceptó sabiendo que esta era una oportunidad que no podía dejar pasar. Y la acompaño a conocer el lugar 
disculpándose con sus amigos porque ya no llegaría.
               
Comenzó la universidad al mismo tiempo que trabajaba en la prueba de testeo, durante la semana estuvo 
asistiendo a clases, sacrificando horas de sueño por un futuro mejor. 
Termino la semana y consiguió trabajo como creador de anuncios publicitarios y se encarga de hacer estudios 
estadísticos. Ahora el estudia y trabaja feliz.
""")
Input3_es_B = ("""
Diego subió a la camioneta que lo llevo hasta la zona 1, donde a unas cuadras de bajar sufrió un asalto. 
Dos hombres se le acercaron, exigiendo su teléfono y dinero, el se resistió y desafortunadamente 
lo asesinaron apuñalándolo.
""")
#no hay texto de input 5 es b porque todo eso agara de los textos compartidos entre 3 lineas temporales

#                                INICIO DEL PROGRAMA
print (""" 
GENERADOR DE HISTORIA INTERACTIVA
Instrucciones: Se te presentara una historia en la que tendras que elegir las decisiones del protagonista.
               Cada vez que tomes una decisión, la historia se desarrollara de manera diferente. 
               "Las decisiones que tomes repercutiran en el futuro"   
               *IMPORTANTE* Amplia la terminal lo mas posible para ver mejor""")

Iniciar_Historia = (input("Comenzamos?   "))
if Iniciar_Historia == "si" or Iniciar_Historia == "SI" or Iniciar_Historia == "Si" or Iniciar_Historia == "sI" or Iniciar_Historia == "Yes" or Iniciar_Historia == "YES":
    print(Texto1)
    El_programa_ha_iniciado = True
else:
    print("Bueno :(")

#primera encuesta   INPUT1
if El_programa_ha_iniciado == True:

    input1 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. ir a la universidad primero.
b. buscar trabajo.
    """))

    if input1 == "a":
        print (Input1_es_A)
        print (Texto2compartido)
        elinput1fue__A = True
        eltextocompartido = True
    if input1 == "b":
        print (Input1_es_B)
        elinput1fue__B = True

#segunda encuesta INPUT 6 Y INPUT2
#input 6 osea A
if eltextocompartido == True:

    input6 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. aceptar.
b. no aceptar.
    """))

    if input6 == "a":
        print (Input6_es_A)
        elinput6fue__A = True
    if input6 == "b":
        print (Input6_es_B)
        elinput6fue__B = True
# en ambos input 6 termina aqui el programa

#input 2 osea B
if elinput1fue__B == True:

    input2 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. continuar buscando.
b. ir a casa por hoy.
    """))

    if input2 == "a":
        print (Input2_es_A)
        elinput2fue__A = True
    if input2 == "b":
        print (Input2_es_B)
        elinput2fue__B = True

#Input 4
if elinput2fue__A == True:

    input4 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. ir al siguiente día.
b. no ir.
    """))

    if input4 == "a":
        print (Input4_es_A)
        elinput4fue__A = True
    if input4 == "b":
        print (Input4_es_B)
        print (Elotrotextocompartido)
        print (Texto2compartido)
        elinput4fue__B = True
        eltextocompartido = True
    #continua del input 4 es b y es lo mismo que la linea 131, pero es necesario ponerlo otra vez
    if eltextocompartido == True:

        input6 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. aceptar.
b. no aceptar.
    """))

        if input6 == "a":
            print (Input6_es_A)
            elinput6fue__A = True
        if input6 == "b":
            print (Input6_es_B)
            elinput6fue__B = True

#aqui se retoma la linea original del input 4
if elinput4fue__A == True:

    input5 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. aceptar el trabajo.
b. no aceptar el trabajo.
    """))

    if input5 == "a":
        print (Input5_es_A)
        elinput5fue__A = True
    if input5 == "b":
        print (Elotrotextocompartido)
        print (Texto2compartido)
        elinput5fue__B = True
        eltextocompartido = True
    #continua del input 5 es b y es lo mismo que la linea 131, pero es necesario ponerlo otra vez
    if eltextocompartido == True:

        input6 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. aceptar.
b. no aceptar.
    """))

        if input6 == "a":
            print (Input6_es_A)
            elinput6fue__A = True
        if input6 == "b":
            print (Input6_es_B)
            elinput6fue__B = True

#se retoma linea original en input 2  revisar en linea 148 para entender
if elinput2fue__B == True:

    input3 = str(input ("""
Responde con una letra minuscula.
¿Que hará Diego?
a. hablarle.
b. ignorarla.
    """))

    if input3 == "a":
        print (Input3_es_A)
        elinput3fue__A = True
    if input3 == "b":
        print (Input3_es_B)
        elinput3fue__B = True

#texto de fin para todos los finales
if elinput6fue__A == True or elinput6fue__B == True or elinput5fue__A == True or elinput3fue__A == True or elinput3fue__B == True:
    print (" ")
    print ("FIN")