temperatures = [36.6, 37.2, 38.1, 39.0, 37.8, 36.4]

rows = []
for temp in temperatures:
    if temp < 37.5:
        rows.append(f"✅ {temp:.1f} °C  → Normal")
    elif temp < 39.0:
        rows.append(f"⚠️ {temp:.1f} °C  → Fever")
    else:
        rows.append(f"🚨 {temp:.1f} °C  → High fever")

print("\n┌──────────────────────────────────────┐")
print("│       MEDASSISTANT: ТРІАЖ            │")
print("├──────────────────────────────────────┤")
for row in rows:
    print(f"│  {row.ljust(34)}  │")
print("└──────────────────────────────────────┘")

"""
┌──────────────────────────────────────┐
│       MEDASSISTANT: ТРІАЖ            │
├──────────────────────────────────────┤
│  ✅ 36.6 °C  → Normal                 │
│  ✅ 37.2 °C  → Normal                 │
│  ⚠️ 38.1 °C  → Fever                 │
│  🚨 39.0 °C  → High fever             │
│  ⚠️ 37.8 °C  → Fever                 │
│  ✅ 36.4 °C  → Normal                 │
└──────────────────────────────────────┘
"""
