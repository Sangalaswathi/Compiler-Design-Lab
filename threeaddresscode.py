class Three:
    def __init__(self, temp, data):
        self.temp = temp
        self.data = data

def process_input_data(input_data):
    s = []
    for line in input_data:
        parts = line.split()
        s.append(Three(parts[0], parts[2:]))

    for i in range(len(s)):
        if s[i].data[0] == "=":
            print("\nLDA\t" + s[i].data[1])
            if len(s[i].data) > 2 and s[i].data[2] == "+":
                print("ADD\t" + s[i].data[3])
            elif len(s[i].data) > 2 and s[i].data[2] == "-":
                print("SUB\t" + s[i].data[3])
            print("STA\t" + s[i].temp)

def main():
    print("Test Case 1")
    input_data_1 = ["t1 = in1 + in2", "t2 = t1 + in3", "out = t2"]
    process_input_data(input_data_1)

    print("\nTest Case 2")
    input_data_2 = ["x = a + b", "y = x - c", "z = y + d"]
    process_input_data(input_data_2)

    print("\nTest Case 3")
    input_data_3 = ["t1 = in1 - in2", "out = t1"]
    process_input_data(input_data_3)

if __name__ == "__main__":
    main()
