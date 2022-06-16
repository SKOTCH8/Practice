import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas as pd


fign = 1

for item in ['s1_high_resistance_bike.csv', 's1_low_resistance_bike.csv', 's1_walk.csv',
             's2_high_resistance_bike.csv', 's2_low_resistance_bike.csv', 's2_walk.csv',
             's3_high_resistance_bike.csv', 's3_low_resistance_bike.csv', 's3_walk.csv', 's3_run.csv',
             's4_run.csv',
             's5_low_resistance_bike.csv', 's5_run.csv',
             's6_low_resistance_bike.csv', 's6_walk.csv', 's6_run.csv',
             's8_walk.csv', 's8_run.csv',
             's9_walk.csv']:
    data = pd.read_csv(item, header=0)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, figsize=(8, 8))
    plt.figure(fign)
    fign += 1

    ax1.plot(range(len(data["'Elapsed time'"])), data["'chest_ecg'"])
    ax1.set_title('chest_ecg')
    ax1.set_xlabel('t, s')
    ax1.set_ylabel('mV')
    ax1.grid(True)

    ax2.plot(range(len(data["'Elapsed time'"])), data["'wrist_ppg'"])
    ax2.set_title('wrist_ppg')
    ax2.set_xlabel('t, s')
    ax2.set_ylabel('mV')
    ax2.grid(True)

    ax3.plot(range(len(data["'Elapsed time'"])), data["'wrist_gyro_x'"])
    ax3.plot(range(len(data["'Elapsed time'"])), data["'wrist_gyro_y'"])
    ax3.plot(range(len(data["'Elapsed time'"])), data["'wrist_gyro_z'"])
    ax3.set_title('wrist_gyro')
    ax3.set_xlabel('t, s')
    ax3.set_ylabel('degs^-1')
    ax3.grid(True)

    ax4.plot(range(len(data["'Elapsed time'"])), data["'wrist_low_noise_accelerometer_x'"])
    ax4.plot(range(len(data["'Elapsed time'"])), data["'wrist_low_noise_accelerometer_y'"])
    ax4.plot(range(len(data["'Elapsed time'"])), data["'wrist_low_noise_accelerometer_z'"])
    ax4.set_title('wrist_accelerometer')
    ax4.set_xlabel('t, s')
    ax4.set_ylabel('ms^-2')
    ax4.grid(True)
    plt.tight_layout()

plt.show()
