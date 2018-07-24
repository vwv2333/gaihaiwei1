/**
  * Created by 盖海炜 on 2018/7/20.
  */

/*练习题1
1.定义一个天气温度列表，写出里面每一天的温度
2.打印一周的天气，天气里面的周三打印例外，周三+温度
* */
object GhwScala3{
  def main(args: Array[String]){
    val a=List(38,39,40,38,39,39,36)
    val b=List(0,1,2,3,4,5,6)
    for (i <- b)
      if (i==2)
        println("周三的温度为："+a(2))
      else
        println(a(i))
  }
}














