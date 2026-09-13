```mermaid
flowchart TD
    A["main.py"] --> B["main"]
    B --> C["add_numbers"]
    B --> D["multiply_numbers"]
    C --> E["lib.py"]
    D --> E
    