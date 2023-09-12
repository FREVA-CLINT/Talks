# The freva future Data API Architecture

## Introduction

The [freva](https://freva-clint.github.io/freva/) Future Data API is an
innovative architecture designed to change the way datasets are registered,
searched for, and generated.
Instead of pre-computing and storing large sets of data, this architecture
allows users to register *future* datasets—data that does not yet exist but
can be generated on-demand. This system is especially useful for calculating
variables that are derived from existing datasets or even creating entirely
new datasets, such as applying recipes for climate model simulations.

Utilizing freva's python API, Apache Solr, and MariaDB, the system efficiently
manages these future datasets through a sophisticated workflow that is both
resource-efficient and highly adaptable.

> ``📝`` The code of the prototype can be found in the `futures` branch of
         the [freva GitHub repository](https://github.com/FREVA-CLINT/freva/tree/futures)

### Terminology: Why Call These "Futures"?

In programming, a "Future" refers to a value that is not yet available but
will be resolved at some point in the future. The concept aligns well with
this architecture for the following reasons:

1. **Deferred Execution**: Just like a future, the actual dataset does not
    exist until demanded.
2. **Resource Optimization**: Computing resources are utilized only when
    there is a need for the dataset.
3. **Reproducibility**: The existence of the notebook as a recipe ensures
    that the data can be recreated, similar to how a future can be resolved
    multiple times.
4. **Dynamic Adaptation**: The ability to generate datasets on-the-fly makes
    the system adaptive and responsive to user needs, much like how futures
    are used for asynchronous operations.

Thus, the term "futures" aptly encapsulates the architecture's essence of
handling data that will be materialized on demand, making it efficient and
forward-looking.


## Architecture Components

1. **User Interface**: Allows users to register and search for datasets.
2. **Python API**: Facilitates user registration and dataset handling.
3. **Apache Solr**: Stores dataset facets and Jupyter Notebook string
    representation.
4. **MariaDB**: Keeps a copy of the Jupyter Notebook content, code hash, and
    data file locations.

### Workflow

1. Users register datasets by submitting Jupyter Notebooks containing the
    data recipe. This can be done either by:

    * Using pre defined templates where the `solr-parameters` and any
      additional variables are passed to create the specific recipe for
      this datasets.
    * Creating a recipe from a *freva plugin* run that has already been
      applied.

2. The Python API reads cells tagged with `solr-parameters` and extracts
    variables as Apache Solr facets making the dataset searchable via apache
    solr (the `freva databrowser`).
3. The string representation of the Jupyter Notebook and the extracted facets
    are stored in Apache Solr.
4. The notebook content, along with a hash representing the notebook code,
    is stored in MariaDB.
5. MariaDB also maintains a table containing a JSON field for the location of
    the data files that the notebook would generate.

### On-Demand Data Generation

1. Users search for datasets using the API.
2. When a dataset is requested for use, the corresponding notebook is
    executed on-demand.
3. The generated data replaces the "future" dataset representation in
    both Apache Solr and MariaDB.

## Use Cases

- **Derived Variables**: The architecture allows for easy computation of
    variables that are derivatives of existing datasets.
- **New Datasets**: It can also generate completely new datasets, such as
    climate model simulations, by applying specific recipes encapsulated
    in Jupyter Notebooks.


## Examples
There are two notebooks outlining the anticipated usage of the proposed
mechanism [FuturesExample.ipynb] demonstrates the usage from python while
[FuturesExample-Bash.ipynb] explains the same scenario for the `freva`
command line interface.
