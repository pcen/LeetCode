var maxSubArray = (nums) => {
  if (!nums || nums.length == 0)
    return 0;
  let maxVal = current = nums[0];
  for (i = 1; i < nums.length; i++) {
    current = Math.max(current, 0) + nums[i];
    maxVal = Math.max(current, maxVal);
  }
  return maxVal;
}
