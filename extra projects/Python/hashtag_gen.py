print("Hello, this code generates hashtags!")
def generate_hashtag(s):
    if s=="":
        return ""
    else:
        a=s
        s=s.strip()
        s=s.split(" ")
        cap=[word.capitalize() for word in s]
        new_arr="#"
        for i in range(len(cap)):
            new_arr+=cap[i]
        return "Hashtag for {} is \n{}".format(a, new_arr)
print(generate_hashtag(s=input("Enter text: ")))