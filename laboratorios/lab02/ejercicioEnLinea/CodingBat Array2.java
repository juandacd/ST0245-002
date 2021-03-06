//Ejercicios en línea - CodingBat Array2

//1.lucky13
public boolean lucky13(int[] nums) 
{
  for(int i = 0; i < nums.length; i++)
  {if(nums[i] == 1 || nums[i] == 3) {return false;}}
  return true; 
}


//2.more14
public boolean more14(int[] nums) 
{
  int count1 = 0; 
  int count4 = 0; 
  for(int i = 0; i < nums.length; i++)
  { 
    if(nums[i] == 1) {count1++;}
    if(nums[i] == 4) {count4++;} 
  }
  return count1 > count4; 
}


//3.fizzArray
public int[] fizzArray(int n) 
{
  int [] ans = new int [n]; 
  for(int i = 0; i < n; i++){ans[i] = i;}
  return ans;
}

//4.withoutTen
public int[] withoutTen(int[] nums) 
{
  int a=0;
  for(int q=0; q<nums.length; q++)
  { 
      if(nums[q]==10) {nums[q]=0;}
      else
      {
	nums[a]=nums[q];
	if(a != q) {nums[q]=0;}
	a+=1;
      }
  }
  return nums;  
}


//5.zeroMax
public int[] zeroMax(int[] nums) 
{
  int max = 0;
  for (int i = nums.length-1; i >= 0; i--) 
  {
    if (nums[i] % 2 == 1){max = Math.max(max, nums[i]);}
    if (nums[i] == 0) {nums[i] = max;}
  }
  return nums;
}
