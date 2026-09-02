---
layout: resume
fullname: Alvin Litani Liauw
headline: Machine learning engineer
location: Ottawa, Ontario, Canada
contact:
  - text: alvin.litani@gmail.com
    url: mailto:alvin.litani@gmail.com
  - text: github.com/alvinlitani
    url: https://github.com/alvinlitani
  - text: linkedin.com/in/alvin-litani
    url: https://linkedin.com/in/alvin-litani
---

Machine learning engineer focused on building and deploying ML systems:
[time-series forecasting for wind generation](https://github.com/alvinlitani/wind-power-forecast)
served through a FastAPI service on Google Cloud Run, retrieval-augmented
generation over enterprise documentation, and computer vision similarity search.
Three years of production infrastructure experience maintaining Java and Ruby
applications, and four years in client-facing technical roles before the move
into ML. Computer science graduate with a recent graduate certificate in AI
software development from Algonquin College.

Eligible to work in Canada without sponsorship. Open to relocation anywhere in
Canada, or remote.

## Selected projects

### Wind power forecasting, Ontario
*XGBoost, FastAPI, Google Cloud Run — [repository](https://github.com/alvinlitani/wind-power-forecast) · [live API](https://wind-forecast-api-654769911920.us-central1.run.app/predictions/latest)*

- Produces daily hourly generation forecasts for all 45 IESO-reporting wind plants in Ontario, served through a FastAPI endpoint on Cloud Run.
- Trains on ERA5 reanalysis data and infers from Open-Meteo forecasts, using a general model refined into site-specific variants.
- Engineered physically motivated features: hub-height wind speed via power-law extrapolation, air density, gust ratio as a turbulence proxy, and sine/cosine wind direction encoding.
- Retains multi-height wind speeds without imposing monotonic shear assumptions, and passes turbine physical characteristics as static inputs.
- Built the turbine specification dataset by cross-referencing IESO generator records against the NRCan Canadian Wind Turbine Database and Ontario ERO filings.
- Iterated from LSTM and Temporal Fusion Transformer architectures to gradient boosting after evaluating accuracy against serving cost.

### Celebrity face matching
*facenet-pytorch, FAISS, Gradio — [repository](https://github.com/alvinlitani/Celebrity-Face-Matching) · [live demo](https://huggingface.co/spaces/aliauw/celebrity-face-matching)*

- Takes a photo and returns the closest match from the [CelebA dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) using face embeddings and nearest-neighbour search.
- MTCNN detection and InceptionResnetV1 embeddings, indexed with FAISS for similarity search; deployed to Hugging Face Spaces.

### Product manual assistant
*LangChain, ChromaDB, Hugging Face — [repository](https://github.com/alvinlitani/RAG-for-Product-Manual-Assistant) · [live demo](https://huggingface.co/spaces/aliauw/product-manual-assistant)*

- Retrieval-augmented chatbot answering technical questions about product documentation, built with LangChain v1 and ChromaDB.
- Containerized with Docker for reproducible local and hosted runs; deployed to Hugging Face Spaces.

## Experience

### Accounts receivable support (part-time, remote)
*PT Bangun Prima Sukses — 2025 to present, Jakarta, Indonesia*

Construction materials supplier.

- Remote accounts receivable and reporting support alongside full-time study and portfolio work.

### Warehouse supervisor
*PT Bangun Prima Sukses — 2019 to 2023, Jakarta, Indonesia*

- Supervised a team of 10+ and a fleet of 8 delivery trucks, covering scheduling, training, and day-to-day performance management.
- Coordinated delivery schedules to 20+ active construction sites.

### Technical manager
*PT Perkasa Pilar Utama — 2015 to 2019, Jakarta, Indonesia*

IT consultancy building systems for government and business clients, introducing
LoRaWAN to the Indonesian market.

- Negotiated partnership and joint-venture agreements, including contract terms, with global technology vendors across four countries.
- Ran multi-day LoRaWAN trials at five client sites — cellular base stations, a public water pipeline, a plantation, a frozen food warehouse, and a mining site — handling logistics and leading the on-site technical demonstrations.
- Evaluated 20+ vendor hardware and software options for product-market fit against enterprise requirements in the Indonesian market.
- Acted as technical point of contact across four enterprise accounts, coordinating five-person teams spanning engineering, logistics, and sales.
- Created technical pitch documents and supporting data analysis for client proposals.

### Application administrator
*PT Midtrans — 2013 to 2015, Jakarta, Indonesia*

Payment gateway processing card and bank transfers for hundreds of Indonesian
e-commerce merchants.

- Monitored and tuned five Java and Ruby applications across three Linux servers, maintaining 99.9% uptime on live payment processing.
- Introduced application performance telemetry with New Relic, cutting incident detection from hours to roughly 15 minutes.
- Traced production failures through application and system logs across two DevOps teams to isolate root causes.
- Deployed releases and ran rollbacks weekly, handling around two production incidents a week on a two-person on-call rotation.
- Supported the fraud monitoring team weekly, reviewing transaction logs for suspicious activity.

### Technical sales and merchant support
*PT Midtrans — 2012 to 2013, Jakarta, Indonesia*

Early-stage startup with no dedicated technical support for the sales team.

- Built and modified three PHP payment extensions for the Magento, Drupal, and WooCommerce e-commerce platforms.
- Supported around two merchant integrations a week, working with client engineering teams to troubleshoot API and transaction failures.
- Joined near-daily client meetings as the technical contact alongside sales, covering roughly four prospects a week.

## Education

### Graduate Certificate in Artificial Intelligence Software Development
*Algonquin College, Ontario, Canada*
*2024-2025*

### Graduate Certificate in Supply Chain Management
*Algonquin College — 2023-2024, Ottawa, Ontario*

### Bachelor of Computer Science and Technology
*University of Sydney — 2008-2011, Australia*

## Skills

**Languages** — Python, SQL; Java, Ruby, PHP (working exposure)

**Machine learning and AI** — PyTorch, scikit-learn, XGBoost, LangChain, ChromaDB, FAISS, facenet-pytorch, Hugging Face, pandas, NumPy

**Tools and infrastructure** — Linux, Docker, Git, FastAPI, Google Cloud Run, Hugging Face Spaces, Gradio, New Relic

**Concepts** — Time-series forecasting, RAG, vector search, embeddings, LLM APIs, prompt engineering, NLP, sentiment analysis, computer vision

**Spoken languages** — English (professional), Indonesian (native)
