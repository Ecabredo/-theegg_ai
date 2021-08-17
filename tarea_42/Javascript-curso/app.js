document.write("<h1>Hello World </h1>");      //Mostrar mensaje por pantalla
console.log("This is string");                //Mostrar mensaje en consola.


/*Tipos de datos

//String: entre comillas doble o simples. 
"Hello World" // String
'Hello World' // String

//Número
10000000
-2.3

//Booleano
true
false

/*Array: una lista. Puede contener elementos de distinto tipo. 
['Ernesto', 'Adriana', 'Karmele']   //Lista de strings
[1,2,3]                             //Lista de números
[true, false, false, true]          //Lista de booleanos  */

//Objeto: se crean a partir de llaves y se representan a través del par clave:valor. Las claves van entre comillas.
//En este caso, se introduce se añade console.log para mostrarlo en la consola del navegador. 
console.log({"username": 'Ernesto',
            "score": 23.23, 
            "hours": 14,
            "professional": true,
            "friends": ["Adriana", "Karmele"]});

//Variables
var user_name = "Ernesto"  //La palabra clave var y let se utilan para crear variables. ¿Cuándo utiliza var y cuándo let? 
//En función del alcance de las variables. 
let last_name = "Martinez de Cabredo"
console.log(user_name);
console.log(last_name);

//Se puede cambiar la variable.
user_name = "Pepe";

//Para declarar variable constantes. No es posible reasignar otro valor a este tipo de variables. 
const PI = 3.1416;
console.log(PI);

//Operadores
let numberOne = 60;
let numberTwo = 100;
let result = numberOne+numberTwo
console.log(result);

//Concatenación: únicamente viable con los strings
let name = 'John';
let lastname = 'Carter'
let completeName = name+ ' ' + lastname;
console.log(completeName);

//Comparaciones: devuelve un booleano
let comparison_0 = numberOne>numberTwo;
console.log(comparison_0);
let comparison_1 = numberTwo==numberTwo;
console.log(comparison_1);
let comparison_2 = numberOne!=numberTwo;
console.log(comparison_2);

//Condicionales
if (comparison_0 == true) {
    console.log('Correcto');  
} else {
    console.log('Incorrecto');
}

let score = 70;
if (score>30){
    console.log('You need to practice more');
}
else if (score>15) {
    console.log('Estas mejorando');
}
else {
    console.log('Muy bueno');
}

let typeCard = 'Debit Card';
switch (typeCard) {
    case 'Debit Card':
        console.log('Esta es una tarjeta de débito');
        break;
    case 'Credit Card':
        console.log('Esta tarjeta es de crédito');
        break;
    default:
        console.log('No conozco ese tipo de tarjeta');    
}

//Bucles
//Mostrar 10 veces 'Hola Mundo':
let count = 10;
while(count>0) {
    console.log('Hello World');
    count--; //Operador de decremento. Count++; Operador de incremento.
}

let names = ['Ernesto', 'Adriana', 'Karmele', 'Izaskun'];
console.log(names[0]); //ídice de lalista para ver el valor que interesa. El primer índice de la lista es el cero.
console.log(names.length); //Método para obtener la longitud de la lista. 
for(let i=0;i<names.length;i++) {
    console.log(names[i]);
}
for(let i=names.length-1;i>=0;i--) {
    console.log(names[i]);
}

//Funciones
function greeting (nombre) {
    console.log('Hello');
    console.log(nombre);
}
greeting('Ernesto');

function suma  (n1, n2) {
    console.log(n1+n2);
}
suma(1,2);
suma(12,13);
suma('Ernesto', 'Mtez de Cabredo');

//DOM
//NODEJS
//HTML5API


