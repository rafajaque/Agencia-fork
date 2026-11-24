# Panel de seguimiento escolar: ideas por evaluar

Estado: **borrador de ideas para segunda opinión**. No es una decisión ni modifica ADR. Fecha: 2026-11-11.

## Contexto

La agencia es una plataforma **gratuita** para estudiantes de 3.º y 4.º medio de **liceos con alta vulnerabilidad escolar en Chile** (humanístico-científicos y técnico-profesionales). El estudiante compara carreras con datos oficiales, simula su puntaje ponderado, arma una hoja de decisión y sigue los plazos del FUAS (el formulario de beneficios estatales). El portal básico no pide cuenta y no guarda datos personales.

Se estudia ahora un **panel de seguimiento escolar para los colegios**, centrado en **cumplir las metas vocacionales** de los estudiantes y construir una buena base para ellas. Ejemplo: si un curso apunta a estudiar enfermería, el refuerzo debería ir a biología y química (y a las pruebas que esa carrera pondera) antes que a otras áreas, sin negar que los demás ramos siguen siendo esenciales.

El colegio podría intervenir **de forma temprana y presencial** con sus estudiantes (orientador, psicopedagoga, docentes).

## Restricciones no negociables

- **Ley 21.719 de protección de datos personales de Chile** (vigencia prevista el 2026-12-01). Los artículos de la matriz interna salen de una fuente no oficial: hay que verificarlos antes de citarlos como hechos.
- La ficha pertenece al estudiante. Menores de 18: autorización del tutor.
- La IA no diagnostica ni es terapeuta. No se promete predicción. Lenguaje sin estigma.
- Un equipo pequeño (tres personas). El piloto es en 2027 con uno o dos liceos; no habrá grupo de comparación.
- Datos oficiales con fuente, URL y fecha. Nada se inventa.

## Lo que ya existe o está decidido

- Calendario oficial del FUAS con el estado de cada hito; hoja de decisión (anotaciones solo en el navegador); comparador de carreras; simulador de puntaje ponderado en revisión (ponderaciones oficiales de DEMRE por carrera).
- Un protocolo de crisis (riesgo de suicidio o autolesión → líneas de ayuda y alerta con revisión humana).
- En la versión actual del diseño, el panel muestra solo agregados con grupos pequeños ocultos, solicitudes de ayuda y acuerdos que el propio estudiante decide compartir.

## Las ideas por evaluar

Cada una se describe tal como la plantea el líder y con el ajuste que propuso el asistente.

1. **ID del estudiante.** Cada estudiante recibe un ID numérico aleatorio al crear su cuenta. La plataforma no recibe nombres; el colegio guarda la tabla ID ↔ nombre. Sigue siendo dato personal (seudonimización).
2. **Autorizaciones de apoderados tramitadas por el colegio.** El colegio reparte y recoge el formulario; la plataforma conserva la prueba del consentimiento, que debe ser específico por finalidad y revocable.
3. **Datos socioeconómicos.** Se muestra al estudiante en qué tramo socioeconómico está, con consentimiento explícito y separado. El colegio ya conoce parte de esa información.
4. **Puntajes individuales visibles para el docente.** Con autorización específica del estudiante o su tutor. Hoy el simulador no guarda nada: sería un cambio de arquitectura.
5. **Meta de carrera y avance.** Al crear su perfil, el estudiante elige una carrera meta y ve qué le falta: puntaje necesario, plazos y pasos. Por defecto queda solo con él.
6. **Foco curricular del curso según las metas.** El panel agrega las carreras que el curso eligió y muestra qué pruebas (por ejemplo ciencias, matemática, lenguaje) pondera cada una según DEMRE, para orientar el refuerzo del colegio.
7. **Alertas configurables por el docente.** Por ejemplo «sin respuesta en 5 días». El estudiante sabe que existen, y dicen «sin actividad», no «riesgo». La idea original era que el estudiante no supiera del seguimiento; se descartó por transparencia y confianza. El docente puede acercarse sin decir «vi que no usas la app».
8. **Psicopedagoga.** Recibe derivaciones cuando el estudiante pide hablar con alguien y cuando se activa el protocolo de crisis. La idea original era que viera a quién tiene «riesgo de TDAH o TDA» según su comportamiento en la app; se descartó por ser dato de salud inferido, sin respaldo de que el uso de una app sirva para eso, y por el riesgo de falsos positivos.
9. **Comparación de NEM con carreras.** Un simulador de escenarios («con NEM X y PAES Y tendrías Z; el año pasado el corte fue W») con datos públicos, sin perfilar. La idea original incluía decir «si subes el NEM puedes relajarte en la PAES»; se acordó que **no** sea un consejo de la app.
10. **Rankings.** Ninguno entre colegios. Dentro del colegio se discute entre un ranking de estudiantes y mostrar solo rangos o distribuciones del curso.
11. **Grupos pequeños.** La ley no fija un número. Se propone un mínimo (por ejemplo 10) antes de mostrar una cifra.
12. **Intervención presencial temprana.** El panel permite al colegio detectar pendientes y actuar en persona. El líder cree que ya está demostrado que intervenir físicamente sube los puntajes y el conocimiento.
13. **Etiquetas de vulnerabilidad o riesgo por estudiante.** Se recomendó no hacerlas (perfilado, estigma, falsos positivos), y usar reglas transparentes en su lugar.

## Lo que se quiere de la segunda opinión

Responde en español, en **menos de 900 palabras**, con esta estructura:

**A. Para cada una de las 13 ideas (en una o dos líneas por punto):** puntos favorables, puntos negativos o riesgos (legales, éticos, de efectividad), y una mejora concreta.

**B. Evidencia.** Busca en la web evidencia que respalde o contradiga las ideas 5, 6, 7, 10 y 12 en particular. Para cada fuente da: autores o institución, año, tipo de estudio (experimento aleatorio, metaanálisis, observacional), país, qué mide y su límite. Marca **[verificado]** solo lo que leíste en la fuente; marca **[no verificado]** lo demás. No inventes citas ni cifras.

Preguntas de evidencia concretas:
1. ¿Hay evidencia de que la intervención **presencial** (tutoría, mentoría, asesoría) mejora el **aprendizaje o los puntajes**, y no solo la postulación o la matrícula? Distingue ambos resultados.
2. ¿Qué evidencia hay sobre **sistemas de alerta temprana** escolares: efectividad, exactitud y falsos positivos, y daños de etiquetar?
3. ¿Qué efectos tienen los **rankings dentro del mismo curso o colegio** sobre la motivación y el autoconcepto de los estudiantes?
4. ¿Reforzar las áreas que ponderan las carreras elegidas mejora la admisión? ¿Y cuáles son los riesgos de un refuerzo demasiado enfocado?
5. ¿Qué se sabe sobre cuándo y por qué los estudiantes **no piden ayuda**, y qué diseños aumentan que la pidan sin vigilarlos a escondidas?

**C. Cierre.** Tres cosas que recortarías del piloto 2027 por riesgo o costo, tres preguntas concretas para el abogado, y lo más importante que falta definir.

Cita siempre las fuentes con enlace. Si algo no tiene evidencia, dilo.
