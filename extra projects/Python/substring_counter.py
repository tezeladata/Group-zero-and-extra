def count_substring(string, sub_string):
    all_var = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            all_var.append(string[i:j])
            
    return all_var.count(sub_string)

if __name__ == '__main__':
    string = input("Enter string here: ").strip()
    sub_string = input("Enter substring here: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)