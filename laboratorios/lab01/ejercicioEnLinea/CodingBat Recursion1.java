Ejercicios en línea - CodingBat

1.bunnyEars
public int bunnyEars(int bunnies) 
{
  if(bunnies == 0){return 0;}
  else{return 2 + bunnyEars(bunnies - 1);}
}


2.Triangle
public int triangle(int rows) 
{
  if(rows==0){return 0;}
  else{return rows + triangle(rows - 1);}
}


3.sumDigits
public int sumDigits(int n) 
{
  if(n==0){return 0;}
  else{return n%10 + sumDigits(n/10);}
}


4.count8
public int count8(int n) 
{
  if(n == 0){return 0;}
  else
  {
    if(n%10 == 8) 
    {
      if((n/10)%10 == 8){return 2 + count8(n/10);}
      else{return 1 + count8(n/10);}
    }
    else{return count8(n/10);}
  }
}


5.array11
public int array11(int[] nums, int index) 
{
  if(index==nums.length)
    return 0;
  else
    if(nums[index]==11)
      return 1 + array11(nums, index+1);
    else 
      return array11(nums,index+1);
}
