"""Quickstart: consulta de risco de congestão para um ou varios portos.

Rode com:
    pip install "aetherx-oracle[async]"
    export RAPIDAPI_KEY="sua-chave"
    python examples/quickstart.py
"""
import asyncio
import os

from aetherx import OracleClient

API_KEY = os.environ.get("RAPIDAPI_KEY", "SUA_RAPIDAPI_KEY")


def single_port() -> None:
    client = OracleClient(api_key=API_KEY)
    risk = client.get_port_risk("BRSSZ")

    print(f"{risk.port_name} ({risk.port_id}) - {risk.country}")
    print(f"  congestion_score        = {risk.congestion_score}")
    print(f"  eta_delay_days          = {risk.eta_delay_days}")
    print(f"  waiting_vessels         = {risk.waiting_vessels}")
    print(f"  freight_volatility_idx  = {risk.freight_volatility_index}")
    print(f"  updated_at              = {risk.updated_at}")


async def batch_ports() -> None:
    client = OracleClient(api_key=API_KEY)
    ports = ["BRSSZ", "CNSHA", "NLRTM", "USLAX"]

    risks = await client.get_ports_risk_async(ports)
    for risk in risks:
        print(f"{risk.port_id}: {risk.congestion_score}")


if __name__ == "__main__":
    print("== Um porto ==")
    single_port()
    print("\n== Varios portos em paralelo ==")
    asyncio.run(batch_ports())
