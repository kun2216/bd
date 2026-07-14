Step 1: Download Apache Pig
wget https://archive.apache.org/dist/pig/pig-0.17.0/pig-0.17.0.tar.gz
Step 2: Extract Apache Pig
tar -xvzf pig-0.17.0.tar.gz
mv pig-0.17.0 pig
Step 3: Set Environment Variables

Open .bashrc:

nano ~/.bashrc

Add:

export PIG_HOME=~/pig
export PATH=$PATH:$PIG_HOME/bin

Apply the changes:

source ~/.bashrc
Step 4: Create Input File
nano input.txt

Add:

big data is big
data is powerful
big data is useful
Step 5: Create Pig Script
nano wordcount.pig

Add:

-- Load the data
data = LOAD 'input.txt'
       USING TextLoader()
       AS (line:chararray);

-- Tokenize lines into words
words = FOREACH data
        GENERATE FLATTEN(TOKENIZE(line)) AS word;

-- Group words
grouped = GROUP words BY word;

-- Count occurrences
wordcount = FOREACH grouped
            GENERATE group AS word, COUNT(words) AS count;

-- Display result
DUMP wordcount;
Step 6: Run the Pig Script

Run Pig in local mode:

pig -x local wordcount.pig
