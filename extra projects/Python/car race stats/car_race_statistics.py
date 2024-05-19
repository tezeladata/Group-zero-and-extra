import time # For proper file names
import matplotlib.pyplot as plt # For visualization

def race_statistics():
    def greeting():
        print("Hello, this is race statistics calculator.")
        print("You can enter multiple elements.")
        print("\nAn example of format is: 01|20|15 - 1 hour, 20 minutes, 15 seconds\n")
        print("After your input, you will get range, average, median and standart deviation for your data\n")

    greeting()

    # User input
    strg = input("Enter your race results: ")

    # Funcs for convertions
    def convert_to_seconds(time):
        return time[0] * 3600 + time[1] * 60 + time[2]

    def convert_to_hms(seconds):
        hours = int(seconds / 3600 // 1)
        minutes = int((seconds - hours * 3600) / 60 // 1)
        seconds = int(seconds - hours * 3600 - minutes * 60)
        
        return f"{hours:02d}|{minutes:02d}|{seconds:02d}"
    

    # Funcs for range, mean, median
    def stat_range(data):
        return convert_to_hms(data[-1] - data[0])

    def stat_mean(data):
        return convert_to_hms(sum(data) / len(data))
        
    def stat_median(data):
        data_length = len(data)
        middle = data_length // 2
        
        if data_length % 2 == 0:
            return convert_to_hms((data[middle - 1] + data[middle]) / 2)
        return convert_to_hms(data[middle])
    
    def stat_deviation(data):
        return convert_to_hms(int((sum([(i - (sum(data) / len(data)))**2 for i in data]) / len([(i - (sum(data) / len(data)))**2 for i in data])) ** 0.5))

    # Main func:
    def main(strg):
        data_list = []
        for runner_time in strg.split(", "):
            times = convert_to_seconds([int(time) for time in runner_time.split("|")])
            data_list.append(times)
        data_list.sort()

        # Plotting histogram
        plt.hist(data_list, bins=10, color='black', edgecolor='black', alpha=0.7)
        plt.xlabel('Race Times (seconds)')
        plt.ylabel('Frequency')
        plt.title('Race Times Histogram')
        plt.grid(True)
        plt.show()
        

        # Final result
        res = f"Range: {stat_range(data_list)} \nAverage: {stat_mean(data_list)} \nMedian: {stat_median(data_list)} \nStandart deviation: {stat_deviation(data_list)}"
        print(f'\n{"".join(["-" for _ in range(len(res))])}')
        print(res)
        print(f'{"".join(["-" for _ in range(len(res))])}\n')

        # Save the result to a file
        filename = f"car_race_statistics_result_{time.strftime('%Y%m%d-%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(f"With input: {strg}\nYour results are:\n\n{res}")

    # If input is correct, main func will be used
    def validate(user_input):
        # To check if minutes or seconds are invalid
        original = user_input
        user_input = [i.split("|") for i in user_input.split(", ")]

        is_valid = True
        for i in user_input:
            for x in i[1:]:
                if int(x) >= 60:
                    is_valid = False
        
        # For short inputs
        is_valid = len(user_input) >= 3
        
        if is_valid:
            main(original)
        else:
            print("Your input did not satisy all requirements")

    validate(strg)

race_statistics()

# Test cases:
# 01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17
# 02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41
# 02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|32|34, 2|17|17