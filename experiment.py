import os
import pandas as pd
import matplotlib.pyplot as plt

for umax in ["0_3", "0_6", "0_9"]:
    for algo in ["grub", "pa", "csf", "ffa"]:
        os.system(f"python ./schedsim/scripts/simulate.py tasksets/data_umax{umax} {algo}")

for umax in ["0_3", "0_6", "0_9"]:
    os.system(f"python ./schedsim/scripts/energy-consumption-vs-utilization.py tasksets/data_umax{umax} energy_umax{umax}.csv")

for umax in ["0_3", "0_6", "0_9"]:
    df = pd.read_csv(f"energy_umax{umax}.csv", sep=" ")

    x = df['util']
    grub = df['grub']
    pa = df['pa']
    ffa = df['ffa']
    csf = df['csf']

    # Plot
    plt.plot(x, grub, label='GRUB')
    plt.plot(x, pa, label='GRUB Power Aware')
    plt.plot(x, ffa, label='Frequency First')
    plt.plot(x, csf, label='Core State First')
    plt.xlabel('Total Utilization $U$')
    plt.ylabel('Power Consumption [W]')
    plt.legend()
    plt.title(f"Power Consumption with umax < {umax.replace("_", ".")}")
    plt.grid(True)
    plt.savefig(f"plot_energy_umax{umax}.png")
    plt.close()
