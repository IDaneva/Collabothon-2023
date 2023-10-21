# Collabothon-2023
this will be the idea of our team for the Collabothon 2023 #InnovateFinance

Welcome to our idea!

Isn't constantly transferring money to friends and family for shared expenses annoying?
We've been there and we know it is. 
Imagine living with someone and constantly having to track who paid for the dinner last Friday / the electricity for this month / wifi ...etc

You may have heard of family bank accounts but let's be honest... They are restricted.

Why are family accounts only savings ones and not just like regular ones? We actually don't know and that's why we came up with the idea of family accounts accessible from more than one person.

These new family accounts allow incoming and outgoing transfers from different accounts. 
This way you can for example set a rule with your partner to contribute the same amount at the beginning of each month and make the shared expenses from the family account. The whole concept allows you to ditch tracking "who paid for what and how much do I owe you" and make payments a lot easier. Of course, tracking is important and that's why we added filtering not only by categories but also by the person who made the payments.

Let's dive into the steps we had to take in order to get to the point where we are.

1. No solution would be complete without a real DB

  We had to define our models and create an admin panel where the DB could be accessed through
  ![image](https://github.com/IDaneva/Collabothon-2023/assets/101068051/7e5da4af-afae-46c5-91c0-3a122beac0e9)
  of course as we couldn't rely on real data for the transactions and the accounts, we filled up the DB with mock data

2. Then came the hard part - taking the defined DB models and adding the functionality to them. For this step was crucial to create web pages for the bank app. The pages collect the data from the DB, make the necessary calculations and display it

   a page like this is something that you're used to seeing when opening your banking app
![image](https://github.com/IDaneva/Collabothon-2023/assets/101068051/b1f8ddad-e190-4116-84b5-1caaa005ece2)

  our idea lies in the family button. Once clicked you can see the family account that was opened for you and the transactions which were made from and to this family account. The cool part is that you can filter out the transactions by categories and users
  ![image](https://github.com/IDaneva/Collabothon-2023/assets/101068051/95cefd83-6475-4b51-8507-9bdb063d234b)


  of course, sometimes it is necessary to make actual payments to the personal accounts. You can see the member information and account information once you click on the list button 
  ![image](https://github.com/IDaneva/Collabothon-2023/assets/101068051/e4a0ce8a-725d-4751-9343-59c7a3dd7ed2)
  
we worked a bit on the responsiveness of the pages...but prioritized user authentication(still in progress...)

3. And the hardest part :D The presentation... come see it live at the event

