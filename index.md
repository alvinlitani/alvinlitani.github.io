---
layout: resume
fullname: Alvin Litani Liauw
headline: Applied machine learning, data pipelines, and production ML services
location: Ottawa, Ontario, Canada
contact:
  - text: alvin.litani@gmail.com
    url: mailto:alvin.litani@gmail.com
  - text: github.com/alvinlitani
    url: https://github.com/alvinlitani
  - text: linkedin.com/in/alvin-litani
    url: https://linkedin.com/in/alvin-litani
---

Computer science graduate with a graduate certificate in AI software development,
returning to engineering after a decade spanning payments infrastructure, IT
consulting, and operations. I build machine learning systems end to end — data
sourcing and feature engineering through to a deployed, documented service.

## Selected projects

### Ontario wind power forecasting
*XGBoost, FastAPI, Google Cloud Run — [github.com/alvinlitani/wind-power-forecast](https://github.com/alvinlitani/wind-power-forecast)*

- Produces daily hourly generation forecasts for all 45 IESO-reporting wind plants in Ontario, served through a FastAPI endpoint on Cloud Run.
- Trains on ERA5 reanalysis data and infers from Open-Meteo forecasts, using a general model refined into site-specific variants.
- Engineered physically motivated features: hub-height wind speed via power-law extrapolation, air density, gust ratio as a turbulence proxy, and sine/cosine wind direction encoding.
- Retains multi-height wind speeds without imposing monotonic shear assumptions, and passes turbine physical characteristics as static inputs.
- Built the turbine specification dataset by cross-referencing IESO generator records against the NRCan Canadian Wind Turbine Database and Ontario ERO filings.
- Iterated from LSTM and Temporal Fusion Transformer architectures to gradient boosting after evaluating accuracy against serving cost.

### Product manual RAG assistant
*LangChain, ChromaDB, Gradio, Docker*

- Retrieval-augmented question answering over product documentation, with a Gradio interface deployed to Hugging Face Spaces.
- Containerized with Docker for reproducible local and hosted runs.

### Celebrity face matching
*MTCNN, InceptionResnetV1, FAISS, Gradio*

- Face detection and embedding pipeline with FAISS similarity search over a reference index, deployed to Hugging Face Spaces.

## Experience

### Administrative support, part-time and remote
*PT Bangun Prima Sukses — 2023 to present*

- Remote administrative and reporting support alongside full-time study and portfolio work.

### Warehouse supervisor
*PT Bangun Prima Sukses — 2019 to 2023, Jakarta, Indonesia*

- Supervised daily warehouse operations, staffing, and inventory accuracy.
- [Add one line with a number: headcount supervised, throughput, or an error rate you improved.]

### Technical manager
*PT Perkasa Pilar Utama — 2015 to 2019, Jakarta, Indonesia*

- Led client-facing technical engagements, including IoT pilot deployments and evaluation.
- Negotiated partner and vendor agreements, and translated client requirements into delivery scope.

### Application and server administrator
*PT Midtrans — 2013 to 2015, Jakarta, Indonesia*

- Administered Java and Ruby applications on Linux for a national payment gateway.
- Handled deployment, monitoring, and incident response for production payment services.

### Technical sales and merchant support
*PT Midtrans — 2012 to 2013, Jakarta, Indonesia*

- Supported merchant integrations against the payment gateway API.
- Built and extended PHP e-commerce platform plugins to shorten merchant onboarding.

## Education

### Graduate certificate, artificial intelligence software development
*Algonquin College — completed August 2025*

### Bachelor of Computer Science and Technology
*University of Sydney — 2008 to 2011*

## Skills

**Machine learning** — XGBoost, PyTorch, scikit-learn, time series forecasting, feature engineering, LangChain, RAG, FAISS

**Engineering** — Python, Java, Ruby, SQL, FastAPI, Docker, Google Cloud Run, Linux, Git

**Data** — pandas, geospatial and meteorological data, ERA5, Open-Meteo, public regulatory datasets

**Languages** — English, Indonesian, Japanese (in progress)
