# Curso de Haskell - Traducción de la comunidad

[🇺🇸 version (original)](https://github.com/input-output-hk/haskell-course)

>Esta es una traducción hecha del curso de Haskell de IOG, supervisada por Robertino 😇, con el objetivo de ofrecer a la comunidad hispana de Haskell/Cardano una herramienta de aprendizaje en su idioma. Cualquier miembro de la comunidad puede realizar su aporte/sugerencia.
>>Todos los comentarios de la traducción estarán en bloques como estos.

**Este curso está diseñado para que sus estudiantes puedan aprender Haskell desde cero, hasta tener el conocimiento necesario para trabajar con Marlowe y Plutus.** El curso en sí no contiene explicaciones sobre Marlowe o Plutus. Por lo tanto, si deseas aprender Haskell para otros usos, ¡podés hacerlo! 😃

Para más información, continúa leyendo o mira este video introductorio:
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)


## ¿Cuánto debo estudiar si solo deseo usar Marlowe/Plutus?
En el [índice](#lo-que-cubriremos), hay puntos de control bien marcados (para ambos Marlowe y Haskell) donde consideramos que ya sabes suficiente Haskell como para usar esa tecnología.

## Cómo leer/mirar las lecciones

Para recorrer las lecciones interactivas, dirigite a la lección que desees dentro de "[Lo que cubriremos](#lo-que-cubriremos)" y clickeá sobre el botón que se ve como el de debajo de este párrafo. Si la página carga con "500: Internal Server Error" simplemente volvé a cargarla y debería andar bien. En la parte superior, vas a observar una consola que muestra el progreso en preparar tu lección interactiva. Durante este tiempo, podés explorar la lección que se estará mostrando de forma no interactiva.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vamanfredi/haskell-course/HEAD?labpath=%2Flessons%2F01-Introducci%C3%B3n-a-haskell.ipynb)

Para ver el video, clickea el botón que se ve como éste:

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)

## Para realizar la ejercitación

