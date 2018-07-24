import scala.collection.mutable.ListBuffer

/**
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
    sc.textFile("F:\\大数据实训\\广西理科招生人数.txt")
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
