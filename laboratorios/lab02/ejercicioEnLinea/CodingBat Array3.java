//Ejercicios en línea - CodingBat Array3

//1.maxSpan
public int maxSpan(int[] nums) 
{
  if(nums.length == 0){return 0;} 
    int maxSpan = 1; 
    int span = 0 ;
    for(int i = 0; i < nums.length; i++)
    { 
      for(int j = nums.length - 1; j >= 0; j--)
      { 
        if(nums[j] == nums[i])
        { 
          span = j - i + 1; 
          if(span > maxSpan){maxSpan = span;}
        }
      }
    }
  return maxSpan; //C11
}

//2. fix34
public int[] fix34(int[] nums) 
{
  int aux = 0; //C1
  for(int i = 0; i < nums.length; i++)
  { 
    if(nums[i] == 3)
    { 
      aux = nums[i+1]; //C4*r
      nums[i+1] = 4; //C5*r
      for(int j = i + 2; j < nums.length; j++){if(nums[j] == 4){nums[j] = aux;}}
    }
  }
  return nums; //C9
}

//3.canBalance
public boolean canBalance(int[] nums) 
{
  int acum1 = 0; 
  int acum2 = 0; 
  for(int i = 0; i < nums.length; i++)
  { //C3*m
    acum1 += nums[i]; 
    for(int j = i+1; j < nums.length; j++){acum2 += nums[j]; //C6*m*(m-1)}
    if(acum1 == acum2){return true; //C8}
    acum2 = 0; 
  }
  return false; 
}

//4.linaerIn
public boolean linearIn(int[] outer, int[] inner) {
  int count = 0; //C1
  for(int i = 0; i < inner.length; i++)
  { 
    for(int j = 0; j < outer.length; j++)
    { 
      if(inner[i] == outer[j])
      { 
        count++; 
        break; 
      }
    }
  }
  return count == inner.length; //C7
}

//5.seriesUp
public int[] seriesUp(int n) 
{
  int[] ArregloSerie = new int[n*(n+1)/2];
	int p = 0;
	for(int k = 1; k <= n; k++)
	{
		for(int c = 1; c <= k; c++, p++){ArregloSerie[p] = c;}
	}
	return ArregloSerie;
}
