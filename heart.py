import scipy
import matplotlib.pyplot as plt


def plot_heart():
    fig = plt.figure()

    x = scipy.linspace(-2, 2, 1000)
    y1 = scipy.sqrt(1 - (abs(x) - 1) ** 2)
    y2 = -3 * scipy.sqrt(1 - (abs(x) / 2) ** 0.5)

    plt.fill_between(x, y1, color='yellow')
    plt.fill_between(x, y2, color='yellow')
    plt.xlim([-2.5, 2.5])
    plt.text(
        0,
        -0.4,
        'BVB',
        fontsize=40,
        fontweight='bold',
        color='black',
        horizontalalignment='center'
    )

    return fig


if __name__ == '__main__':
    heart_fig = plot_heart()
    heart_fig.show()
