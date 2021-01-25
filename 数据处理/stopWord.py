from pyhanlp import *

# 使用停用词的简单例子

text = "小区居民有的反对喂养流浪猫"

CRFnewSegment = HanLP.newSegment("crf")

term_list = CRFnewSegment.seg(text)

# BasicTokenizer = SafeJClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")

# term_list = BasicTokenizer.segment(text)

CoreStopWordDictionary = JClass("com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary")

CoreStopWordDictionary.apply(term_list)

HanLP.Config.ShowTermNature = False

print(term_list)

print([i.word for i in term_list])

# 停用词

# 在import pyhanlp之前编译自己的Java class，并放入pyhanlp/static中

import os

from pyhanlp.static import STATIC_ROOT, HANLP_JAR_PATH

java_code_path = os.path.join(STATIC_ROOT, 'MyFilter.java')

with open(java_code_path, 'w') as out:
    java_code = """
            import com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary;
            
            import com.hankcs.hanlp.dictionary.stopword.Filter;
            
            import com.hankcs.hanlp.seg.common.Term;
            
            public class MyFilter implements Filter{
            
                public boolean shouldInclude(Term term){
                    if (term.nature.startsWith('m')) return true; // 数词保留
                    return !CoreStopWordDictionary.contains(term.word); // 停用词过滤
                }
            }
        """
    out.write(java_code)

os.system('javac -cp {} {} -d {}'.format(HANLP_JAR_PATH, java_code_path, STATIC_ROOT))

# 编译结束才可以启动hanlp

CoreStopWordDictionary = JClass("com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary")

Filter = JClass("com.hankcs.hanlp.dictionary.stopword.Filter")

Term = JClass("com.hankcs.hanlp.seg.common.Term")

BasicTokenizer = JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")

NotionalTokenizer = JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")

text = "小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝"

# 可以动态修改停用词词典

CoreStopWordDictionary.add("居民")

print(NotionalTokenizer.segment(text))

CoreStopWordDictionary.remove("居民")

print(NotionalTokenizer.segment(text))

# 可以对任意分词器的结果执行过滤

term_list = BasicTokenizer.segment(text)

print(term_list)

CoreStopWordDictionary.apply(term_list)

print(term_list)

# 还可以自定义过滤逻辑

MyFilter = JClass('MyFilter')

CoreStopWordDictionary.FILTER = MyFilter()

print(NotionalTokenizer.segment("数字123的保留"))  # “的”位于stopwords.txt所以被过滤，数字得到保留

# 来源 https://www.sohu.com/a/275797117_100223767
