"""JSON formatter and validator tool."""
import json


def process_json(command: str) -> str:
    """Process JSON commands: 'validate:<json>', 'format:<json>', or 'minify:<json>'.
    
    Examples:
        process_json('validate: {"name": "agent"}') -> 'Valid JSON'
        process_json('format: {"a":1,"b":2}') -> formatted JSON with indentation
        process_json('minify: { "a" : 1 }') -> '{"a":1}'
    """
    try:
        if ":" not in command:
            return "Invalid format. Use 'validate:<json>', 'format:<json>', or 'minify:<json>'"
        
        cmd_type, json_str = command.split(":", 1)
        cmd_type = cmd_type.strip().lower()
        json_str = json_str.strip()
        
        # Parse JSON first to validate
        parsed = json.loads(json_str)
        
        if cmd_type == "validate":
            return "Valid JSON"
        
        elif cmd_type == "format":
            formatted = json.dumps(parsed, indent=2)
            return f"Formatted JSON:\n{formatted}"
        
        elif cmd_type == "minify":
            minified = json.dumps(parsed, separators=(',', ':'))
            return f"Minified JSON: {minified}"
        
        else:
            return f"Unknown command: {cmd_type}. Use 'validate', 'format', or 'minify'."
    
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"
    except Exception as e:
        return f"Error processing JSON: {e}"
