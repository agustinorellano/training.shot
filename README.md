# Training Shot · Rutina L5

App web de rutinas de gimnasio pensada para entrenar con cuidado de la zona lumbar (L5) y la ATM.

- Genera la rutina del día (3 días base + 4º día opcional de refuerzo).
- Fichas por ejercicio: imagen, músculos, pasos, errores comunes, ritmo y notas para la espalda.
- Registro por serie, temporizador de descanso, sugerencia de progresión y gráfico de progreso.
- Tema claro/oscuro. Los datos se guardan en el navegador (`localStorage`); hay copia de seguridad por código.

## Deploy
Es un sitio estático: `index.html` en la raíz. En Vercel, importá el repo sin framework ni build command.

## Editar
`index.html` se genera desde `src/template.html` (ahí están los ejercicios, planes y estilos).
Ver `src/build.py` para regenerarlo.

## Créditos
Imágenes de los ejercicios: [free-exercise-db](https://github.com/yuhonas/free-exercise-db) (dominio público).

> Esta app es una guía para ordenar el entrenamiento y no reemplaza a un médico ni a un kinesiólogo.
