<p align="center">
  <img src="assets/profile-hero.svg" alt="Siobhan Goh — AI, Data Science and Data Analytics" width="100%" />
</p>

<p align="center"><strong>Master of Artificial Intelligence · Monash University Malaysia</strong><br/>
Bachelor of Information Systems (Honours), Data Analytics · Sunway University</p>

<p align="center">
  <a href="https://www.linkedin.com/in/siobhan-goh/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://github.com/SiobhanGoh?tab=repositories">Repositories</a> &nbsp;·&nbsp;
  <a href="https://siobhangoh.github.io/RetailAI-Adaptive-Sales-Intelligence/">RetailAI app</a> &nbsp;·&nbsp;
  <a href="https://capstone2-sentiment-streamlit-colab.pages.dev/">Sentiment web app</a> &nbsp;·&nbsp;
  <a href="https://siobhangoh.github.io/klang-valley-blood-donation-dashboard/">Blood donation dashboard</a>
</p>

<p align="center"><sub>Currently interested in full-time internships across AI/ML, data science, analytics and business intelligence · November 2026–February 2027</sub></p>

---

### A little about me

I turn complex data into useful **analyses, experiments and applications**. My background connects statistical reasoning, machine learning, NLP and business intelligence. I enjoy both sides of the process: **building models** and **explaining what their results do—and do not—mean**.

I am particularly interested in projects where the technical work supports real decisions, from multilingual text classification to retail analytics and interpretable forecasting.

