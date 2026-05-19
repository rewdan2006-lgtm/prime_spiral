```markdown
# Ulam Spiral (Prime Number Distribution)

This project generates and visualizes the **Ulam Spiral** (also known as the Prime Spiral). The Ulam Spiral is a graphical depiction of the distribution of prime numbers, constructed by writing the positive integers in a square spiral and specially marking the prime numbers. 

When scaled up, distinct diagonal, horizontal, and vertical lines emerge, revealing fascinating patterns in the distribution of primes.

## Features

- **Prime Checker:** Efficiently determines if a number is prime using the trial division method up to $\sqrt{n}$.
- **Spiral Coordinate Generator:** Generates 2D Cartesian coordinates in a clockwise, expanding square spiral pattern.
- **Data Visualization:** Uses `matplotlib` to render a minimalist, dark-themed scatter plot of the prime distributions.

## Preview of the Spiral Algorithm

The spiral starts at the origin `(0, 0)` for the number 1 and expands outwards:

1. `1 -> (0, 0)`
2. `2 -> (1, 0)`
3. `3 -> (1, 1)`
4. `4 -> (0, 1)`
5. `5 -> (-1, 1)`

## Getting Started

### Prerequisites

Make sure you have Python 3 installed on your system. 

### Installation

1. Clone or download this repository to your local machine.
2. Open your terminal or VS Code terminal and navigate to the project folder.
3. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt

```

### Running the Script

Execute the Python file to generate the plot:

```bash
python main.py

```

## Customization

You can increase or decrease the density of the spiral by changing the argument passed to `generate_spiral()` in the script:

```python
# Change 1200 to a higher number (e.g., 10000) for a denser, more detailed pattern
coords = generate_spiral(1200)

```

## License

This project is open-source and free to use.

```

```