from tools.calculator import evaluate as calc_evaluate
from tools.weather import get_weather as weather_get


class SimpleAgent:
    """A tiny rule-based agent that routes to a calculator or weather tool."""

    def __init__(self):
        self.tools = {
            "calculator": calc_evaluate,
            "weather": weather_get,
        }

    def handle(self, query: str) -> str:
        q = query.strip()
        low = q.lower()

        # Calculator triggers: startswith calc:, or contains math symbols
        if low.startswith("calc:") or low.startswith("calculate") or any(s in q for s in ["+", "-", "*", "/", "**", "(", ")"]):
            # if user used prefix, take the remainder
            expr = q.split(":", 1)[1].strip() if ":" in q else q
            return self.tools["calculator"](expr)

        # Weather triggers: weather: or contains word weather/temperature
        if low.startswith("weather:") or "weather" in low or "temperature" in low:
            # parse location after 'weather:' if provided
            if ":" in q:
                loc = q.split(":", 1)[1].strip()
                if not loc:
                    return "Please provide a location after 'weather:' (e.g., weather: London)"
                return self.tools["weather"](loc)
            # otherwise try to extract a location word
            parts = q.split()
            if len(parts) >= 2:
                # assume last token is location
                return self.tools["weather"](" ".join(parts[1:]))
            return "Please specify a location, e.g., 'weather: London'"

        return "I can answer two kinds of requests: 'calc:<expression>' or 'weather:<city>'."


if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.handle("calc: 2+2*3"))
