# 寄托天下留学论坛爬虫与可视化分析
## （一）雅思成绩  
该项目利用深度优先算法爬取了寄托家园留学论坛网站（http://bbs.gter.net/） 英国留学板块中申请英国各校的同学的雅思成绩（总分与四个单项），利用pandas进行统计分析并利用matplotlib绘制直方图体现各项成绩分布，分析中国考生的雅思优劣势项目。
该项目共包含2个Python文件：（1）IELTS.py（爬取）（2）ieltsstatistics.py(统计+绘图)与1个csv文件：IELTS.csv(存储爬取结果)  
![image](https://github.com/Karenlyw/Website-Crawler-/blob/master/IELTS/IELTSoverall.png)  
![image](https://github.com/Karenlyw/Website-Crawler-/blob/master/IELTS/IELTS%EF%BC%88Reading%20and%20Listening%EF%BC%89.png)  
![image](https://github.com/Karenlyw/Website-Crawler-/blob/master/IELTS/IELTS%EF%BC%88Speaking%20and%20Writing%EF%BC%89.png)  
## （二）学校offer  
该项目利用深度优先算法爬取了寄托家园留学论坛网站计算机专业申请板块中同学们收到的学校offer，利用pandas进行求和统计并利用matplotlib绘制饼图体现同学申请学校并获得offer的情况。该项目包含2个Python文件：（1）appliedschool.py（爬取）（2）schoolstatistics.py(统计+绘图)与2个csv文件：（1）cs application.csv(存储爬取结果)（2）cs application count.csv(存储统计结果)  
![image](https://github.com/Karenlyw/Website-Crawler-/blob/master/School/school%20statistics.png)
