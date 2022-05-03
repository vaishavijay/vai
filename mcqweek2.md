{% include navigation.html %}

# Proctored MCQ Week 2

## Quiz Corrections: Quiz 3: 34/50:

Which of the following best explains the ability to solve problems algorithmically? A. Any problem can be solved algorithmically, though some algorithmic solutions may require humans to validate the results. B.Any problem can be solved algorithmically, though some algorithmic solutions must be executed on multiple devices in parallel. C.Any problem can be solved algorithmically, though some algorithmic solutions require a very large amount of data storage to execute. D.here exist some problems that cannot be solved algorithmically using any computer.
- A: D, not A (While some solutions benefit from being validated by a human, not all problems can be solved with an algorithm.)

Two computers are built by different manufacturers. One is running a Web server and the other is running a Web browser. Which of the following best describes the ability of the two computers to communicate with each other across the Internet? A. The computers cannot communicate because different manufacturers use different communication protocols. B. The computers can communicate, but additional hardware is needed to convert data packets from one computer’s protocol to the other computer’s protocol. C. The computers can communicate directly only if the messages consist of text; other formats cannot be interpreted across computers. D. The computers can communicate directly because Internet communication uses standard protocols.
- A: D, not B (The protocols of the Internet, including TCP/IP, allow any computers that run that protocol to send data back and forth to each other. Protocols such as TCP/IP are implemented through software, not hardware, and additional hardware is not required.)

A certain game keeps track of the maximum and minimum scores obtained so far. If num represents the most recent score obtained, which of the following algorithms correctly updates the values of the maximum and the minimum? AIf num is greater than the minimum, set the minimum equal to num. Otherwise, if num is greater than the maximum, set the maximum equal to num. BIf num is less than the minimum, set the minimum equal to num. Otherwise, if num is greater than the maximum, set the maximum equal to num. CIf num is less than the minimum, set the minimum equal to num. Otherwise, if num is less than the maximum, set the maximum equal to num. DIf num is greater than the minimum, set the minimum equal to num. Otherwise, if num is less than the maximum, set the maximum equal to num.
- A: B, not D (The minimum needs to be updated if the new number is less than the minimum, not greater. The second check is also incorrect. The maximum needs to be updated if the new number is greater than the maximum, not less)

In the following procedure, the parameter n is an integer greater than 2.

![image](https://user-images.githubusercontent.com/85912486/166507585-20f5775d-d37f-4d76-ae2e-5d97bd9653cd.png)Which of the following best describes the value returned by the procedure? A The procedure returns nothing because it will not terminate. B The procedure returns the value of 2 * n. C The procedure returns the value of n * n. D The procedure returns the sum of the integers from 1 to n.
- A: D, not C (The procedure does not return the value of n * n. For a procedure to return n * n, it could initialize result to 0 and then repeatedly add n to result a total of n times.)
