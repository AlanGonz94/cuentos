Generador de una Historia Interactiva 📗
*Por: Alan González*

**DOCUMENTACIÓN**

Este programa esta hecho para funcionar con el lenguaje python, te presenta una historia en la que tendras que elegir las decisiones del protagonista.
Cada vez que tomes una decision, la historia se desarrollara de manera diferente. Tiene 5 Finales distintos.

Existen variables que son segmentos de texto de las historias identificados por un nombre relacionado al momento en el que deberan aparecer, si es que las condiciones se cumplen.

Debes seguir las instrucciones de las encuentas que te indican como debes responder, segun como quieres que sea el curso de la historia.

El codigo se basa principalmente en la funcion if, en que segun las decisiones que tu tomes hara que se cumpla la condicion que de paso a que te salga cierto segmento de historia y al mismo tiempo internamente se va llevando un registo de que decisiones fueron tomadas por el usuario en un sistema booleano true/false.

Como sea que vayas decidiendo las variables de respuestas pasaran de un estado inicial falso al estar inactivas, a true cuando tu las activas y eso dara pie a que texto te saldra y a la nueva pregunta con 2 opciones para decidir el futuro de nuestro protagonista.
Si quieres puedes dejar de leer aqui y empezar a analizar el codigo.
-
-
-
-
Ejemplo para comprender mejor la descripcion:
#if elinput1fue__B == True:     
*si en la encuesta 1 elegiste la opcion b te colocara la encuesta luego del texto de la historia*
#    input2 = str(input ("""    
*Responde con una letra minuscula.*
#¿Que hará Diego?
#a. continuar buscando.
#b. ir a casa por hoy.
#    """))
*si elegiste la opcion a o b dependera que texto te mostrara y marca que elegiste la opcion a o b al volver la variable verdadera para que sirva despues como una confirmacion para seguir con la siguiente parte*
#    if input2 == "a":
#        print (Input2_es_A)
#        elinput2fue__A = True
#
el print de input2 es A o B es el texto de la historia
#    if input2 == "b":
#       print (Input2_es_B)
#       elinput2fue__B = True
