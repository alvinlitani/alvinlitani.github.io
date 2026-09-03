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

Machine learning engineer focused on building and deploying ML systems: [time-series forecasting for wind generation](https://github.com/alvinlitani/wind-power-forecast) served through a FastAPI service on Google Cloud Run, retrieval-augmented generation over enterprise documentation, and computer vision similarity search. Nearly three years of production infrastructure experience maintaining Java and Ruby applications, and over four years in client-facing technical roles before the move into ML. Computer science graduate with a recent graduate certificate in AI software development from Algonquin College.

Eligible to work in Canada without sponsorship. Open to relocation anywhere in Canada, or remote.

## Selected projects

### Wind power forecasting, Ontario
*XGBoost, FastAPI, Google Cloud Run - [github.com/alvinlitani/wind-power-forecast](https://github.com/alvinlitani/wind-power-forecast) | [live API](https://wind-forecast-api-654769911920.us-central1.run.app/predictions/ontario)*

Day-ahead hourly forecasts for all 45 IESO-reporting wind plants in Ontario (4,943 MW, ~90% of provincial wind capacity). Per-site XGBoost models predict capacity factor and are trained on historical weather forecasts rather than actuals to avoid train/serve data mismatch. 11.3% capacity-weighted nMAE over a full-year 2025 test set (394,006 site-hours); 0.37 MAE skill score against a persistence baseline in live daily runs. Prefect Cloud schedules a Cloud Run Job writing to GCS, with a separate FastAPI service serving predictions and fail-closed data quality gates throughout.

### Celebrity face matching
*facenet-pytorch, FAISS, Gradio - [github.com/alvinlitani/Celebrity-Face-Matching](https://github.com/alvinlitani/Celebrity-Face-Matching) | [live demo](https://huggingface.co/spaces/aliauw/celebrity-face-matching)*

A computer vision app that takes a personal photo as input and finds which celebrity in [CelebA dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) that the person most resemble using face embeddings and nearest-neighbor search. It is built with facenet-pytorch and FAISS. Hosted on HuggingFace.

### Product manual assistant
*LangChain, ChromaDB, Hugging Face - [github.com/alvinlitani/RAG-for-Product-Manual-Assistant](https://github.com/alvinlitani/RAG-for-Product-Manual-Assistant) | [live demo](https://huggingface.co/spaces/aliauw/product-manual-assistant)*

A RAG (Retrieval-Augmented Generation) chatbot that answers technical questions about product documentation. Built with LangChain v1, HuggingFace, and ChromaDB. Hosted on HuggingFace.

## Experience

### Accounts receivable support (part-time, remote)
*PT Bangun Prima Sukses, Indonesia (2025-present)*

Construction materials supplier.

- Remote accounts receivable and reporting support.

### Warehouse supervisor
*PT Bangun Prima Sukses, Indonesia (2019-2023)*

- Supervised a team of 10+ and a fleet of 8 delivery trucks covering scheduling, training, and day-to-day performance management.
- Coordinated delivery schedules to 20+ active construction sites.

### Technical manager
*PT Perkasa Pilar Utama, Indonesia (2015-2019)*

IT consultancy building systems for government and business clients. Introducing new Internet of Things/IoT (LoRaWAN) technology to the Indonesian market. Continue to advise informally on their adoption of agentic coding tools (2025 – present).

- Negotiated partnership and joint-venture agreements including contract terms with global technology vendors across 4 countries.
- Ran multi-day LoRaWAN trials at 5 client sites (cellular base stations, a public water pipeline, a plantation, a frozen food warehouse, and a mining site) handling logistics and leading the on-site technical demonstrations.
- Evaluated 20+ vendor hardware and software platforms for product-market fit against enterprise requirements in the Indonesian market.
- Acted as technical point of contact across 4 enterprise accounts and coordinated 5-person teams spanning engineering, logistics, and sales.
- Created technical pitch documents and supporting data analysis for business proposals to clients.

### Application administrator
*PT Midtrans, Indonesia (2013-2015)*

Payment gateway processing card and bank transfers for hundreds of Indonesian e-commerce merchants. Part of the infrastructure team and 2 DevOps teams.

- Monitored and tuned 5 Java and Ruby applications across 3 Linux servers, maintaining 99.9% uptime on live payment processing.
- Introduced application performance telemetry with New Relic, cutting incident detection from hours to roughly 15 minutes.
- Traced production failures through application and system logs to isolate root causes.
- Deployed releases and ran rollbacks weekly, handling around 2 production incidents a week on a 2-person on-call rotation.
- Supported the fraud monitoring team weekly by reviewing transaction logs for suspicious activity.

### Technical sales and merchant support
*PT Midtrans, Indonesia (2012-2013)*

Early-stage startup with no dedicated technical support for the sales team.

- Built and modified 3 PHP payment extensions for the Magento, Drupal, and WooCommerce e-commerce platforms.
- Supported around 2 merchant integrations a week, working with client engineering teams to troubleshoot API and transaction failures.
- Joined near-daily client meetings as the technical contact alongside sales, covering roughly 4 prospects a week.

## Education

### Graduate Certificate in Artificial Intelligence Software Development
*Algonquin College, Ontario (2024-2025)*

### Graduate Certificate in Supply Chain Management
*Algonquin College, Ontario (2023-2024)*

### Bachelor of Computer Science and Technology
*University of Sydney, Australia (2008-2011)*

## Skills

**Languages** - Python, SQL; Java, Ruby, PHP (working exposure)

**Machine learning and AI** - PyTorch, scikit-learn, XGBoost, LangChain, ChromaDB, FAISS, facenet-pytorch, Hugging Face, pandas, NumPy

**Tools and infrastructure** - Linux, Docker, Git, FastAPI, Google Cloud Run, Hugging Face Spaces, Gradio, New Relic

**Concepts** - Time-series forecasting, RAG, vector search, embeddings, LLM APIs, prompt engineering, NLP, sentiment analysis, computer vision

**Spoken languages** - English (professional), Indonesian (native)
