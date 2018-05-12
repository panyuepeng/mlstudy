package spark.study.java.demo;


import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.regex.Pattern;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import scala.Serializable;
import scala.Tuple2;


public class TopK {
    public static final Pattern SPACE = Pattern.compile(" ");

    public static void main(String[] args)throws Exception {
        String inPath = null;

        if (args.length == 1) {
            inPath = args[0];
        } else {
            System.out.println("Usage: <src> [des]");
        }

        SparkConf sparkConf = new SparkConf().setAppName("Word Count");
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
        JavaRDD<String> lines = jsc.textFile(inPath);
        JavaRDD<String> words = lines.flatMap(new FlatMapFunction<String, String>() {
            @Override
            public Iterable<String> call(String s) throws Exception {
                return Arrays.asList(SPACE.split(s));
            }
        });

        JavaPairRDD<String, Integer> pairs = words.mapToPair(new PairFunction<String, String, Integer>() {
            @Override
            public Tuple2<String, Integer> call(String s) throws Exception {
                return new Tuple2<String, Integer>(s, 1);
            }
        });

        JavaPairRDD<String, Integer> counts = pairs.reduceByKey(new Function2<Integer, Integer, Integer>() {
            @Override
            public Integer call(Integer i1 , Integer i2) throws Exception {
                return i1 + i2;
            }
        });

        JavaPairRDD<Integer, String> converted = counts.mapToPair(new PairFunction<Tuple2<String, Integer>, Integer, String>() {
            @Override
            public Tuple2<Integer, String> call(Tuple2<String, Integer> tuple) throws Exception {
                return new Tuple2<Integer, String>(tuple._2(), tuple._1());
            }
        });

        JavaPairRDD<Integer, String> sorted = converted.sortByKey(true, 1);
        List<Tuple2<Integer, String>> topK = sorted.top(5, new Comp());

        for(Tuple2<Integer, String> top: topK) {
            System.out.println(top._2() + ": " + top._1());
        }

        jsc.stop();
    }
}

class Comp implements Comparator<Tuple2<Integer, String>>, Serializable {

    @Override
    public int compare(Tuple2<Integer, String> o1, Tuple2<Integer, String> o2) {
        if(o1._1() < o2._1()) {
            return -1;
        }else if(o1._1() > o2._1()) {
            return 1;
        }else {
            return 0;
        }
    }
}
