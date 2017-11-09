# Logs Analysis Project

`LogsAnalysis.py` is a reporting tool for a news site that uses a PostgreSql database. The program runs in the terminal.

The program provides reports for e queries:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

## Setup
### Install the VM and download the sql file
* The tools (Vagrant)[https://www.vagrantup.com/] and (VirtualBox)[https://www.virtualbox.org/wiki/Download_Old_Builds_5_1] are used to install and manage the VM.
* The VM configuration files can be downloaded forked and cloned from (Udacity's Github)[https://github.com/udacity/fullstack-nanodegree-vm].
* Download the [sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file and find `newsdata.sql`. Put it into the vagrant directory.
* Launch the virtual machine with command `vagrant up`, (*This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.*) then log into it with command `vagrant ssh`. This completes the setup of the Linux VM.
* Connect the newsdata database using `psql -d news`

## The Database
* The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

## Usage
 From the vagrant directory inside the virtual machine, run `python3 LogsAnalysis.py`.

Look at `LogsAnalysis_Output.txt` to see an example of the program's output.
