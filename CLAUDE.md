# Training Shot · Rutina L5

App web de rutinas de gimnasio para un usuario con discopatía lumbar L5 y ATM. Idioma: español rioplatense (vos). Estética: minimalista tipo Apple, bordes redondeados, tema claro/oscuro con botón.

## Estructura
- `src/template.html`: **fuente editable** (HTML + CSS + JS en un solo archivo). Ejercicios (`EX`), fichas (`INFO`), músculos (`ZONES`), planes (`PLAN3`, `DAYD`).
- `src/build.py`: genera `index.html` incrustando las imágenes (base64) de free-exercise-db. Ver el docstring.
- `index.html`: **generado**, no editar a mano. Es lo que se publica (sitio estático, sin build en Vercel).

## Reglas de dominio (no romper)
- Nada de peso muerto, sentadilla cargada, remo inclinado, abdominales de flexión repetida ni press parado pesado.
- Press y hombros con respaldo a 90° o banco ≤ 30°. Core en todas las rutinas.
- Dolor lumbar diario: 0–3 normal, 4–6 descarga (menos series, −15% de peso, sin prensa), ≥7 solo core suave y recomendar descanso.
- La app es una guía y no reemplaza a un médico/kinesiólogo; las notas de espalda de cada ejercicio están pendientes de revisión profesional.

## Datos (localStorage, clave `rutina-l5-v1`)
`{p:{days,extra,focus,pain,v,d,theme,sel}, logs:{[id]:[{d,w,reps,sets:[{w,r}],fit}]}}`
- `fit`: `easy` | `ok` | `hard`. `reps` = mínimo de reps entre las series hechas. Progresión doble: al llegar al tope del rango y cómodo, sube `step`.
- Hay copia de seguridad por código (copiar/pegar) en la pestaña Progreso.

## Pendientes (por orden)
1. Imágenes en mayor resolución (hoy 300 px, 2 cuadros).
2. Videos concretos por ejercicio (hoy son búsquedas de YouTube).
3. Base de datos para sincronizar entre dispositivos (Supabase) y login simple.
4. PWA instalable.
5. Historial de dolor con gráfico y descarga automática cada 4–6 semanas.
6. Registro de peso corporal y medidas.

## Créditos
Imágenes: free-exercise-db (dominio público).
