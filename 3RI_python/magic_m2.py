#input_nums = []
    #input_nums.extend([int(i) for i in input().split()])
#input_nums.extend([int(i) for i in input().split()])
#input_nums.extend([int(i) for i in input().split()])
#input_nums[0], input_nums[1], input_nums[2] = [int(i) for i in input().split()]
#input_nums[3], input_nums[4], input_nums[5] = [int(i) for i in input().split()]
#input_nums[6], input_nums[7], input_nums[8] = [int(i) for i in input().split()]
#print(input_nums)

input_nums=[4,1,8,7,4,3,2,5,4]


pos = []
pos.append([8,1,6,3,5,7,4,9,2])
pos.append([6,1,8,7,5,3,2,9,4])
pos.append([4,9,2,3,5,7,8,1,6])
pos.append([2,9,4,7,5,3,6,1,8])
pos.append([8,3,4,1,5,9,6,7,2])
pos.append([4,3,8,9,5,1,2,7,6])
pos.append([6,7,2,1,5,9,8,3,4])
pos.append([2,7,6,9,5,1,4,3,8])

#print(pos)

mindiff = 10000

for arr in pos:
    diff = 0
    for i in range(9):
        diff += abs(arr[i] - input_nums[i])
    if (diff < mindiff):
        mindiff = diff
        
print(mindiff)