{% include navigation.html %}

# Proctored MCQ Week 2

## Quiz Corrections: Quiz 3: 34/50:

The following procedure is intended to return the value of x times y, where x and y are integers. Multiplication is implemented using repeated additions.![image](https://user-images.githubusercontent.com/85912486/167026146-294ae3f0-280a-40ee-bace-3d275e73cb14.png) For which of the following procedure calls does the procedure NOT return the intended value? Select two answers.
- A: D, not C (For C's values, the procedure repeatedly adds -2 to result five times, resulting in the intended product -10)

The table below shows the time a computer system takes to complete a specified task on the customer data of different-sized companies.![image](https://user-images.githubusercontent.com/85912486/167026298-caec8e47-9388-4e53-990b-8822037e7110.png). Based on the information in the table, which of the following tasks is likely to take the longest amount of time when scaled up for a very large company of approximately 100,000 customers?
- A: D, not C (Look at the values from small to large company in between, not the end column alone)

The transmission control protocol (TCP) and Internet protocol (IP) are used in Internet communication. Which of the following best describes the purpose of these protocols? A. To ensure that communications between devices on the Internet are above a minimum transmission speed. B. To ensure that private data is inaccessible to unauthorized devices on the Internet. C. To establish a common standard for sending messages between devices on the Internet. D. To validate the ownership of encryption keys used in Internet communication
- A: C, not A (TCP/IP are intended to define a standard format for messages sent between devices on the Internet)

Consider the two programs below. ![image](https://user-images.githubusercontent.com/85912486/167026780-83cf33f0-3063-45c2-a240-bcc39e009495.png)![image](https://user-images.githubusercontent.com/85912486/167026791-0f34edf1-e51e-485a-b643-f58c9bc3ebbf.png)Which of the following best compares the values displayed by programs A and B? A. Program A and program B display identical values. B. Program A and program B display the same values in different orders. C. Program A and program B display the same number of values, but the values differ. D. Program A and program B display a different number of values.
- A: C, not D (Both programs display ten values)

Consider the two programs below.

![image](https://user-images.githubusercontent.com/85912486/167027412-373e75f0-d2be-4579-8130-be356081eaac.png)

Which of the following best compares the values displayed by programs A and B? Program A and program B display identical values in the same order. Program A and program B display the same values in different orders. Program A and program B display the same number of values, but the values differ. Program B displays one more value than program A.
- A: C, not D (Both programs display ten values)

An online game collects data about each player’s performance in the game. A program is used to analyze the data to make predictions about how players will perform in a new version of the game. The procedure GetPrediction (idNum) returns a predicted score for the player with ID number idNum. Assume that all predicted scores are positive. The GetPrediction procedure takes approximately 1 minute to return a result. All other operations happen nearly instantaneously. Two versions of the program are shown below. Which of the following best compares the execution times of the two versions of the program?
- A: D, not A (Version I calls GetPrediction once for each element of idList, while version II calls GetPrediction twice for each element of idList (plus one more time at the end). Therefore, version II takes longer than version I)

Consider a game in which a player flips a fair coin three times. If all three coin flips have the same result (either all heads or all tails) the player wins. Otherwise, the player loses. Which of the following code segments best simulates the behavior of the game?The procedure GetPrediction (idNum) returns a predicted score for the player with ID number idNum. Assume that all predicted scores are positive. The GetPrediction procedure takes approximately 1 minute to return a result. All other operations happen nearly instantaneously.
- A: ![Uploading image.png…]( (In this code segment, the variable flip is assigned one of four values: 0, 1, 2, or 3. The player wins approximately two out of every four times (when flip is 0 or 3).)

A certain computer game is played between a human player and a computer-controlled player. Every time the computer-controlled player has a turn, the game runs slowly because the computer evaluates all potential moves and selects the best one. Which of the following best describes the possibility of improving the running speed of the game? A. The game’s running speed can only be improved if the game is played between two human players instead of with the computer-controlled player. B. The game’s running speed might be improved by using a process that finds approximate solutions every time the computer-controlled player has a turn.
A: B, not A (Changing the game from single player to multiplayer does not solve the original problem. It might improve the running speed, but other methods of improving performance exist, such as using a heuristic.)

The following code segment is intended to remove all duplicate elements in the list myList. The procedure does not work as intended.

    j ← LENGTH(myList)
    REPEAT UNTIL(j = 1)
    {
    IF(myList[j] = myList[j - 1])
    {
    REMOVE(myList, j)
    }
    j ← j - 1
    }

For which of the following contents of myList will the procedure NOT produce the intended results? Select two answers.
- A: D, not C (The code segment will iterate over myList from right to left, removing each element that is equal in value to the element immediately preceding it. For this list, the code segment will remove the sixth element (10), the fourth element (20), and the second element (10). This results in the list [10, 20, 10], which still contains duplicates)

The figure below represents a network of physically linked devices labeled A through I. A line between two devices indicates that the devices can communicate directly with each other. Any information sent between two devices that are not directly connected must go through at least one other device. For example, in the network represented below, information can be sent directly between A and B, but information sent between devices A and G must go through other devices.

Which of the following statements is true about the network? A. Information sent from device A to device D can use at most two unique paths. B. Information sent from device A to device I will pass through at most four other devices. C. If devices B and F fail, then device A will not be able to communicate with device G. D. If devices C and F fail, then device D will not be able to communicate with device H.
- A: C, not A (There are many possible paths between devices A and D, including A-B-D, A-C-D, A-C-F-D, and A-B-E-F-D)

A user enters a Web address in a browser, and a request for a file is sent to a Web server. Which of the following best describes how the file is sent to the user? A. The file is broken into packets for transmission. The packets must be reassembled upon receipt. B. The file is broken into packets for transmission. The user’s browser must request each packet in order until all packets are received. C. The server attempts to connect directly to the user’s computer. If the connection is successful, the entire file is sent. If the connection is unsuccessful, an error message is sent to the user. D. The server repeatedly attempts to connect directly to the user’s computer until a connection is made. Once the connection is made, the entire file is sent.
- A: A, not C (The server does not attempt to connect directly to the user’s computer. Rather, packets are sent via routers, and the packets may take different paths to get to the user’s computer. If one packet’s journey to the user is unsuccessful, that packet is resent by the server)

Which of the following is an example of an attack using a rogue access point? A. An unauthorized individual gains the ability to view network traffic by connecting to a network router that uses weak or no security measures. B. An unauthorized individual physically disconnects an exposed network router, making the network unavailable to some users. C. An unauthorized individual poses as a network administrator and attempts to trick a user into providing personal information. D. A group of unauthorized individuals overwhelms a network router with traffic, making it unavailable to some users.
- A: D, not B (While disconnecting a router can be disruptive to users, it does not allow unauthorized individuals to intercept information transmitted on a network)
