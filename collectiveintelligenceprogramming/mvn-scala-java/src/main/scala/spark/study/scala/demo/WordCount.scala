package spark.study.scala.demo

import org.apache.spark.{SparkConf, SparkContext}

object WordCount {

  def main(args: Array[String]){
    val inputFile = "hdfs://localhost:9000/user/pan/study/test/data/wd/data"
//    val outputFile = args(0)
    val conf = new SparkConf().setAppName("scala-wordcount").setMaster("local")
    val sc = new SparkContext(conf)
    val input = sc.textFile(inputFile)
    val words = input.flatMap(line=>line.split(" "))
    val counts = words.map(word=>(word, 1)).reduceByKey{case(x,y) => x+y}
    counts.saveAsTextFile("hdfs://localhost:9000/user/pan/study/spark/output/test/"+System.currentTimeMillis())
  }
}
