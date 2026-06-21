from tools.calculator import evaluate as calc_evaluate
from tools.weather import get_weather as weather_get
from tools.text_converter import process_text as text_process


class SimpleAgent:
    """A tiny rule-based agent that routes to calculator, weather, or text converter tool."""

    def __init__(self):
        self.tools = {
            "calculator": calc_evaluate,
            "weather": weather_get,
            "text": text_process,
        }

    def handle(self, query: str) -> str:
        q = query.strip()
        low = q.lower()

        # Calculator triggers: startswith calc:, or contains math symbols
        if low.startswith("calc:") or low.startswith("calculate") or any(s in q for s in ["+", "-", "*", "/", "**", "(", ")"]):
            expr = q.split(":", 1)[1].strip() if ":" in q else q
            return self.tools["calculator"](expr)

        # Weather triggers: weather: or contains word weather/temperature
        if low.startswith("weather:") or "weather" in low or "temperature" in low:
            if ":" in q:
                loc = q.split(":", 1)[1].strip()
                if not loc:
                    return "Please provide a location after 'weather:' (e.g., weather: London)"
                return self.tools["weather"](loc)
            parts = q.split()
            if len(parts) >= 2:
                return self.tools["weather"](" ".join(parts[1:]))
            return "Please specify a location, e.g., 'weather: London'"

        # Text converter triggers: wordcount:, charcount:, or reverse:
        if low.startswith("wordcount:") or low.startswith("charcount:") or low.startswith("reverse:"):
            return self.tools["text"](q)

        return "I can answer three kinds of requests:\n  'calc:<expression>' (calculator)\n  'weather:<city>' (weather)\n  'wordcount:<text>', 'charcount:<text>', or 'reverse:<text>' (text tools)"


if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.handle("calc: 2+2*3"))
