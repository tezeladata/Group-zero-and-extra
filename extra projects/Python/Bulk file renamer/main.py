import os

# Function to rename multiple files
def main():
    i = 0

    path = "C:/Users/PC/OneDrive/Desktop/coding course/extra projects/Python/Bulk file renamer/Images/"
    for filename in os.listdir(path):
        my_dest = f"goa{i}.jpg"
        my_source = path + filename
        my_dest = path + my_dest

        os.rename(my_source, my_dest)

        i+=1

if __name__ == "__main__":
    main()