**Explore:** [Featured builds](#featured-builds) · [Graduate research](#selected-graduate-research) · [Toolkit](#toolkit) · [Connect](#lets-connect)

### Featured builds

I keep revisiting my past projects rather than leaving them as they were first submitted: re-checking the results, fixing what fell short and rebuilding when a better design is possible. Each project lists what changed in its latest round.

#### 01 · [RetailAI — Adaptive Sales Intelligence](https://github.com/SiobhanGoh/RetailAI-Adaptive-Sales-Intelligence)
<sub>First built May 2026 · rebuilt as version 2 in November 2026</sub>

Open a CSV or Excel sales export and get trends, forecasts with error bands, customer segments and product pairings, all calculated in your browser. The file never leaves the tab. Three built-in sample stores let you try it straight away: a fictional US office-supplies store, a real UK online gift shop and a synthetic Malaysian grocery chain priced in RM.

**What improved in version 2**
- **New platform:** moved off Streamlit to a static browser app that doesn't sleep, with a new order-ticket interface and light and dark modes.
- **Better forecasts:** one model with a made-up confidence score became four models, each replayed on past weeks, with the best one chosen and error bands drawn from its past mistakes.
- **More faithful data handling:** returns and duplicate rows are kept and reported instead of silently dropped. Column detection no longer mistakes prices for revenue or ship dates for order dates.
- **Honest labels:** a "business health score" that only measured dataset size, and rule-based features branded as AI, were removed or renamed.
- **New features:** customer segments and cohorts, product pairings, explanations for unusual weeks, comparisons with last year and CSV exports.
- **Better sample data:** the original US sample couldn't show returns, margins or real repeat buying, so I added real UK invoices (CC BY 4.0) and a Malaysian store built from official data.gov.my product and retail-trade data, with Raya and Chinese New Year peaks.

[Live app](https://siobhangoh.github.io/RetailAI-Adaptive-Sales-Intelligence/) · [Explore source](https://github.com/SiobhanGoh/RetailAI-Adaptive-Sales-Intelligence)

#### 02 · [Malay–English Sentiment Analysis](https://github.com/SiobhanGoh/capstone2-sentiment-streamlit-colab)
<sub>First built December 2025 · re-evaluated October 2026 · web app November 2026</sub>

Negative / Neutral / Positive sentiment for Malay, English and code-switched text, using a fine-tuned multilingual BERT.

**What improved**
- **Corrected evaluation (Oct 2026):** the original train/test splits overlapped, so I rebuilt the evaluation on one shared, disjoint split. Corrected result: 76.04% test accuracy, against 66.46% for a TF-IDF baseline.
- **Private, always-on web app (Nov 2026):** a 16-bit ONNX copy of the model now runs inside the visitor's browser, so text never leaves their device. It gives the same labels as the full model on the 981-input test set.
- **Richer comment analysis:** pull up to 100 YouTube comments, or paste or upload up to 1,000. A results dashboard shows the label mix, creator notes (most-liked negative comments, viewer questions), theme and Malaysian-state maps and a comment timeline, plus PDF, CSV and copyable summaries. Two videos can be compared side by side.
- **Explainable and correctable:** "Why this label?" shades the words that move the score most, and "Wrong label?" lets users record the right label, collected as a hand-checked test set for the next model.
- **Next model, in progress:** a notebook compares Malaysian DeBERTa-v2, Malaysian RoBERTa and XLM-T under the same corrected protocol, choosing the winner on validation before any test score is computed.

[Live web app](https://capstone2-sentiment-streamlit-colab.pages.dev/) · [Explore source](https://github.com/SiobhanGoh/capstone2-sentiment-streamlit-colab/tree/browser-model) · [Original Streamlit demo](https://huggingface.co/spaces/SiobhanGoh/emotion-detection-malaybert-skeleton) <sub>(wakes up after a minute when idle)</sub>

#### 03 · [Klang Valley Blood Donation Forecasts](https://github.com/SiobhanGoh/klang-valley-blood-donation-dashboard)
<sub>November 2026 · grew out of my BloodReady AI analysis</sub>

An R Shiny dashboard of daily blood-donation collections in the Klang Valley by ABO blood group.

**What improved**
- **From one-off report to live dashboard:** my BloodReady R Markdown analysis now refreshes every morning with the latest data.gov.my records, through a tested GitHub Actions pipeline.
- **Still checked against the original:** automated tests confirm the four forecasting methods still reproduce the report's results on its frozen snapshot.
- **Easier to explore:** a story-style layout in plain words, with interactive charts, light and dark themes, a live tracker, low-collection-day errors, a Blood 101 guide for donors and printable reports.
- **Faster to open:** I cut the browser download by drawing charts directly with plotly.js and loading 46 R packages instead of 66, so the first visit now takes around half a minute.

[Live dashboard](https://siobhangoh.github.io/klang-valley-blood-donation-dashboard/) <sub>(first visit takes around half a minute while R loads)</sub> · [Explore source](https://github.com/SiobhanGoh/klang-valley-blood-donation-dashboard)

> These are portfolio prototypes and academic projects—not validated production decision systems. See individual READMEs for model-evaluation limitations.

### Selected graduate research

Beyond my published apps, my master's coursework includes **implemented** work in R-based analytics, deep learning and model evaluation:

- **BloodReady AI · R / Forecasting:** analysed Malaysian blood-donation records, compared four interpretable forecast approaches over retrospective years, and reported low-collection-day limitations. *The R Markdown analysis is now the basis of the [live dashboard](https://github.com/SiobhanGoh/klang-valley-blood-donation-dashboard), whose tests confirm it still reproduces the report's results.*
- **Deep Learning · PyTorch / Transformers:** implemented neural networks, sequence classifiers, a scratch Transformer and BERT fine-tuning, with training, evaluation and checkpoint-handling workflows.
- **Computer Vision · Transfer Learning:** explored ensemble inference with frozen pretrained CLIP, SigLIP, SigLIP2 and DINOv2 encoders, including low-resolution validation checks.

<details>
<summary><strong>What I'm learning about rigorous evaluation</strong></summary>
<br/>
Research and application development require more than a high metric. My recent work has involved chronological evaluation, baseline comparisons, feature-selection controls, validation-set limitations and correcting problematic preprocessing. I prefer to document uncertainty and use models as decision-support tools rather than promising unsupported accuracy or business impact.
</details>

### Toolkit

**Languages & analysis** · Python · R · TypeScript · Pandas · NumPy · scikit-learn · statistical modelling  
**Machine learning & NLP** · PyTorch · Transformers · BERT fine-tuning · classical ML · model evaluation  
**Visualisation & applications** · React · R Shiny / Shinylive · Streamlit · Plotly · Matplotlib · ggplot2 · R Markdown · ReportLab  
**Deployment & tools** · ONNX / transformers.js · GitHub Actions · GitHub Pages · Cloudflare Pages · Hugging Face Spaces · Jupyter / Google Colab

<details>
<summary><strong>Additional technical work</strong></summary>
<br/>
Selected work also includes Bayesian-network inference and decision analysis, large-file Bash/AWK data processing, model-selection diagnostics and research-led interface design. I only share course material publicly when publication is permitted and private information has been removed.
</details>

### Let's connect

I'm open to internship opportunities across **AI, Machine Learning, Data Science, Data Analytics and Business Intelligence**. The best way to reach me is via [LinkedIn](https://www.linkedin.com/in/siobhan-goh/).

<p align="center"><sub>Thoughtful models. Clear analysis. Useful outcomes. ♡</sub></p>