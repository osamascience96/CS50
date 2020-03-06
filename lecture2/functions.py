def square(x):
    return x * x

def main():
    for i in range(10):
        # {} is the placeholder
        print("{} squared is {}".format(i, square(i)))

# if i am running this file, then run the main function
if __name__ == "__main__":
    main()