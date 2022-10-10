# EC601-Project-2

This project is writing tests programs for twitter API, Botometer, and Google NLP API.

Part 1: Twitter API
The program wrote in Python for this section is lookup tweets using user IDs. The figure below shows the test result.

<img width="866" alt="image" src="https://user-images.githubusercontent.com/77231716/194653361-a96ffd9a-8a43-4061-9fb3-9258b35d40a0.png">

In this test, just one user ID was entered as input, however, the programs allow users enter several IDs at the same time and lookup their user information. The user ID entered is '2244994945'. The result in the terminal shows this account was created at Dec. 14, 2013 (2013-12-14), the account has 543410 followers, 2008 following account, and posted 4029 tweets in total. There are also user description for this account, account profile url, and the time these information was retrieved.

Part 2: Botomter
The mission of this part is writing a test program for botometer. Botometer could help us identify whether the accounts are bot or real person. The testing program allow users enter the screen name or user ID of the account they want to check, several account can be entered at the same time. However, when running this program, there's a error message tells that I'm unauthorized for url of botometer. I tried to work on it for a while, but I'm a beginner in Python and not familiar to botometer and twitter library, so I wasn't able to solve the problem. I found expected results on Github provided by Botomer, which are shown in figure below. The result includes a botscore, the highest value of botscore is 1, when botscore is high, an account is more likely to be a bot, when the bot score is low, the account should be operated by a real people.

<img width="446" alt="image" src="https://user-images.githubusercontent.com/77231716/194673060-138f9de1-5158-40f1-af04-8d0463c2a99e.png">

Part 3: Google NLP
NLP means natural leaguage processing, it can analyze a piece of writing, and output the entities (whether a word is used saliently), sentiment (natural, positive, or negative language), syntax (relationship between words), caregories (the categories of topic). The rquirement of this part is writing a test program for sentiment analysis, but when the program was running, there is a credentials problem. I spent hours to lookup codes, set up the proejct, initialize the Google Cloud CLI, but the initialize process always give me warnings. Since the code doesn't work properly, but literally, the output should be a set of scores for sectences. The sentiment scores are set in a range, for example, -1 to 1. When score is low, the system think a sentence includes negative language, when scores are high, it's more likely to be positive language. After sentiment score, there is a index called sentiment magnitude, which indicate how confident the system believe in the sentiment score. The sentiment magnitude is higher, the system is more confident. The following figure shows an example of sentiment score and sentiment magnitude provided by Google Cloud website.

<img width="656" alt="image" src="https://user-images.githubusercontent.com/77231716/194678477-68bd3f83-58c2-4973-8598-c01fbe66d559.png">


Phase 2 User Story

Social media apps such as Facebook, Instagram, Twitter, and Snapchat are becoming essential in our lives to acquire information, read news, and learn about what's happening around us. Influencer is a powerful role to spread information and bring earnings to social media apps. Many social media operation companies would like to reward influencers who increase the liveness of the platform, and this reward will be based on the number of reads, posts, and followers. To operate the reward mechanism for influencers, social media companies need to have statistics on this information. The mission of this project is to develop a tool to collect the number of reads, posts, and followers of influenciers.
