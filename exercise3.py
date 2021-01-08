
from os import linesep

if __name__ == "__main__":
    number_of_runs = 0
    total_duration = 0
    while True:
        next_run = input("Enter 10 km run time: ")
        try:
            total_duration += float(next_run)
        except ValueError:
            if number_of_runs != 0:
                average = total_duration/number_of_runs
                print(linesep + f"Average of {average} over {number_of_runs} runs")
            else:
                print("Whatever")
            break
        else:
            number_of_runs += 1
