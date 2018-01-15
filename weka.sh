#! /bin/bash

#Update Supercomputer JDK to be compatible with Weka's .jar file
module load jdk/1.8.0-121

#Add the weka Jar to class path environment variable
#(Lets java know where to look for all of weka classes)
echo CLASSPATH=/fslgroup/fslg_genome/pep_seq/weka-3-8-2/weka.jar >> ~/.bash_profile

#Increase max heap size to 1 gigabyte so we don't get Out of Memory Errors
echo _JAVA_OPTIONS="-Xmx1024x" >> ~/.bash_profile


