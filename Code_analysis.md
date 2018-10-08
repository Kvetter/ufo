# Code Analysis

By Kasper Vetter and Phillip Brink

Project used for exercises: https://github.com/CPHB-KEPP/LSD

## Exercise 1

We have chosen to look for the following 10 checks

1. System.Out.Println()

  This is a common thing for a developer to do which working on the project, but it is unesseary for the system to do System.Out.Println's
  instead it should be replaced with a log.
  
2. Unused imports

3. Unused variables

  There is no need for unused code.
  
4. Long Comments

  We want to keep our code clean, nice and simple. Therefore we want to reduce the needs for complex comments.
  
5. Visibility Modifier

  We want to look for all public variables to see if we can make them private or protected.
  
6. Method Name

  We want to make sure that our methodes follows the convention we have decleard for our project.
  
7. One Statement Per Line

  We want to make sure our code is easy readable for everyone.
  
8. Outer Type Filename

  It makes sense to only have one class per file. We want to make sure that the class name and filename is the same.
  
9. Empty Catch Block

  We want to handle exceptions properly and log them.
  
10. For Loop Can Be Foreach

  To ensure that we loop through all elements, we want to use the foreach loop instead of a for loop.
  
 ### Coding Rules 
 ![Coding Rules](https://github.com/Kvetter/ufo-linq/blob/master/img/Coding_Rules.png)
 ### Analysis Resault
 ![Analysis Resault](https://github.com/Kvetter/ufo-linq/blob/master/img/Analysis_Resault.png)
 ### Analysis Report
![Analysis Report](https://github.com/Kvetter/ufo-linq/blob/master/img/PMD_Report.png)

## Exercise 2

We could not find any where neither in the plugin for Intellij or through the profiler in VisualVM to see a bottleneck.
What we found were how to see the memory usage and keep track of the performance.

### Performance Overview
![Analysis Report](https://github.com/Kvetter/ufo-linq/blob/master/img/Performence_Overview.png)

### Memory usages Overview
![Analysis Report](https://github.com/Kvetter/ufo-linq/blob/master/img/Memory_Overview.png)

We have used a profiler called VisualVM, what we can see on Performance Overview is how much CPU, threads and memory are being used.
Everything we see is live so as long as the program is running, we will gather data. On Memory usage we have some options, here we also see live how much memory the program is using, but can perform a garbage clean to see how much unecessary memory is being used. 
