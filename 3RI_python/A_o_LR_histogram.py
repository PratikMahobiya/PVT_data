def max_area_histogram(hist):

    Stack = []
    max_area = 0
    index = 0
    while index < len(hist):


        if (not Stack) or (hist[Stack[-1]] <= hist[index]):
            Stack.append(index)
            index += 1

        else:
            top_of_Stack = Stack.pop()

            area = (hist[top_of_Stack] * ((index - Stack[-1] - 1) if Stack else index))
            max_area = max(max_area, area)

    while Stack:
  
        top_of_Stack = Stack.pop()

        area = (hist[top_of_Stack] * ((index - Stack[-1] - 1) if Stack else index))
        max_area = max(max_area, area)

    return max_area

def main():

    hist = []
    num = int(input("Enter the length of list : "))
    for i in range(num):
        hist.append(int(input("Enter Element {} :=> ".format(i+1))))
    print("Maximum area is: ",max_area_histogram(hist))

if __name__ == "__main__":
    main()