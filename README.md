# Path Reducer

The Path Reducer is a Python package that simplifies a list of directions by removing opposite directions that cancel each other out.

## Installation

You can install the Path Reducer package using pip:

```
pip install path-reducer
```

## Usage

```python
from path_reducer import PathReducer

# Create a PathReducer instance
path_reducer = PathReducer()

# Example usage
directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
optimized_directions = path_reducer.reduce_path(directions)
print(optimized_directions)  # Output: ["WEST"]
```

## Local Setup

To set up the project locally using Poetry, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your-username/path-reducer.git
    ```

2. Navigate to the project directory:

    ```
    cd path-reducer
    ```

3. Install Poetry (if you haven't already):

    ```
    pip install poetry
    ```

4. Use Poetry to install the project's dependencies:

    ```
    poetry install
    ```

5. Activate the Poetry virtual environment:

    ```
    poetry shell
    ```

6. Now you can use the Path Reducer package in your local environment.
