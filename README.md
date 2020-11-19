# Anomaly Detection in Bootcamp Curriculum Logs

This project is based on a scenario presented in the e-mail below:

> Hello,

> I have some questions for you that I need answered before the board meeting Thursday morning. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

> 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
> 2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?
> 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
> 4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents?
> 5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
> 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
> 7. Which lessons are least accessed?
> 8. Anything else I should be aware of?

> Thank you,

> Sr. Data Scientist

## Deliverables

• Submit link to GitHub notebook that asks and answers questions - document the work you do to justify findings
• Compose an email with the answers to the questions/your findings, and in the email, include the link to your notebook in GitHub and attach your slide.
• You will not present this, so be sure that the details you need your need your leader to convey/understand are clearly communicated in the email.
• Slide should be like an exec. Summary and be in form to present.
• Continue using best practices of acquire.py, prepare.py, etc.
• No modeling to be done, and no need to split the data into train/validate/test.

## Email Response:

> Sr. Data Scientist, 

> Attached is the single slide covering the most important findings from the analysis of the curriculum logs. I’ll take a moment to answer the questions you had one by one, and then I will summarize the slide so that you can speak to it during the board meeting today. 

> You can review my analysis in detail at the following GitHub page: https://github.com/adam-gomez/code-dependent-students/blob/main/explore_scratchbook.ipynb

> 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

> Within the web development cohorts, the most viewed lesson overall is the “/javascript-i” lesson. I also looked at how the ‘javascript-i’ module as a whole compared to other web development modules. The ‘javascript-i’ module is the most viewed overall. These trends were relatively consistent, in part because overlapping web development cohorts. As one group of students moves away from a module, another group will move into it, and this smooths out the trend.

> For the data science cohorts, the picture was less clear. The ‘1-fundamentals/1.1-intro-to-data-science’ web page had the most views overall, but it was not consistently in the lead over time. There are currently no overlapping data science cohorts. As students move through the curriculum, their interest in sections increase and decrease substantially and this is reflected in the overall trend. 

> The overview pages for different data science modules tended to have the highest views. When I looked at the modules overall. SQL related content was the most accessed. There was a noticeable difference in how much the Darden cohort viewed classification and regression modules compared to previous cohorts. Earlier cohorts were taught regression before classification and have more overall views in regression pages than classification pages. Darden was taught classification before regression and has more overall views in classification pages.

> I’ve included a visualization of this on the bottom left of the attached slide. I think what may be happening here is that Darden students were more confused by the first modeling module than previous cohorts. While Darden viewed the regression module pages less than other cohorts, their overall page views in these initial modeling lessons went up considerably overall. 

> 2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?

> Among web development cohorts, most groups focus on a mix of javascript, java, spring, and html-css. The Kings cohort focused almost entirely on php and laravel related pages. The Sequoia cohort had most of their views on spring related pages. 

> For the data science cohorts, we have no data for Ada. Bayes focused heavily on regression, Curie focused on python, and Darden focused on classification. 

> 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?

> I reviewed all user ids that had less than 100 views during the time window that the cohort was actively being taught. There were no strong apparent trends in which pages they tended to view, but most of the students in this subset were from Sequoia (11 out of 39) and Darden (6 out of 39).

> 4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents?

> The vast majority of the ip addresses associated with our users are in the Texas area, though we do have some visits from more distant locations (and even countries). I sent some of the IP addresses through https://ipremoval.sms.symantec.com/ipr/lookup, and a few of them were labeled with a negative reputation, but this was too time consuming to perform on every IP address. 

> I pivoted to focus more on identifying high activity spikes by resampling the data into 1-minute periods and looking at the number of web pages being viewed during those windows. I identified 6 user ids that had anomalous spikes in their activity, and of those there were 3 web scraping. On average, users have a peak count of about 10 web pages during their most active one minute window. The web scraping users were many multiples higher than the mean. 

> The three web scraping users:

> USER ID 526
> IP: 172.124.70.146
> On December 19th, 2019, at 11:57:53 pm over a period of 20 seconds, this user accessed 186 distinct pages, each accessed only once. 

> USER ID 341
> IP: 204.44.112.76
> On March 3rd, 2019, at 10:52:05 pm over a period of 7 seconds, this user accessed 167 distinct pages, each accessed only once. 

> USER ID 247
> IP: 72.191.33.138
> On August 27th, 2018, at 1:58:04 pm over a period of 74 seconds, this user accessed 57 distinct pages, each accessed one to three times. This user had absolutely zero activity before and after the event.

> Included on the slide is a chart showing high but normal use of our curriculum (top right). Also included is a chart showing web scraping (bottom right). Unlike most of our users, the web scrapers have limited or no activity before and after their sudden spike in activity.

> There was not any information about user-agents in the data, so I could not answer that question. 

> 5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

> There is at least one user (#268) that appears to have been in both programs. They were a part of the Xanadu web development cohort and are currently a part of the Darden data science cohort. 

> When I reviewed the names of the pages that the web development students had accessed, there was a history of many data science pages being accessed. I am unable to say if this is still happening as I struggled to develop a method that could accurately scan all users across time who had at one point accessed pages from a different curriculum than their own and determine if they were still able to do so. With some additional time, I should be able to answer this question more fully. 

> 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 

> Web development alumni tend to view javascript and spring pages. They also have a lot of views on java-i, java-ii, and java-iii. 

> Data science alumni tend to view the overview pages for the different modules in the curriculum. Beyond this they review SQL and classification material. 

> 7. Which lessons are least accessed?

> This is difficult to generalize as there are a considerable number of pages with only a handful of views. Nevertheless, for both data science and web development, appendix pages tended to be viewed infrequently. 

> 8. Anything else I should be aware of?

> The section below covering the slide will be invaluable during the presentation.

> Presentation Notes

> The slide shows four charts. 
> Top left: This shows which five top pages are being accessed by web development students over time. The five top pages were identified through the use of value_counts(). The data was resampled to quarterly periods. Shorter periods had too much variation to be able to read. The sudden drop in all page views on the far right of the graph is not due to a change in the trend. The final quarter of 2020 is not complete, so the last points in the line represent a count of only a portion of the total time period. 
> Bottom left: This shows the trends for the top five modules accessed by data science students over time. The data was resampled to weekly periods. Data science students operate in non-overlapping cohorts. As each part of the curriculum is covered in class, views of the relevant pages increases. Once the class moves on to a different module, views of the previous module’s material decreases. The most important takeaway is in the change to the order of Darden’s curriculum. This resulted in a dramatic increase in views of the classification material. The students may have been more confused during the classification module compared to other cohorts. The first modeling module in the curriculum simultaneously teaches fundamental principles of modeling along with specific algorithms. Based on the trend in the data, I would suggest that the classification algorithms are more difficult to understand than the regression algorithms. Learning the more difficult algorithms at the same time as one learns the fundamental principles of modeling may have been more difficult.
> Top right: This chart shows the activity of the user that has accessed the web pages the most. This user was from the Lassen web development cohort in 2016. They are still actively reviewing the curriculum pages four years later. Notice that their activity is relatively consistent, and even when they have spikes, they are not nearly as large as the spikes that web scrapers have.
> Bottom right: This chart shows the activity that is characteristic of a web scraper. There is little to no activity during most periods and there is an extreme spike in a single period.
> The slide also shows three user ids and their related ip addresses (center)
> These are the three web scrapers that were identified in the analysis.
> User 526 is located in San Antonio, TX
> User 341 is located in Dallas, TX
> User 247 is located in Irving, TX


> Please reach out to me with any questions you may have regarding this analysis.

> Thank you,

> Adam Gomez