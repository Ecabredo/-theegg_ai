Cifrado simétrico y asimétrico

	• Simétrico: solamente utiliza una clave, tanto para cifrar como para descifrar el mensaje. Si queremos enviarle un correo a otro usuario, ciframos ese mensaje con una llave. Esa clave la tiene que poner el destinatario para poder descifrarlo. Podemos decir, por tanto, que en el cifrado simétrico tanto el emisor como el receptor utilizan una misma clave para ese mensaje. Lógicamente ambas partes tienen que conocer esa clave, tienen que comunicarse previamente para saber cuál van a introducir.
	
	• Asimétrico: la principal diferencia es que utiliza dos claves en este caso. Una de ellas es privada y otra es pública; de manera que a una clave pública le corresponde una clave privada. Cada usuario tiene dos clave: una pública y una privada. La clave pública sirve para cifrar ese correo y la privada para descifrarlo. Si queremos mandar un correo a otro usuario de manera cifrada, necesitamos saber la clave pública del destinatario y así cifrar el correo. El destinatario lo que hace es usar su clave privada para descifrar ese mensaje.
	El remitente le dice al destinatario: "eh, dame tu clave pública (de la cual solo tú tienes la clave privada) para mandarte el mensaje".
	Verificar la autenticidad del remitente y el destinatario:
	El remitente cifra un mensaje con la clave pública del destinatario y lo firma con su clave privada.
			i. El mensaje está protegido.
			ii. Solo el destinatario, con su clave privada, puede acceder al contenido del mensaje.  Por lo tanto, se verifica la autenticidad del destinatario.
			iii. El destinatario, con la clave pública del remitente, puede verificar la autenticidad del remitente.
	
	El sistema de cifrado más famoso es el desarrollado el 1977  por Rivest, Shamir, Adleman, (RSA):
		○ Se generan, para cada usuario, un par de claves en base a dos números primos de longitud similar entre sí.
	
	Para mejorar los sistemas de RSA, existen también las entidades certificadoras o terceros de confianza. Actúan como repositorios de claves públicas. No obstante, se utilizan principalmente para dar veracidad a las firmas. 
	
	PGP:
		○ Pretty Good Privacy
		○ Principalmente utilizado en el correo electrónico. 
		
Cifrar con el solitario

	1. Divide el mensaje original en grupos de cinco letras (No hay nada mágico respecto a los grupos de cinco letras, es sólo tradición). Usa "X" para completar el último grupo. Así, si el mensaje es "DO NOT USE PC", el texto se transformará en:
     DONOT USEPC
	2. Usa Solitario para generar una ristra de letras (los detalles se dan más tarde). Supongamos que son:
     KDWUP ONOWT
	3. Convertimos el mensaje original de letras a números, A=1, B=2, etc:
     4 15 14 15 20   21 19 5 16 3
	4. Convertimos la ristra de Solitario de forma similar:
     11 4 23 21 16   15 14 15 23 20
	5. Sumamos los números de mensaje original con los correspondientes de la ristra Solitario, módulo 26. Es decir, si suman más de 26, restamos 26 de resultado. Por ejemplo, 1+1=2, 26+1=27, y 27-26=1, así que 26+1=1.
     15 19 11 10 10   10 7 20 13 23 
	6. Convertimos los números de nuevo a letras:
     OSKJJ JGTMW

Descifrar con Solitario

La idea básica consiste en generar la misma ristra, y restarla del texto cifrado.
	1. Toma el mensaje cifrado y divídelo en grupos de cinco letras (ya debería estar en ese formato).
     OSKJJ JGTMW
	2. Usa Solitario para generar la ristra. Si el receptor usa la misma clave que el transmisor, la ristra será la misma.
     KDWUP ONOWT
	3. Convierte el mensaje cifrado a números:
     15 19 11 10 10   10 7 20 13 23
	4. Convierte la ristra de forma similar:
     11 4 23 21 16   15 14 15 23 20
	5. Resta a cada número del texto cifrado el número correspondiente de la ristra, módulo 26: for ejempo, 22-1=21, 1-22=5. Es fácil. Si el primer número es menor o igual que el segundo, sumamos 26 al primer número antes de restar. Así, 1-22 se convierte en 27-22=5.
     4 15 14 15 20   21 19 5 16 3
	6. Convierte los números a letras:
     DONOT USEPC
