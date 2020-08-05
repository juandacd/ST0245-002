def Suma_grupo(start, nums, target):
    if (target == 0):
        return True
    if (start == len(nums)):
        return False
    return Suma_grupo(start+1, nums, target-nums[start]) or Suma_grupo(start+1, nums, target)    
    
print(Suma_grupo(0,[5, 1, 3],6))
