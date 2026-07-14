
### Step 1: Install Java

sudo apt install openjdk-17-jdk -y
java -version

### Step 2: Install 

sudo apt install 3.12 3.12-venv 3-pip -y

### Step 3: Create Virtual Environment

3.12 -m venv spark_env
source spark_env/bin/activate

### Step 4: Install PySpark

pip install pyspark

### Step 5: Download Spark

wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz

### Step 6: Extract Spark

tar -xvzf spark-3.5.1-bin-hadoop3.tgz
mv spark-3.5.1-bin-hadoop3 spark

### Step 7: Set Environment Variables

nano ~/.bashrc

Add:
export SPARK_HOME=~/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

Apply changes:
source ~/.bashrc
### Step 8: Start PySpark

source spark_env/bin/activate
pyspark

### Step 9: Create Structured Data


data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),
    ("David", 40)
]

df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

### Step 10: Access and Process Data

df.filter(df.Age > 30).show()
df.select("Name").show()
df.sort("Age").show()

### Step 11: Perform Aggregation

df.groupBy("Age").count().show()