2. Cloná este repositorio.
3. Crea una cuenta de [GitPod](https://www.gitpod.io/).
4. Hacé click en este botón para crear un entorno de desarrollo remoto: [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white)](https://gitpod.io/#https://github.com/input-output-hk/haskell-course)
5. Selecciona la carpeta `Tarea/TareaXX` con la tarea que desees completar.
6. Seguí las instrucciones del archivo app/Main.hs.
8. ¡Revisá las soluciones dentro de la rama "solutions-es"!

#### Estructura del Repositorio

    Haskell-Course/ES-translation
        |   |
        |   |---- Tarea
        |          |
        |          |---- Tarea01 (Tarea para clase 01)
        |          |---- Tarea02 (Tarea para clase 02)
        |          ...
        |
        |-------- lecciones (Lecciones en formato Jupyter Notebook. Se accede a través de Binder.)
                   |
                   |---- 1-Introducción-a-haskell
                   |---- 2-Funciones-Tipos-de-Datos-y-Signatures

Todo el resto puede ser ignorado

## Interactuar con otros estudiantes
 (ambos en inglés)
- [Canvas](https://iohk.instructure.com/enroll/3BAAGG)
- [IOG's technical community (revisá el canal #ask-haskell!)](https://discord.gg/inputoutput)

## Preguntas Frecuentes

[Preguntas Frecuentes](PreguntasFrecuentes.md)

## Lo que cubriremos

**Esta es una guía provisional. Los cambios pueden (y van a ser) hechos a medida que avancemos con el curso y obtengamos feedback de los estudiantes**

**Si no hay botones en una lección, todavía no está publicada.**

### 1. Intro y herramientas [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vamanfredi/haskell-course-ES/HEAD?labpath=ES-translation%2FLecciones%2F01-Introducci%C3%B3n-a-haskell.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/pkU8eiNZipQ)

- Introducción al curso y las clases
  - Qué cubriremos
  - Estructura del repositorio
- Introducción a Haskell
  - Cómo abrir y usar JupyterLab
  - Programación funcional pura
  - Sintaxis básica
  - Sistema de Tipos en Haskell
  - Laziness
  >no hay una traducción para esto, viene de "lazy evaluation", refiere a una forma particular de evaluar expresiones que se explica más adelante
  - GHC y GHCi
- GitPod
  - Cómo abrir y usar GitPod
  - Ejemplo de cómo completar un ejercicio de tarea.


### 2. Tipos de datos, Firmas y Polimorfismo[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F02-Functions-Data-Types-and-Signatures.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/RABzYje2d2A)


- Introducción a los tipos
- Firmas de tipos
  - Firmas de funciones
  - Variables en Haskell
    - Parámetros en funciones
    - Nombres/Definiciones
- Funciones Infijas y Prefijas (Infix y Prefix)
- Tipos de datos en profundidad
  - Int, Integer
  - Float, Double
  - Rational
  - Bool
  - Char
  - Listas
  - Strings
  - Tuplas (Tuples) + Tuplas VS Listas
- Valores polimórficos y variables de tipo

### 3. Condicionales y construcciones auxiliares

- If-then-else
- Guardas (Guards)
- `let`
- `where`
- ¿Debería usar `let` o `where`?
- Tips a tener en cuenta

### 4. Pattern matching y Case

- Qué es pattern matching
- Pattern matching en
  - Implementación de funciones
  - Listas
  - Tuplas
- Case

### 5. Mejorando y combinando funciones

- Funciones de orden superior
  - La función `filter`
  - La función `any`
- Funciones Lambda
- Precedencia y asociatividad 
- Funciones currificadas (curried)
  - Aplicación parcial
- Composición y aplicación de funciones
-  Operador `.`
-  Operador `$`
### 6. Recursion

- Concepto
- Ejemplos

### 7. Manipulando listas

- `zip`
- `map`
- `foldl`, `foldr`
- `scan`

### 8. Introducción a los Type Classes

- ¿Qué son los type classes?
- Type classes más comunes
  - `Eq`
  - `Ord`
  - `Integral`
  - `Floating`
  - `Num`
  - Mencionando `Read`, `Show`, `Enum`, `Bounded`, and `Foldable`.
- Restricciones de classes con ejemplo

### 9. Creando tipos

- Sinónimos de tipos
  - Cómo definir sinónimos de tipos
  - Por qué usar sinónimos de tipos
- Definir nuevos tipos
  - `data`
  - Parámetros por valor
  - Pattern matching en tipos
  - Record syntax
- Parametrizar tipos
  - Parametrizar sinónimos de tipos
  - Parametrizar nuevos tipos
- Honorable mención de `newType`

### 10. Creando Type Classes e Instanciación

- Repaso de Type Classes
- El type class `Eq` 
  - Definiendo la type class `Eq` 
  - Definiendo una instancia para la type class `Eq`
  - Mejorando la type class `Eq` (minimal complete definition)
  - Defining an instance for a parameterize type.
- El type class `Ord`
  - Explorando el type class `Ord` (Subclases)
- Deriving
- Ejemplo completo

### 11. IO Básico (Entrada y salida)

- Necesitamos efecto
- Qué es IO
- main + putStrLn + componiendo otras funciones
- `>>`
- `>>=`
- do notation
  - `do`
  - `<-`
  - `let`
- Algunos ejemplos
- Leer/Escribir en consola
- Leer/Escribir un archivo

### 12. Bits y Bytes

- Agrupando bits y bites
- Haskell y los bytes
- Byte strings estrictos y lazy
- Ejemplo

### 13. Pragmas, Módulos y Cabal

- Prelude
- pragmas/extensiones
- Visión general de módulos base
- Importando módulos base
- Algunos módulos
  - Data.Char
  - Data.Tuple
  - Data.Array
- Creando tus propios módulos
- Cabal
  - Qué es y por qué usarlo
  - Archivo cabal
  - Usando bibliotecas externas con Cabal

### 14. Aprendiendo por tu cuenta y Map

- Usar GHCi para descubrir más
- Hoogle
- HaskellWiki
- Enseñando el módulo Map

### 15. Either y Maybe (sólo uso práctico)

- Maybe
  - Por qué y cuando usar Maybe
  - Syntaxis
  - Ejemplos
- Either
  - Por qué y cuando usar Either
  - Syntax
  - Ejemplos
- Proyectos usando Maybe e IO

### 16. Aeson

- Aeson

---

#### YA ESTÁS PREPARADO PARA MARLOWE! 🥳🎉 (Seguí avanzando para Plutus.)

---
>Más adelante el resto de la traducción😪 
### 17. Monoid

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 18. Functor

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 19. Applicative

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 20. Monad

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)
- `do` notation in general

### 21. Reader Monad

- Incentive/Motivation
- Binding strategy (see [here](https://wiki.haskell.org/All_About_Monads#The_Reader_monad))
- Definition
- Examples

### 22. Writer Monad

- Incentive/Motivation
- Binding strategy
- Definition
- Examples

### 23. State Monad

- Incentive/Motivation
- Binding strategy
- Definition
- Examples

### 24. Monadic functions / Operating with Monads

- liftM
- sequence and sequence_
- mapM and mapM_
- filterM
- foldM

### 25. Transformers

- TODO
