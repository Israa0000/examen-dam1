# Teoria

Realiza el examen directamente sobre el archivo!

Este examen solo muestra algunos conceptos al azar que me parecen importantes, hay muchos!

Intenta añadir código cuando lo necesites utilizando

```lenguaje
codigo
```

1. ¿Que diferencia una variable creada con `let` de una creada con `const`?
Let se utiliza para una variable que va a cambiar, const con una variable que no cambia
2. ¿Qué es un dato primitivo? ¿y un objeto?

2. ¿Qué diferencia hay entre `==` y `===`?

3. Analiza el siguiente código, ¿qué valor se mostrará en la consola?
```js
let a = 1;

function mi_funcion() {
    let a = 2;
}

mi_funcion();
console.log(a);
```
Se mostrara en consola: 2

4. ¿Qué es el DOM? Explícalo brevemente.
Es la manera en la que se representa un documento HTML

5. ¿Este código es correcto? Si no lo es, ¿por qué?
```js
const boton = document.querySelector('button');
function saluda() {
    console.log('Hola');
}
boton.addEventListener('click', saluda());
```
No es correcto, para que el evento 'click' ejecute la funcion saluda cuando se haga click en el boton se debe de pasar la referencia a la funcion
CORRECCION
```js
const boton = document.querySelector('button');
function saluda() {
    console.log('Hola');
}
boton.addEventListener('click', saluda);
```

6. ¿Que formas de seleccionar elementos del DOM conoces? ¿Cuál es la diferencia entre ellas?
document.getElementById()

7. ¿Qué es un evento? ¿Qué formas conoces de crearlos?
Es una accion que ocurre despues de interactuar con una pagina web
<button click="alert('Hola')">Haz clic aquí</button>

8. ¿Como se añade una libreria externa a un proyecto de JavaScript? Puedes usar p5 como referencia.
<body>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>

    <script>
        function setup() {
            createCanvas(400, 400);
            background(220);
        }

        function draw() {
            ellipse(200, 200, 50, 50); 
        }
    </script>

</body>

9. ¿Que es esto? `<meta charset="UTF-8">` ¿Por qué es importante?
es una codificación de caracteres utilizada para representar texto en todos los idiomas del mundo.

10. ¿Que es una función? Explica brevemente su sintaxis en el lenguaje que prefieras.
Es un codigo que se puede ejecutar cuando se llama

´´´
function saludar(nombre) {
    return "¡Hola, " + nombre + "!";
}

console.log(saludar("Carlos")); 
```

La función saludar toma un parámetro nombre y devuelve un mensaje saludando a la persona cuyo nombre se pasa como argumento.

Cuando llamamos a la función saludar("Carlos"), el valor "Carlos" es pasado como el parámetro nombre, y la función devuelve el mensaje "¡Hola, Carlos!".