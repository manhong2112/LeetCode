object Solution {
  def findNumbers(nums: Array[Int]): Int = {
    nums.count(_.toString.length % 2 == 0)
  }
}
