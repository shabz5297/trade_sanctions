# Trade Sanctions & Intermediary Routing Analysis

This project investigates whether international trade data exhibits structural patterns
consistent with intermediary routing and sanctions circumvention. Using public UN Comtrade data, 
the project explores how high-value exports and sensitive imports may co-exist across selected country 
pairs and regions

The aim is not to make legal or political claims, but to demonstrate how data analysis,
visualisation, and network methods can be used identify discrete trade patterns 
using open data.

#Project Status

**Curent Stage:** Data extractions and analysis framwork
**Focus case studies:**
- USA - Israel
- Sudan - regional neighbours & UAE

This is an evolving research based project, which emphasises transparency reproducibility and learning from
building.

## Key Questions
- Do Certain country pairs show recursive trade imbalances between high-value exports and sensitive imports?
- Are trade flows concentrated in a small number of partners
- Can network structure highlight potential mediator or "bridge" behaviour?
- How do these patterns evolve over time?

## Data Source

- **UN Comtrade API (v1)**
- Annual HS-code level trade data (2021–2023)

### Example HS Categories Used
- Gold (HS 7108)
- Heavy machinery (HS 8429)
- Weapon parts (HS 9305)
- Drone systems / parts (HS 8806 / 8807)
- Electronic components (HS 8542)

---

## Tech Stack

- **Python**
- **Pandas** – data cleaning and aggregation  
- **NumPy** – numerical operations  
- **Matplotlib** – time-series and comparative visualisation  
- **NetworkX** – trade network construction and centrality analysis  
- **Git / GitHub** – version control and reproducibility  

---

## Repository Structure
