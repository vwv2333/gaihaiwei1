package cn

/**
  * Created by 盖海炜 on 2018/7/20.
  */
object ghw {
  def main(args: Array[String]) {
    var a=List(40,39,40,39,40,39,40)
    var b=List(0,1,2,3,4,5,6)
    for (i<-b){
      if (i==2){
        println("周三温度为"+a(2))
      }
      else {
        println(a(i))
      }
    }
  }


}



import scala.collection.mutable.ListBuffer

/**
  *
  */
/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */


object ZSpark{

  def main(args: Array[String]) {
    import org.json.JSONObject//导入str转json工具包
    import org.apache. spark.SparkConf//
    import org.apache.spark.SparkContext
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory", "2147480000");
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("全国招生人数.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{//line str===>List line  抚平1
      val  json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        //        jsonlist.getJSONObject(0)
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))

  }
}
object ZSparkTest{
  def main(args: Array[String]) {
    println("aaa@qq.com".endsWith("qq.com"))
    println("status\":1}")
    //    new JsonObject
    //    import json    将字符串转换为json（字典）
    import org.json.JSONObject
    val json = new JSONObject("{\"data\":{\"city_name\":\"\\u6e56\\u5357\"},\"info\":\"\",\"status\":0}")
    println(json.getInt("status"))
    println(json.getJSONObject("data"))
    val list = List[Int](1,1,1)//大小不变的固定列表
    //    list(2) = 3
    val list2 = ListBuffer[Int]()
    list2.append(3)
    list2.append(4)
    println(list2)
  }
}






/**import scala.collection.mutable.ListBuffer
  * Created by Me on 2018/7/24.
  */
object zhaosheng {
  def main(args: Array[String]): Unit = {
    import org.json.JSONObject
    //导入Str转为json的工具包
    import org.apache.spark.SparkContext
    import org.apache.spark.SparkConf
    //sparkcontext的配置，名字叫做cala，运行在本地
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf)
    //使用spark读取文本文件
    sc.textFile("E:\\专业\\大数据\\广西招生人数1")
      .filter(line => line.endsWith("status\":1}")&&line.startsWith("{"))
      .flatMap(line => {
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for (i <- 0 to jsonlist.length() - 1) {
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))
  }
}




import scala.collection.mutable.ListBuffer

/**
  * Created by Me on 2018/7/24.
  */
object zhaosheng1 {
  def main(args: Array[String]): Unit = {
    import org.json.JSONObject
    //导入Str转为json的工具包
    import org.apache.spark.SparkContext
    import org.apache.spark.SparkConf
    //sparkcontext的配置，名字叫做cala，运行在本地
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf)
    //使用spark读取文本文件
    sc.textFile("E:\\专业\\大数据\\广西理科招生人数.txt")
      .filter(line => line.endsWith("status\":1}"))
      .flatMap(line => {
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for (i <- 0 to jsonlist.length() - 1) {
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println("'"+line._1+"',"))
  }
}