Como puedes ver, descifrar es igual que cifrar, salvo que al mensaje cifrado se le resta la ristra obtenida con Solitario.

Generar las letras de la secuencia de clave


Trébol          à Se toma su valor tal cual.
Diamantes  à Su valor + 13.
Corazones  à Su valor + 26.
Picas            à Su valor + 39.
Jokers          à 53.

Orden secuencial de las cartas de póker: A,2,3,4,5,6,7,8,9,10,J,Q,K
Que equivalen a 1,2,3,4,5,6,7,8,9,10,11,12,13

Si la carta es un trébol, toma su número tal cual. Si es de diamantes, suma 13 a su valor. Si es de corazones, súmale 26. Si es de picas, súmale 39.

Esto es el corazón de Solitario. Las descripciones del cifrado y descifrado dadas más arriba funcionan para cualquier cifrado tipo "ristra" (stream) en modo "output-feedback". Es la manera en que funciona RC4. También es la manera en que funciona DES en modo OFB. Esta sección es específica a Solitario, y explica cómo Solitario genera la ristra.
Solitario genera la ristra utilizando una baraja de cartas. 
Puedes pensar en una baraja de 54 cartas (no olvides los dos comodines) como una permutación de 54 elementos [El texto original en inglés se refiere, evidentemente, a una baraja de póker. N. del T.]. Hay 54!, sobre 2.31*10^71 posibles ordenamientos de la baraja. Mejor aún, hay 52 cartas en una baraja (sin los comodines), y 26 letras en el alfabeto. Este tipo de coincidencia es demasiado buena para dejarla pasar.
Para utilizar Solitario, se necesita una baraja con las 52 cartas y los dos comodines. Los comodines deben ser diferentes. (Esto es habitual. La baraja que estoy usando mientras escribo tiene estrellas en sus comodines: uno tiene una estrella pequeña, y el otro tiene una estrella grande). Llámalo a uno comodín A y al otro comodín B. Generalmente hay algún elemento gráfico en los comodines que es igual, pero de diferente tamaño. Llama "B" al comodín que lo tiene más "grande". Es más fácil si puedes escribir una gran "A" y una gran "B" en los comodines, pero recuerda que tendrás que explicárselo a la policía secreta si alguna vez te cogen.
Para inicializar la baraja, cógela con la mano, cara arriba. Luego ponlas en su configuración inicial, que será su clave (hablaré de la clave más tarde, porque es un tema diferente a generar la ristra en sí). Ahora estás preparado para producir una ristra.
He aquí cómo generar un carácter. Esto es Solitario:

	1. Encuentra el comodín A. Intercámbialo con la carta que tiene debajo. Si el comodín está al final de la baraja, ponlo debajo de la primera carta.
	2. Encuentra el comodín B. Muévelo bajo la carta que está debajo de la que tiene debajo. Si el comodín está al final de la baraja, muévelo debajo de la segunda carta. Si el comodín es la penúltima carta, muévelo debajo de la primera carta. Básicamente asume que la baraja es un bucle, ¿te haces la idea?.
Es importante realizar los dos pasos anteriores en orden. Es tentador volverse perezoso y simplemente mover los dos comodines cuando los encuentras. Eso también funciona, a menos que estén muy cerca el uno del otro.
Así que si la baraja está en esta situación antes del paso 1:
     A 7 2 B 9 4 1

al final del paso 2 debería ser
     7 A 2 9 4 B 1

Y si la bajara fuese:
     3 A B 8 9 6

Al final del paso 2 debería ser:
     A 3 8 9 B 6

