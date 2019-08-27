number = int(input("Enter the Amount of Israeli money you want:"))
s = {1, 2, 5, 10, 20, 50, 100, 200}

#this function finds the biggest number that is smaller than the input number
def find_biggest(s, number):
    result = 0
    for k in s:
        if k > result and k <= number:
            result = k
    return result

result = []

while sum(result) != number:
    current_result=number-sum(result)
    if sum(result) < number:
        result.append(find_biggest(s, current_result))

print("There you go: ")
print(result)

