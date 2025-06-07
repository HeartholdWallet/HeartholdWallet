# 🫶 Hearthold Wallet

**Hearthold** is a secure Solana wallet with AI-powered risk detection and intuitive insights — built to protect your assets calmly and confidently.

## 🔑 Key Features

### 🕯️ SignalScan Engine  
Scans token parameters to detect:
- Open Mint Authority  
- Freeze Capabilities  
- Unlocked Liquidity  

### 💀 Risk Index Calculator  
Evaluates token safety on a 0–100 scale using:
- Known Vulnerabilities  
- Blacklist Status  
- Ownership Change Patterns  

### 🐋 WhaleLens  
Analyzes wallet distribution to uncover:
- Whale Dominance  
- Supply Imbalance  
- Potential Dump Signals  

### 🧭 TrustLabel Translator  
Translates numeric risk into intuitive labels:
- 🟢 Safe  
- 🟡 Watch  
- 🔴 Risk  

### 🪶 Insight Memory Log  
Continuously logs token risk behavior to detect:
- Slow-burn Threats  
- Behavioral Shifts  
- Long-term Red Flags  

---

## 🌅Road Ahead

### 🔹 Q3 2025 — Foundation Set  
✅ MVP Launch:
- Send / Swap  
- NFT Viewer  
- Activity Log  
✅ HearthKey Activation Layer  
✅ Live AI Risk Tags + Real-Time Token Monitoring  
⚠️ Whale Cluster Detection (Beta Phase)

### 🔹 Q4 2025 — Expansion Phase  
🔁 EVM Chain Support (Ethereum + BNB)  
📊 Smart Asset Metrics:
- Risk Overlays  
- Movement Heatmaps  

### 🔹 Q1 2026 — Intelligence Lift  
🧠 DEX Flow Forecasting (AI-driven trend anticipation)  
💬 Sentiment Signals across supported chains  
🗳️ Role-Based Governance powered by $HEARTH token  

---
## Under the Hood

Hearthold is driven by a suite of intelligent scanners and behavioral engines that work in real time — not just to detect risks, but to understand their patterns and evolution.

### 🕯️ SignalScan Engine  
**Purpose:** Spot hidden traps in token settings

```python
def scan_token(token):
    flags = []
    if token.get("mint_authority") == "open":
        flags.append("Open Mint")
    if token.get("freeze_authority") == "active":
        flags.append("Can Freeze Tokens")
    if not token.get("liquidity_locked", False):
        flags.append("No Liquidity Lock")
    return flags
```
#### AI Insight:
Scans for silent red flags like open mints, freeze permissions, and liquidity issues — comparing against known exploit patterns to catch threats before they surface.

### 💀 Risk Index Calculator
#### Purpose: Assign a dynamic 0–100 trust score

```python
def hearth_score(token):
    score = 100
    if token.get("blacklist"): score -= 40
    if token.get("mint_authority") == "open": score -= 25
    if not token.get("liquidity_locked", True): score -= 20
    if token.get("owner_changed_recently"): score -= 15
    return max(0, score)
```
#### AI Insight:
Think of it as your digital gut instinct. Each token flaw lowers the score. Calibrated on past scams, the system evolves with every flag and correction.

### 🐋 WhaleLens
#### Purpose: Reveal holder concentration risks

```javascript
function scanHolders(holders) {
  const whales = holders.filter(h => h.balance >= 0.05);
  return whales.length > 5 ? 'Whale Dominated' : 'Balanced';
}
```
#### AI Insight:
When a few wallets hold the power, you're likely not in control. WhaleLens flags unhealthy centralization before it leads to sudden dumps.

### 🧭 TrustLabel Translator
#### Purpose: Simplify raw scores into human-readable tags

```javascript
function label(score) {
  if (score >= 80) return "Safe";
  if (score >= 50) return "Watch";
  return "Risk";
}
```
#### AI Insight:
Translates score into intuitive weather:

- Safe — clear skies

- Watch — clouds forming

- Risk — storm incoming. Labels evolve with feedback, usage patterns, and community signals.

### 🪶 Insight Memory Log
#### Purpose: Track risk patterns over time

```python
def log_insight(token_id, label, score):
    log = {
        "token": token_id,
        "label": label,
        "score": score,
        "time": datetime.utcnow().isoformat()
    }
    insights_db[token_id] = {**insights_db.get(token_id, {}), **log}
```
#### AI Insight:
Every scan becomes memory. Hearthold builds token timelines, tracks shifts in risk, and refines its detection logic as threats evolve. It doesn’t forget — it learns.

---

## 🫧 Closing Thought

> Hearthold isn’t just a wallet — it’s your quiet guardian  
> Reading the chain. Remembering the patterns. Acting with care.

---