Si tienes alguna duda, recuerda mover el comodín A antes que el B. Y ten cuidado cuando los comodines se encuentren al final de la baraja. Si un comodín es la última carta, imagínatela como si fuera la primera carta, antes de empezar a contar.
	3. Corta la baraja en tres, intercambiando las cartas antes del primer comodín con las cartas que están detrás del segundo comodín. Si la baraja fuera:
     2 4 6 B 5 8 7 1 A 3 9

entonces tras el corte la baraja sería:
     3 9 B 5 8 7 1 A 2 4 6

"Primer" y "segundo" comodín se refiere al comodín que está más arriba o más abajo respecto al extremo de la baraja. Ignora el hecho de que un comodín es "A" y otro es "B", en este paso.
Recuerda que los comodines y las cartas entre ellos no se mueven. Esto es fácil de hacer con las manos. Si no hay cartas en una de las secciones (porque los comodines están juntos, o porque uno está arriba y otro debajo de la baraja), simplemente considera esa sección como vacía y muévela de todos modos. Si la baraja es:
     B 5 8 7 1 A 3 9

Tras el corte el intercambio, será:
     3 9 B 5 8 7 1 A

Una baraja
     B 5 8 7 1 A

no sufrirá ningún cambio tras este paso.
	4. Mira la última carta. Conviértela a un número de 1 a 53 (usa el orden normal: tréboles, diamantes, corazones y picas. Si la carta es un trébol, toma su número tal cual. Si es de diamantes, suma 13 a su valor. Si es de corazones, súmale 26. Si es de picas, súmale 39. Ambos comodines suman 53). Cuenta el valor valor obtenido empezando en la carta superior (normamente yo cuento de 1 a 13 una y otra vez, si es preciso; es más fácil que contar hasta un número alto de forma secuencial). Corta tras esa carta, dejando la última carta de la baraja a final. Si la baraja es:
     7 ... cartas ... 4 5 ... cartas ... 8 9

y la novena carta es el 4, el corte sería:
     5 ... cartas ... 8 7 ... cartas ... 4 9

La razón de dejar la última carta en su lugar es para hacer el último paso reversible. Esto es importante a la hora de analizar su seguridad de forma matemática.
Una baraja con un comodín como última carta queda igual tras este paso. No hay cambios.
Asegúrate de no invertir el orden cuando cuentes las cartas. La forma correcta de contar es pasar las cartas de una mano a la otra. No hagas montones sobre la mesa.
	5. Mira la primera carta. Conviértela en un número de 1 a 53, de la misma manera que en el paso 4. Cuenta esas cartas (la primera carta es la uno). Escribe la carta tras la que hayas terminado en un papel; no la quites de la baraja. Si la carta es un comodín, no la apuntes, y vuelve al paso 1. Este paso no modifica el estado de la baraja.
	6. Convierte la carta del paso anterior en un número. Del As de tréboles al Rey de tréboles se cuentan del 1 a 13. Del As de diamantes al Rey de diamantes se cuentan como 14-26. Del As de corazones al Rey de corazones se cuentan como 1 a 13. Por último, del As de picas al Rey de picas se cuentan como 14 a 26. Necesitamos ir de 1 a 26, no de 1 a 52, para poder convertir a letras.

Así es como Solitario cifra un carácter. Se usan estos pasos para generar una ristra tan larga como sea necesario; simplemente se repiten los pasos tantas veces como sea preciso, sin barajar el mazo. Y, recuerda, necesitarás una ristra tan larga como el mensaje original.
Sé que cada país tiene barajas diferentes. En general, no importa cómo se ordenen las cartas o cómo se conviertan las cartas a números. Lo que importa es que el remitente y el receptor se pongan de acuerdo en las reglas. Si no eres consistente, no te podrás comunicar.


Links de interés:

https://www.youtube.com/watch?v=uxzLm79aSzw&feature=youtu.be
https://sindominio.net/biblioweb/telematica/solitario.html
https://developer.rhino3d.com/guides/rhinopython/python-dictionaries/
