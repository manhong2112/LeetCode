object Solution {
  def subtractProductAndSum(n: Int): Int = {
    val k = n.toString().map(_.toInt - '0')
    k.foldLeft(1)(_ * _) - k.foldLeft(0)(_ + _)
  }
}
