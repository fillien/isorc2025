# Running ISORC 2025 Experiments

This outlines how to run the experiments and analyze their results.
First, initialize and update the simulator submodule:

```shell
git submodule update --init --recursive
```

Next, build the simulator using CMake and Ninja:

```shell
cmake -S schedsim -B build -G Ninja
cmake --build build
```

Finally, execute the experiment script to run simulations and generate results:

```shell
python experiment.py
```

This script will output CSV files containing power consumption data for two models. These files are located in the `platforms/` directory.  The script also generates a PNG plot corresponding to each CSV file.
