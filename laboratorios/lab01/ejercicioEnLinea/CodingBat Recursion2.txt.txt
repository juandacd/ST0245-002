Ejercicios en línea - CodingBat

1.groupSum6
public boolean groupSum6(int start, int[] nums, int target) 
{
  if(start == nums.length){return target == 0;}
  if(nums[start] == 6){return groupSum6(start + 1, nums, target - nums[start]);}
  else{return groupSum6(start + 1, nums, target) || groupSum6(start + 1, nums, target - nums[start]);}
}


2.groupNoAdj
public boolean groupNoAdj(int start, int[] nums, int target) 
{
  if(start >= nums.length){return target ==0;}
  else{return groupNoAdj(start + 1, nums, target) || groupNoAdj(start + 2, nums, target - nums[start]);}
}


3.groupSum5
public boolean groupSum5(int start, int[] nums, int target) 
{
  if(start == nums.length){return target == 0;}
  if(nums[start] % 5 == 0){return groupSum5(start + 1, nums, target - nums[start]);}
  else 
  {
    if (start > 0 && nums[start] == 1 && nums[start - 1] % 5 == 0){return groupSum5(start + 1, nums, target);}
    else {return groupSum5(start + 1, nums, target) || groupSum5(start + 1, nums, target -nums[start]);}
  }
}


4.griupSumClump
public boolean groupSumClump(int start, int[] nums, int target) 
{
  if(start == nums.length) {return target == 0;}
  int suma = 0;
  int i;
  for( i = start; i < nums.length; i++)
  {
    if(nums[start] == nums[i]){suma += nums[start];}
    else{break;}
  }
  return groupSumClump(i, nums, target - suma) || groupSumClump(i, nums, target);
}


5.splitArray
public boolean splitArray(int[] nums)
{return auxSplitArray(nums, 0, 0, 0);}

public boolean auxSplitArray(int nums [], int group1, int group2, int start)
{
  if(start == nums.length) {return group1 == group2;}
  else{return auxSplitArray(nums, group1 + nums[start], group2, start +1) || auxSplitArray(nums, group1, group2 + nums[start], start +1);}
}

