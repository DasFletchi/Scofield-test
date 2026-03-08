#!/usr/bin/env python3
"""Michael Scofield's Escape Plan Generator"""

import random

def generate_escape_plan():
    plans = [
        "Dig through the wall with a spoon.",
        "Hack the security system from inside.",
        "Create a distraction with a fire.",
        "Trade something valuable for a favor.",
        "Find a blind spot in the patrols.",
        "Use the ventilation system.",
        "Convince a guard you're helpful.",
        "Wait for the right moment - patience is key."
    ]
    return random.choice(plans)

if __name__ == "__main__":
    print("🎯 Michael's Escape Plan:")
    print(generate_escape_plan())
