import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def plot_pressure_volume(V_min=0.4, V_max=6, T_list=[1.0,0.95,0.9,0.8], N=1001):
    V_array = np.linspace(V_min, V_max, N)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for T in T_list:
        ax.plot(V_array, P(V_array, T), label="T = {}".format(T))
    ax.legend()
    ax.set_xlabel(r"$\hat{V} = \frac{V}{V_C}$")
    ax.set_ylabel(r"$\hat{P} = \frac{P}{P_C}$")
    ax.set_title("Scaled pressure for multiple temperatures")
    ax.set_ylim([-0.5, 3])
    plt.savefig("../latex/figures/pressure_v.eps")
    plt.show()

def P(V, T):
    return 8*T/(3*V-1) - 3/V**2

def plot_pressure_density(rho_min=0.0, rho_max=2.0, T_list=[1.0,0.95,0.9,0.8],
                          N = 1001):
    rho_array = np.linspace(rho_min, rho_max, N)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for T in T_list:
        ax.plot(rho_array, P(1/rho_array, T), label="T = {}".format(T))
    ax.legend()
    ax.set_xlabel(r"$\hat{\rho} = \frac{\rho}{\rho_C}$")
    ax.set_ylabel(r"$\hat{P} = \frac{P}{P_C}$")
    ax.set_title("Scaled pressure for multiple temperatures")
    plt.savefig("../latex/figures/pressure_d.eps")
    plt.show()

if __name__ == '__main__':
    plot_pressure_volume()
    plot_pressure_density()
