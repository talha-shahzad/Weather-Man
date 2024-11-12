

# Weather Data Analyzer

## Project Overview

This project reads, stores, and analyzes temperature data from multiple CSV files in different folders. By leveraging Python generators, it handles large datasets efficiently and performs statistical calculations like maximum, minimum, and average temperature as well as humidity levels. It allows users to filter data based on year, month, and specific locations, outputting both text-based analysis and simple visualizations.

## Features

- **Efficient Data Loading**: Uses Python generators to read CSV files, conserving memory for large datasets.
- **Flexible Filtering**: Supports filtering by year, month, and location.
- **Statistical Analysis**: Computes max, min, and average temperatures and maximum humidity based on the given filters.
- **Graphical Visualization**: Simple ASCII graph displays temperature variations throughout the month.

## Folder Structure

Data should be structured as follows:

```
data/
├── location1/
│   ├── 2020.csv
│   ├── 2021.csv
├── location2/
│   ├── 2020.csv
│   ├── 2021.csv
```

Each CSV file should contain columns such as `Date`, `Max TemperatureC`, `Min TemperatureC`, and `Max Humidity`.

## Usage

### 1. Running the Analyzer

Run the script with date and folder path arguments to analyze specific periods or locations. Example:

```bash
python main.py 2021/6 data/location1
```

This command reads data for June 2021 from the folder `data/location1`.

### 2. Key Functions and Classes

- **`Year_Data`**: Stores max temperature, min temperature, and max humidity, along with dates.
- **`Graph_Data`**: Stores lists of max and min temperatures for graphical output.
- **`read_file` and `read_file_month`**: Generator functions to yield filenames matching the specified year or year/month.
- **`populate_data`**: Updates max, min, and humidity data in `Year_Data`.
- **`print_month_data`**: Outputs average statistics for the month.
- **`FileExplorer`**: Opens files, processes rows, and updates relevant data structures.

### Example API Usage

```python
from weather_analyzer import Year_Data, read_file, FileExplorer

year_data = Year_Data()
file_generator = read_file("2021", "data/location1")
for filename in file_generator:
    FileExplorer(filename, year_data, 1)
year_data.display()
```

## Data Analysis

The program analyzes the following:

- **Highest and Lowest Temperatures**: Displays dates and values for max and min temperatures.
- **Humidity Levels**: Shows the day with the maximum humidity level.
- **Monthly Average**: Calculates and displays the average temperature for a specific month, if provided.

## Output Example

```
Highest: 35C on June 15
Lowest: 10C on June 2
Humidity: 85% on June 20

June 2021:
01 ++++++++++++++++++++++++++++ 29C
01 ++++++++++ 10C
02 ++++++++++++++++++++++++++++ 30C
02 ++++++++++ 11C
...
```
