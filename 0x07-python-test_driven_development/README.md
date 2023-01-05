TEST DRIVEN DEVELOPMENT

>>>>>>>>>>Never forget a test

Testing is the process of evaluating a system or its component(s) with the 
intent to find whether it satisfies the specified requirements or not.
There are five steps that are involved while testing an application for functionality:

The determination of the functionality that the intended application is meant to perform.
The creation of test data based on the specifications of the application.
The output based on the test data and the specifications of the application.
The writing of test scenarios and the execution of test cases.
The comparison of actual and expected results based on the executed test cases.



Unit Testing
This type of testing is performed by developers before the setup is handed over to the testing team to formally execute the test cases. Unit testing is performed by the respective developers on the individual units of source code assigned areas. The developers use test data that is different from the test data of the quality assurance team.

The goal of unit testing is to isolate each part of the program and show that individual parts are correct in terms of requirements and functionality.

Limitations of Unit Testing:

Testing cannot catch each and every bug in an application. It is impossible to evaluate every execution path in every software application. The same is the case with unit testing.
There is a limit to the number of scenarios and test data that a developer can use to verify a source code. After having exhausted all the options, there is no choice but to stop unit testing and merge the code segment with other units.



KEY POINTS :

	All test edge cases in the function must start with test.
	You must import unittest or doctest, depends on which one you are using.
	To run the doctest:
		python3 -m doctest module_name -v(optional)

	Same for running unittest

How doctest works:

python searches for text that looks like the python interpreter session and 
display the output to prove that its actually the same.

As a software developer, testing is very crucial in the software development 
phase.
