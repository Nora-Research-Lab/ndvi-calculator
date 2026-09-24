![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# NDVI Calculator
 
*For remote sensing analysts and ecologists: enter red and near-infrared reflectance values to instantly compute the Normalized Difference Vegetation Index (NDVI) and get a vegetation density classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Remote Sensing & Earth Observation
 
Inputs: (a) Red reflectance (unitless, 0.0–1.0) from a satellite or field sensor, entered via a number input or slider; (b) NIR reflectance (unitless, 0.0–1.0), same input type. Both require two decimal places. Calculation: NDVI = (NIR - Red) / (NIR + Red). If NIR + Red is 0, return NDVI = 0 (edge case). Output: (1) Numerical NDVI value displayed to three decimal places with a color-coded badge (red for negative, yellow for low, green for high). (2) A classification table mapped from the NDVI range: <0 → 'Water / Non-vegetated', 0–0.2 → 'Bare Soil / Sparse Vegetation', 0.2–0.4 → 'Moderate Vegetation', 0.4–0.6 → 'Dense Vegetation', >0.6 → 'Very Dense Vegetation'. (3) A horizontal color bar from red (NDVI=-1) through yellow/green to dark green (NDVI=+1) with a marker showing the computed value. UI: Gradio interface with two labeled input fields, a 'Calculate' button, and output area with the numeric value, classification text, and color bar (generated using matplotlib). No AI/ML component; pure mathematical calculation.
 
## Run it
 
```bash
docker build -t ndvi-calculator .
docker run -p 7860:7860 ndvi-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-24.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
