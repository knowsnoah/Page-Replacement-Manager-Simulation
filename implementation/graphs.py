#this file generates the graphs for the average page faults for each algorithm based on the testing data generated in main.py
import matplotlib.pyplot as plt

frame_sizes = [3, 4, 5, 6]

fifo_avg = [19.14, 16.66, 13.56, 11.10]  # replace with your FIFO averages
lru_avg = [19.36, 16.36, 13.44, 11.10]   # replace with your LRU averages
opt_avg = [14.34, 11.52, 9.76, 8.66]   # replace with your OPT averages


def plot_algorithm(frame_sizes, averages, algorithm_name):
    plt.figure()
    plt.plot(frame_sizes, averages, marker="o")
    plt.title(f"{algorithm_name}: Average Page Faults vs Page Frame Size")
    plt.xlabel("Page Frame Size")
    plt.ylabel("Average Number of Page Faults")
    plt.xticks(frame_sizes)
    plt.grid(True)
    plt.savefig(f"{algorithm_name}_performance.png")
    plt.show()


def plot_all_algorithms(frame_sizes, fifo_avg, lru_avg, opt_avg):
    plt.figure()
    plt.plot(frame_sizes, fifo_avg, marker="o", label="FIFO")
    plt.plot(frame_sizes, lru_avg, marker="o", label="LRU")
    plt.plot(frame_sizes, opt_avg, marker="o", label="OPT")

    plt.title("Average Page Faults vs Page Frame Size")
    plt.xlabel("Page Frame Size")
    plt.ylabel("Average Number of Page Faults")
    plt.xticks(frame_sizes)
    plt.grid(True)
    plt.legend()
    plt.savefig("All_Algorithms_Performance.png")
    plt.show()


plot_algorithm(frame_sizes, fifo_avg, "FIFO")
plot_algorithm(frame_sizes, lru_avg, "LRU")
plot_algorithm(frame_sizes, opt_avg, "OPT")
plot_all_algorithms(frame_sizes, fifo_avg, lru_avg, opt_avg)