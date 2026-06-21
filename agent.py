from tools.calculator import evaluate as calc_evaluate
from tools.weather import get_weather as weather_get
from tools.text_converter import process_text as text_process
from tools.json_formatter import process_json as json_process
from tools.url_handler import process_url as url_process
from tools.password_generator import process_password as pwd_process


class SimpleAgent:
    """A tiny rule-based agent that routes to calculator, weather, text converter, JSON formatter, URL handler, or password generator tool."""

    def __init__(self):
        self.tools = {
            "calculator": calc_evaluate,
            "weather": weather_get,
            "text": text_process,
            "json": json_process,
            "url": url_process,
            "password": pwd_process,
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

        # JSON formatter triggers: validate:, format:, or minify:
        if low.startswith("validate:") or low.startswith("format:") or low.startswith("minify:"):
            return self.tools["json"](q)

        # URL handler triggers: encode:, decode:, or info:
        if low.startswith("encode:") or low.startswith("decode:") or low.startswith("info:"):
            return self.tools["url"](q)

        # Password generator triggers: generate:, strength:, or random:
        if low.startswith("generate:") or low.startswith("strength:") or low.startswith("random:"):
            return self.tools["password"](q)

        return "I can answer six kinds of requests:\n  'calc:<expression>' (calculator)\n  'weather:<city>' (weather)\n  'wordcount/charcount/reverse:<text>' (text tools)\n  'validate/format/minify:<json>' (JSON tools)\n  'encode/decode/info:<url>' (URL tools)\n  'generate/strength/random:<input>' (password tools)"


if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.handle("calc: 2+2*3"))
