def propose_strategy(agent_id: str) -> dict:
    return {"dummy": True}

def update_strategies(generation_data):
    print("BO updated with", len(generation_data), "entries.")