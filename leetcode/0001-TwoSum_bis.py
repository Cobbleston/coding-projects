#   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#   You may assume that each input would have exactly one solution, and you may not use the same element twice.
#   You can return the answer in any order.
#   
#   Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#   
#   Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]
#   
#   Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
#   
#   Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.
#   
#   Variante Cioni: Fallo con m addendi

def twoSum(nums: list[int], target: int, m: int) -> list[int]:
    # Genero il dizionario per dopo
    val_ind = {}
    for i in range(0, len(nums)):
        val_ind[nums[i]] = i
    # Ordino la lista
    nums.sort()
    # Faccio il test
    # Genero gli indici iniziali per m
    possIndex = []
    for i in range(0, m):
        possIndex.append(i)
    # Verifico che la somma dei tre indici sia più o meno grande
    found = False
    while not found:
        s = 0
        for i in possIndex:
            s += nums[i]
        # Genero distanza da precedente e successivo
        nearIndexDifference = {}
        for ind in possIndex:
            nearIndexDifference[ind] = []
            # Indice analizzato == 0
            if ind == 0:
                # Distanza dal precedente
                nearIndexDifference[ind].append(999)
                # Distanza dal successivo
                if ind+1 not in possIndex:
                    nearIndexDifference[ind].append(abs(nums[ind] - nums[ind+1]))
                else:
                    nearIndexDifference[ind].append(999)
            elif ind == len(nums)-1:
                # Distanza dal precedente
                if ind-1 not in possIndex:
                    nearIndexDifference[ind].append(abs(nums[ind] - nums[ind-1]))
                else:
                    nearIndexDifference[ind].append(999)
                # Distanza dal successivo
                nearIndexDifference[ind].append(999)
            else:
                # Distanza dal precedente
                if ind-1 not in possIndex:
                    nearIndexDifference[ind].append(abs(nums[ind] - nums[ind-1]))
                else:
                    nearIndexDifference[ind].append(999)
                # Distanza dal successivo
                if ind+1 not in possIndex:
                    nearIndexDifference[ind].append(abs(nums[ind] - nums[ind+1]))
                else:
                    nearIndexDifference[ind].append(999)
        #print(nearIndexDifference)
        mini = 999
        indSpost = 0
        if s < target:
            #print("dentro se minore")
            for i in nearIndexDifference.keys():
                if nearIndexDifference[i][1] < mini:
                    mini = nearIndexDifference[i][1]
                    indSpost = i
            nextPossIndex = []
            for i in nearIndexDifference.keys():
                if i == indSpost:
                    nextPossIndex.append(i+1)
                else:
                    nextPossIndex.append(i)
        elif s > target:
            #print("dentro se maggiore")
            for i in nearIndexDifference.keys():
                if nearIndexDifference[i][0] < mini:
                    mini = nearIndexDifference[i][0]
                    indSpost = i
            nextPossIndex = []
            for i in nearIndexDifference.keys():
                if i == indSpost:
                    nextPossIndex.append(i-1)
                else:
                    nextPossIndex.append(i)
        else:
            found = True
        possIndex = nextPossIndex
        #print(nextPossIndex)
        #input()
    # Ritorno usando il dizionario gli indici originali
    return possIndex


a = [2, 7, 8, 22, 1]
t = 25
# Output: [0,1,4]
print(twoSum(a, t, 3))