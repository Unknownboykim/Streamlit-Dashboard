## Palmer Penguins Explorer

The dashboard is for exploring measurements of real penguins from three islands in Antarctica. The data file lists 344 penguins, and 11 of them are dropped because some measurements are missing, so 333 are used. It covers three species (Adelie, Chinstrap and Gentoo). For each penguin it records the island, bill length and depth, flipper length, body mass and sex.

1. Sidebar filters (left side)

These control everything else on the page:

Species: choose which species to include.
Island: choose which islands to include.
Body mass slider: limit the weight range in grams.

If no penguins match the filters, a warning tells you to widen them.

2. Summary numbers (top row)

Four headline numbers that update as you filter:

How many penguins are shown
Average body mass (g)
Average flipper length (mm)
How many species are shown
3. Three tabs

Charts tab

Scatter plot: you pick any two measurements for the X and Y axes, and each dot is a penguin, coloured by species. This shows how the species form separate groups.
Histogram: shows how one measurement is spread out, for example how many penguins weigh around 4,000 g compared with 5,000 g.
Bar chart: the number of penguins on each island, split by species.

Data tab

A table of the filtered data, with a Download as CSV button.

Predict tab (machine learning bonus)

You set a penguin’s bill, flipper and weight with four sliders.
A model (a “random forest”) guesses the species and says how confident it is, for example “Gentoo (94% confident)”.
4. “About this data” (bottom)

A section you can expand that gives the data source (Palmer Station, Antarctica, collected by Dr. Kristen Gorman, 2007–2009), lists the columns, and says it was built by Ryan with Python, pandas, Plotly and Streamlit.

In one sentence: it’s an interactive dashboard where you filter penguins, compare their body measurements in charts, look at or download the raw data, and have a model guess a penguin’s species from its measurements.

To run it:
streamlit run app.py

## Built with

Python · pandas · Plotly · scikit-learn · Streamlit

## Run it locally

```bash
pip install -r requirements.txt
streamlit run starter_app.py
```

## Data

Palmer Station Antarctica LTER, collected by Dr. Kristen Gorman (2007-2009). Made available through the `palmerpenguins` package (CC0).


## Prediction Model
A random forest classifier is a machine-learning model that sorts things into categories.
It does this by building lots of small “decision trees”, each a short chain of yes/no questions such as “Is the flipper longer than 206 mm? If yes, it’s probably a Gentoo.”
Each tree learns from a slightly different random sample of the data, and then they all vote on the answer.
In this dashboard, the model is trained on all the penguins in the data, using four measurements (bill length, bill depth, flipper length and body mass) to learn the species.
In the Predict tab you describe a penguin with sliders, the model’s 100 trees each guess its species, and the majority wins. The confidence shown is the share of trees that agreed: for example, if 91 of the 100 trees vote Gentoo, it shows “Gentoo (91% confident)”.




