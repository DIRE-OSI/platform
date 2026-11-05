# 🦟 DIRE

### Estimador de Incidencia de Enfermedades y Recursos

**Pronósticos del riesgo de incidencia de enfermedades a 1, 2 y 3 meses, a escala subnacional.** *Cobertura inicial: dengue y malaria en Perú y Brasil. Se están incorporando otros países y enfermedades.*

[Licencia](https://camo.githubusercontent.com/35b94db23d3ed026343335f74d52ce31e74b77ad7dab4e4b89f49f2026e0937f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d2d322e302d626c7565) [Documentación](https://camo.githubusercontent.com/2757dc2bf5a62095ab6859a19f221900a824d50d26f887a97bcb6acc2a2b2f5d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d43432d2d42592d2d342e302d6c6967687467726579) [Estado](https://camo.githubusercontent.com/7e58d83a32128f526c6bcf2710141d1c11ae3b3135d672d53cacee6a6a4fab10/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7374617475732d616374697665253230646576656c6f706d656e742d6f72616e6765)

[🌐 Panel interactivo en línea](https://dire.impact.nltglobal.com/) · [🗺️ Cómo usar el panel](https://github.com/DIRE-OSI/platform/blob/main/docs/USING_THE_DASHBOARD.md) · [ℹ️ Acerca del proyecto](https://github.com/DIRE-OSI/platform/blob/main/docs/ABOUT.md) · [🔬 Fundamentos científicos](https://github.com/DIRE-OSI/platform/blob/main/docs/RESEARCH_BASIS.md) · [👥 Equipo](https://github.com/DIRE-OSI/platform/blob/main/docs/TEAM.md) · [📜 Hoja de ruta](https://github.com/DIRE-OSI/platform/blob/main/docs/ROADMAP.md) · [🤝 Cómo participar](https://github.com/DIRE-OSI/platform/blob/main/README.md#-get-involved) · [🆘 Soporte](https://github.com/DIRE-OSI/platform/blob/main/SUPPORT.md)

> 🚧 **Estado: en desarrollo activo.** Este repositorio es una versión inicial y en evolución, publicada **en coordinación con el equipo del proyecto DIRE de la Universidad de California en San Diego (UCSD) y New Light Technologies (NLT)**. Su estructura, documentación y código se están incorporando y revisando por etapas, por lo que el contenido puede cambiar. Se comparte desde ahora para facilitar la revisión abierta y la colaboración. Considérelo un trabajo en curso y coordine con el equipo del proyecto antes de utilizarlo como referencia.

> ⚠️ **Descargo de responsabilidad:** Todos los pronósticos y resultados analíticos se proporcionan «tal cual», únicamente como apoyo para la toma de decisiones. New Light Technologies, la Universidad de California en San Diego y UNICEF rechazan expresamente toda responsabilidad por las decisiones tomadas a partir de estos resultados. Consulte [DISCLAIMER.md](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md) para conocer los términos completos.

---

**Versión preliminar.** Este repositorio se está completando, en coordinación con el equipo del proyecto de **UCSD y NLT**, con documentación de las fuentes de datos y flujos de procesamiento en Python y R para DIRE. Es el repositorio abierto a la comunidad del proyecto, publicado conforme a las condiciones de código abierto de la subvención de Wellcome Trust. La API de pronósticos y el panel interactivo están disponibles en [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com/); su código fuente se publicará en fases posteriores. Consulte [docs/ROADMAP.md](https://github.com/DIRE-OSI/platform/blob/main/docs/ROADMAP.md) para conocer el plan completo de publicación.

---

## ¿Qué es DIRE?

DIRE (Disease Incidence and Resource Estimator, Estimador de Incidencia de Enfermedades y Recursos) es una plataforma de pronóstico basada en aprendizaje automático que genera **estimaciones de incidencia de enfermedades para horizontes de 1, 2 y 3 meses** (el mes en curso y los dos siguientes), a nivel de unidades administrativas subnacionales. Está diseñada para ayudar a responsables de la toma de decisiones en salud pública, epidemiólogos y personal de respuesta humanitaria a anticipar la carga de enfermedad y asignar recursos *antes* de que los brotes alcancen su punto máximo.

**La cobertura se está ampliando.** Perú y Brasil, junto con el dengue y la malaria, son los **primeros países y enfermedades** que se están probando durante las fases de desarrollo, operación y mantenimiento (O&M) de la plataforma. La metodología y los flujos de procesamiento están diseñados para generalizarse, y **con el tiempo se están incorporando otros países y enfermedades**. Las referencias a Perú, Brasil, dengue y malaria en este repositorio describen el *despliegue actual*, no el alcance definitivo de la plataforma.

La plataforma integra:

- **Covariables de teledetección:** NASA Earthdata (cobertura del suelo e índices de vegetación de MODIS; elevación de NASADEM).
- **Covariables climáticas:** Copernicus ERA5-Land (temperatura, precipitación, humedad).
- **Vigilancia epidemiológica:** registros de casos de DATASUS SINAN de Brasil y de dengue del MINSA de Perú.
- **Un modelo de aprendizaje automático de conjunto (ensemble):** modelos CatBoost, SVM y LSTM combinados mediante un Random Forest, según lo descrito en Sebastianelli et al. (2024).

Las estimaciones de riesgo se clasifican en cinco niveles (del más bajo al más alto) para las unidades administrativas subnacionales (departamento, provincia y distrito en Perú; estado y municipio en Brasil), y se actualizan mensualmente.

**Instituciones colaboradoras:** Escuela de Política y Estrategia Global de UC San Diego · New Light Technologies (NLT) · Universidad Peruana Cayetano Heredia (UPCH) · UNICEF **Financiador:** Wellcome

---

## 🤝 Cómo participar

DIRE es un proyecto de **ciencia abierta**. Creamos este repositorio para que investigadores, organismos de salud pública y la comunidad de código abierto en general puedan examinar, reproducir, mejorar y ampliar el trabajo, no solo leer sobre él. Existen varias maneras de participar, independientemente de su experiencia.

### Para investigadores y epidemiólogos

- **Reproducir y validar.** Cada flujo de procesamiento de [`workflows/`](https://github.com/DIRE-OSI/platform/blob/main/workflows) está documentado para que pueda volver a ejecutar los pasos de preparación de covariables y pronóstico utilizando los datos agregados incluidos. No se requieren credenciales ni datos privados. Consulte [docs/processing/](https://github.com/DIRE-OSI/platform/blob/main/docs/processing).
- **Ampliar la investigación.** Proponga nuevas covariables, arquitecturas de modelos alternativas, enfermedades adicionales u otros países. Abra una [discusión](https://github.com/DIRE-OSI/platform/discussions) para plantear una idea antes de desarrollarla.
- **Citar el trabajo.** Si DIRE contribuye a su investigación, cite tanto el software como el artículo metodológico en el que se basa. Consulte [Citación](https://github.com/DIRE-OSI/platform/blob/main/README.md#citation).

### Para profesionales de salud pública y personal de respuesta

- **Utilizar el panel.** La plataforma disponible en [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com/) puede utilizarse gratuitamente para planificación y conocimiento de la situación.
- **Contarnos qué necesita.** Las funciones de estimación de recursos y elaboración de informes se diseñan teniendo en cuenta las necesidades operativas reales. Abra un [issue](https://github.com/DIRE-OSI/platform/issues) en el que describa su caso de uso, las decisiones que toma y los resultados que le serían útiles.

### Para colaboradores y desarrolladores

- **Notificar problemas:** errores de software, documentación poco clara o dificultades para reproducir resultados.
- **Mejorar la documentación:** se agradecen especialmente las mejoras de claridad y las traducciones, dado que la plataforma se centra inicialmente en Perú y Brasil (español y portugués).
- **Enviar pull requests:** consulte [CONTRIBUTING.md](https://github.com/DIRE-OSI/platform/blob/main/CONTRIBUTING.md) para conocer el procedimiento y el requisito de firma de conformidad con el Certificado de Origen del Desarrollador (DCO).

### Para socios institucionales y proveedores de datos

- Trabajamos con datos de vigilancia de las autoridades sanitarias nacionales sujetos a los acuerdos pertinentes. Si su institución desea colaborar aportando datos, participando en la validación o ampliando la cobertura a otro país, comuníquese por los canales indicados en [docs/TEAM.md](https://github.com/DIRE-OSI/platform/blob/main/docs/TEAM.md).

**Normas de la comunidad.** La participación en este proyecto se rige por nuestro [Código de Conducta](https://github.com/DIRE-OSI/platform/blob/main/CODE_OF_CONDUCT.md). Léalo antes de participar.

---

## 🆘 Soporte y contacto

¿Necesita ayuda, ha encontrado un error o tiene alguna pregunta? Consulte [**SUPPORT.md**](https://github.com/DIRE-OSI/platform/blob/main/SUPPORT.md) para saber dónde dirigir cada solicitud. En resumen:

- **Errores, fallas o dificultades de reproducibilidad:** abra un [issue](https://github.com/DIRE-OSI/platform/issues/new/choose).
- **Preguntas, ideas, nuevas covariables, enfermedades o países:** inicie una [discusión](https://github.com/DIRE-OSI/platform/discussions).
- **Vulnerabilidades de seguridad:** siga las instrucciones de [SECURITY.md](https://github.com/DIRE-OSI/platform/blob/main/SECURITY.md) (no abra un issue público).
- **Comentarios sobre el panel en línea:** utilice el formulario de comentarios de [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com/).

Los nuevos issues reciben automáticamente un acuse de recibo y se asignan a las personas responsables de su mantenimiento.

---

## Contenido del repositorio

```
platform/
├── docs/
│   ├── data-sources/       # Guías de credenciales, licencias y cobertura por fuente
│   ├── processing/         # Instrucciones para ejecutar los flujos de principio a fin
│   ├── ABOUT.md            # Descripción de la plataforma, enfermedades, datos y referencias
│   ├── TEAM.md             # Equipo del proyecto e instituciones asociadas
│   └── ROADMAP.md          # Plan de publicación por fases
├── workflows/
│   ├── predictors/         # Flujo de Python: covariables climáticas y de teledetección
│   └── dengue_forecasting/ # Flujo de Python y R: pronósticos de incidencia de enfermedades
├── CITATION.cff            # Metadatos de citación legibles por máquina
├── CONTRIBUTING.md         # Flujo de PR y firma DCO
├── CODE_OF_CONDUCT.md      # Normas de la comunidad
├── LICENSE                 # Apache-2.0 (código fuente)
├── NOTICE                  # Atribuciones
├── SECURITY.md             # Divulgación de vulnerabilidades
├── DISCLAIMER.md           # Descargo de responsabilidad y condiciones de exención
└── .env.example            # Plantilla de credenciales

```

### Lo que todavía no está disponible aquí

| **Componente** | **Etapa prevista ([Hoja de ruta](https://github.com/DIRE-OSI/platform/blob/main/docs/ROADMAP.md))** |
| --- | --- |
| API de predicción / servicio de backend | En evaluación |
| Entorno de ejecución local en contenedores | Etapa III (flujos de trabajo abiertos) |
| Conjunto de pruebas automatizadas e integración continua (CI) | Etapa III (flujos de trabajo abiertos) |
| Código fuente del panel interactivo | En evaluación |
| Despliegue en la nube / infraestructura como código | En evaluación |
| Versión de archivo con DOI | Etapa IV (versión archivada) |

---

## Descripción general de la arquitectura

```
Fuentes de datos externas
  NASA Earthdata (MODIS, NASADEM) ─────────┐
  Copernicus CDS (ERA5-Land) ──────────────┤──► workflows/predictors/
  Brasil DATASUS SINAN ────────────────────┤        │  Tablas de covariables
  Perú MINSA (vigilancia) ──────────────────┘        ▼
                                        workflows/dengue_forecasting/
                                        ├── Preparación de variables
                                        ├── Conjunto CatBoost + SVM + LSTM
                                        └── Combinación mediante Random Forest
                                                   │
                                                   ▼
                                Resultados del pronóstico (casos previstos,
                                nivel de riesgo, clase de confianza)
                                por unidad administrativa × mes
                                                   │
                                                   ▼
                                dire.impact.nltglobal.com (panel en línea)

```

Consulte [docs/ABOUT.md](https://github.com/DIRE-OSI/platform/blob/main/docs/ABOUT.md) para ver la descripción completa y las referencias.

---

## Inicio rápido

### Requisitos previos

| **Herramienta** | **Versión** |
| --- | --- |
| Python | 3.11+ (se recomienda 3.12) |
| R | 4.5+ |
| uv (gestor de entornos de Python) | La más reciente |

### 1. Clonar el repositorio

```
git clone https://github.com/DIRE-OSI/platform.git
cd platform
```

### 2. Instalar las dependencias

```
# Flujo de predictores (teledetección y clima)
cd workflows/predictors && uv sync && cd ../..

# Flujo de pronóstico del dengue
cd workflows/dengue_forecasting && uv sync && cd ../..
```

### 3. Configurar las credenciales

```
cp .env.example .env
# Edite .env e introduzca sus credenciales gratuitas de API; consulte docs/data-sources/
```

### 4. Ejecutar un flujo de procesamiento

Las instrucciones completas se encuentran en [docs/processing/](https://github.com/DIRE-OSI/platform/blob/main/docs/processing). El flujo de pronóstico puede ejecutarse con los datos agregados incluidos **sin necesidad de credenciales externas**.

---

## Licencia

**Código fuente:** Licencia Apache 2.0; consulte [LICENSE](https://github.com/DIRE-OSI/platform/blob/main/LICENSE) y [NOTICE](https://github.com/DIRE-OSI/platform/blob/main/NOTICE). **Documentación y contenido distinto del código:** Creative Commons Atribución 4.0 Internacional (CC-BY-4.0).

---

## Citación

Si utiliza este software o los flujos de procesamiento de datos, cite tanto la versión del software como el artículo que describe la metodología subyacente.

- **Software:** New Light Technologies, Inc. (2026). *DIRE: Disease Incidence and Resource Estimator.* GitHub. Consulte [CITATION.cff](https://github.com/DIRE-OSI/platform/blob/main/CITATION.cff).
- **Metodología:** Sebastianelli, A., et al. (2024). *A reproducible ensemble machine learning approach to forecast dengue outbreaks.* Scientific Reports, 14, 3807. DOI: [10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)

---

## Financiamiento y agradecimientos

Este trabajo fue financiado mediante una subvención de **Wellcome Trust** a la **Universidad de California en San Diego (UCSD)**. El software fue desarrollado por **New Light Technologies (NLT), Inc.** Entre los colaboradores científicos se encuentra la **Universidad Peruana Cayetano Heredia (UPCH)**. El panel DIRE en línea es operado por NLT, Inc. y se encuentra actualmente en fase beta, con revisiones continuas de la experiencia de usuario y la calidad de los datos.
