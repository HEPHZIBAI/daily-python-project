'''

Project Brief
Today we explore a trending Python library that is a strong competitor to the popular pandas library. And it is better in many ways, including being more intuitive and faster. This is the polars library.

Your task is to process this CSV file using polars and produce the following statistics:

Print out the first five rows of the CSV


┌──────────────┬─────────────┬──────────────┬─────────────┬─────────┐
│ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species │
│ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---     │
│ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str     │
╞══════════════╪═════════════╪══════════════╪═════════════╪═════════╡
│ 5.1          ┆ 3.5         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ 4.9          ┆ 3.0         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ 4.7          ┆ 3.2         ┆ 1.3          ┆ 0.2         ┆ setosa  │
│ 4.6          ┆ 3.1         ┆ 1.5          ┆ 0.2         ┆ setosa  │
│ 5.0          ┆ 3.6         ┆ 1.4          ┆ 0.2         ┆ setosa  │
└──────────────┴─────────────┴──────────────┴─────────────┴─────────┘
Print general summary statistics using the describe() method:

┌────────────┬──────────────┬─────────────┬──────────────┬─────────────┬───────────┐
│ statistic  ┆ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species   │
│ ---        ┆ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---       │
│ str        ┆ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str       │
╞════════════╪══════════════╪═════════════╪══════════════╪═════════════╪═══════════╡
│ count      ┆ 150.0        ┆ 150.0       ┆ 150.0        ┆ 150.0       ┆ 150       │
│ null_count ┆ 0.0          ┆ 0.0         ┆ 0.0          ┆ 0.0         ┆ 0         │
│ mean       ┆ 5.843333     ┆ 3.057333    ┆ 3.758        ┆ 1.199333    ┆ null      │
│ std        ┆ 0.828066     ┆ 0.435866    ┆ 1.765298     ┆ 0.762238    ┆ null      │
│ min        ┆ 4.3          ┆ 2.0         ┆ 1.0          ┆ 0.1         ┆ setosa    │
│ 25%        ┆ 5.1          ┆ 2.8         ┆ 1.6          ┆ 0.3         ┆ null      │
│ 50%        ┆ 5.8          ┆ 3.0         ┆ 4.4          ┆ 1.3         ┆ null      │
│ 75%        ┆ 6.4          ┆ 3.3         ┆ 5.1          ┆ 1.8         ┆ null      │
│ max        ┆ 7.9          ┆ 4.4         ┆ 6.9          ┆ 2.5         ┆ virginica │
└────────────┴──────────────┴─────────────┴──────────────┴─────────────┴───────────┘
Filter the dataset for a specific species (i.e., setosa)


┌──────────────┬─────────────┬──────────────┬─────────────┬─────────┐
│ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species │
│ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---     │
│ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str     │
╞══════════════╪═════════════╪══════════════╪═════════════╪═════════╡
│ 5.1          ┆ 3.5         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ 4.9          ┆ 3.0         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ 4.7          ┆ 3.2         ┆ 1.3          ┆ 0.2         ┆ setosa  │
│ 4.6          ┆ 3.1         ┆ 1.5          ┆ 0.2         ┆ setosa  │
│ 5.0          ┆ 3.6         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ …            ┆ …           ┆ …            ┆ …           ┆ …       │
│ 4.8          ┆ 3.0         ┆ 1.4          ┆ 0.3         ┆ setosa  │
│ 5.1          ┆ 3.8         ┆ 1.6          ┆ 0.2         ┆ setosa  │
│ 4.6          ┆ 3.2         ┆ 1.4          ┆ 0.2         ┆ setosa  │
│ 5.3          ┆ 3.7         ┆ 1.5          ┆ 0.2         ┆ setosa  │
│ 5.0          ┆ 3.3         ┆ 1.4          ┆ 0.2         ┆ setosa  │
└──────────────┴─────────────┴──────────────┴─────────────┴─────────┘

Environment Setup Instructions

'''