package spark.study.scala.demo

import org.apache.spark.{SparkConf, SparkContext}

object TopK {
  def main(args: Array[String]) {
    if(args.length < 1) {
      System.err.println("Usage: <file>")
      System.exit(1)
    }
    val conf = new SparkConf()
    val sc = new SparkContext(conf)
    //SparkContext 是把代码提交到集群或者本地的通道，我们编写Spark代码，无论是要本地运行还是集群运行都必须有SparkContext的实例
    val line = sc.textFile(args(0))
    //把读取的内容保存给line变量，其实line是一个MappedRDD，Spark的所有操作都是基于RDD的
    //其中的\\s表示 空格,回车,换行等空白符，+号表示一个或多个的意思
    val result = line.flatMap(_.split("\\s+")).map((_, 1)).reduceByKey(_+_)
    val sorted = result.map{case(key,value) => (value,key)}.sortByKey(true,1)
    val topk = sorted.top(args(1).toInt)
    topk.foreach(println)
    sc.stop
  }
}
