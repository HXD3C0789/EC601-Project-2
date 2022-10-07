# EC601-Project-2

This project is writing tests programs for twitter API, Botometer, and Google NLP API.

Part 1: Twitter API
The program wrote in Python for this section is lookup tweets using user IDs. The figure below shows the test result.

<img width="866" alt="image" src="https://user-images.githubusercontent.com/77231716/194653361-a96ffd9a-8a43-4061-9fb3-9258b35d40a0.png">

In this test, just one user ID was entered as input, however, the programs allow users enter several IDs at the same time and lookup their user information. The user ID entered is '2244994945'. The result in the terminal shows this account was created at Dec. 14, 2013 (2013-12-14), the account has 543410 followers, 2008 following account, and posted 4029 tweets in total. There are also user description for this account, account profile url, and the time these information was retrieved.

Part 2: Botomter
The mission of this part is writing a test program for botometer. Botometer could help us identify whether the accounts are bot or real person. The testing program allow users enter the screen name or user ID of the account they want to check, several account can be entered at the same time. However, when running this program, there's a error message tells that I'm unauthorized for url of botometer. I tried to work on it for a while, but I'm a beginner in Python and not familiar to botometer and twitter library, so I wasn't able to solve the problem. I found expected results on Github provided by Botomer, which are shown in figure below. The result includes a botscore, the highest value of botscore is 1, when botscore is high, an account is more likely to be a bot, when the bot score is low, the account should be operated by a real people.
<img width="446" alt="image" src="https://user-images.githubusercontent.com/77231716/194673060-138f9de1-5158-40f1-af04-8d0463c2a99e.png">

Part 3:
