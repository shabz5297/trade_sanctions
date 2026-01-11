import os
import requests
import pandas as pd
import time
import plotly.graph_objects as go
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('COMTRADE_KEY')

# Countries and Commodities
UAE, SUDAN = '784', '729'
NEIGHBORS = {'Chad': '148', 'Libya': '434', 'Egypt': '818'}
HS_CODES = {'Gold': '7108', 'Machinery': '8429', 'Weapon_Parts': '9305'}


def fetch_trade(reporter, partner, item_code, flow):
    url = "https://comtradeapi.un.org/data/v1/get/C/A/HS"
    params = {
        'reporterCode': reporter,
        'partnerCode': partner,
        'period': '2021,2022,2023',
        'cmdCode': item_code,
        'flowCode': flow,
        'subscription-key': API_KEY
    }
    time.sleep(2)  # Reduced sleep slightly for efficiency
    try:
        r = requests.get(url, params=params, timeout=15)
        return r.json().get('data', [])
    except:
        return []


# --- DATA COLLECTION ---
all_results = []
for name, code in NEIGHBORS.items():
    print(f"Collecting data for {name}...")
    # Gold coming IN to UAE
    gold = fetch_trade(UAE, code, HS_CODES['Gold'], 'M')
    # Tech/Parts going OUT of UAE
    mach = fetch_trade(UAE, code, HS_CODES['Machinery'], 'X')
    weap = fetch_trade(UAE, code, HS_CODES['Weapon_Parts'], 'X')

    for entry in gold + mach + weap:
        all_results.append({
            'Neighbor': name,
            'Item': 'Gold' if entry['cmdCode'] == '7108' else (
                'Machinery' if entry['cmdCode'] == '8429' else 'Weapon_Parts'),
            'Value_USD': entry['primaryValue'],
            'Direction': 'Inbound' if entry['flowCode'] == 'M' else 'Outbound'
        })

df = pd.DataFrame(all_results)
df.to_csv("sudan_trade_data.csv", index=False)
print("CSV Saved: sudan_trade_data.csv")

# --- SANKEY VISUALIZATION ---
# We define our nodes (The actors)
nodes = ["Sudan (Shadow)", "Chad", "Libya", "Egypt", "UAE Hub"]
# Indices: 0: Sudan, 1: Chad, 2: Libya, 3: Egypt, 4: UAE

# We create the links based on your findings
# Source -> Target
fig = go.Figure(data=[go.Sankey(
    node=dict(pad=15, thickness=20, label=nodes, color="blue"),
    link=dict(
        source=[1, 2, 3, 4, 4],  # Chad, Libya, Egypt, UAE, UAE
        target=[4, 4, 4, 1, 2],  # All Gold to UAE, then UAE sends back to Chad/Libya
        value=[
            df[(df['Neighbor'] == 'Chad') & (df['Item'] == 'Gold')]['Value_USD'].sum(),
            df[(df['Neighbor'] == 'Libya') & (df['Item'] == 'Gold')]['Value_USD'].sum(),
            df[(df['Neighbor'] == 'Egypt') & (df['Item'] == 'Gold')]['Value_USD'].sum(),
            df[(df['Neighbor'] == 'Chad') & (df['Item'] != 'Gold')]['Value_USD'].sum(),
            df[(df['Neighbor'] == 'Libya') & (df['Item'] != 'Gold')]['Value_USD'].sum()
        ],
        color=["gold", "gold", "gold", "red", "red"]  # Gold for income, Red for weapons/machinery
    )
)])

fig.update_layout(title_text="The Sudan Proxy Trade Loop: Gold vs. Logistics", font_size=12)
fig.show()