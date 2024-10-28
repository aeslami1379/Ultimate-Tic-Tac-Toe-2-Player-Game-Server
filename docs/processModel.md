# Development Process Model - Sprint 1

----
Throughout sprint 1 our team has implemented a process model as follows:
* Initial breakup of activities into modules for each team members contributions:
  * Tyler - User and Session Management implementation
  * Sam - Database module implementation 
  * Arshia - Server API implementation
  * Ashfaq - App Logic implementation
  * Shreyas - HTML Template and construction implementation
* Set up of kanban board for the tracking of each contributor's activity tasks.
* Use of issue tracker to outline any issues a contributor may have, requirements from another contributor needed, missing functionality, etc.
* Held in person team meetings during class time:
  * General discussion on the current status of each team member's module.
  * Any issues or potential issues that have or may arise.
  * Discussion with the professor for clarification on what is required from our project and any issues we could not resolve amongst the team.
  * Code reviews/pull requests merged during meetings.
  * Held 2 scheduled meetings with the professor.
  * meeting notes documented in MeetingNotes.md.
  * Scrum master and note taker rotated between meetings.
* Code Reviews:
  * All contributor branches of the project were put through a code review before merging into the main project branch.
  * Each review was done by following the checklist in the pr_checklist.md file. 
  * A general comment was provided on each code review detailing any prevailing minor issues or fixes required. 
  * If the issue was more than an update to documentation, a minor change to a unittest or a change to one line of code, the code was not merged.
* Performance reviews were conducted for each team member by each team member, ahead of the end of sprint 1, these are found in the docs\performanceReviews directory.
* Potential changes to our process in sprint 2:
  * Based off our experience of the process followed in sprint 1, and performance reviews from each team member, we may make some changes to our process going forward.
  * We may conduct our team meetings via discord for the most part in the future, meeting in person if we have a question or schedule a meeting with the professor.
  * This should help streamline our code reviews and pull request to avoid implementation bottlenecks, as well as team communication, something we struggled with in sprint 1.


# Development Process Model - Sprint 2

----
Our process has remained generally the same throughout sprint 2.
* Some of the changes made throughout sprint 2 were:
  * The workload of each individual was not solely focused on particular module. The main focus in this sprint was in the HTML Templating Module and serverAPI module.
  * Each person did tend to their own module, when an issue was identified that pertained to that module but overall each team member worked together to solve these issues.
* kanban board/issue tracker:
  * The kanban board was expanded during this sprint to include a backlog.
  * The issue tracker was used for any and every issue regarding our project, code, documentation, implementation requirements, meetings, etc. were all tracked.
  * In sprint 2 we decided to create our branches through the issue tracker, assigning a branch to an issue. This simplified the pull request process and was able to keep conflicts when merging at a minimum.
* Team meetings:
  * Throughout sprint 2 we decided to move our meetings to mainly online discord meetings, as well as in class meetings.
  * The online meetings allowed us to share our screens with the entire team and generally get a better understanding of code reviews, issues, etc.
  * Our in class meetings typically revolved around scheduled meetings with Dr. Brown to discuss any questions about implementation/documentation.
  * The content of our meetings generally revolved around code reviews and were scheduled when all team members were available.
  * A typical online meeting involved:
    * Identifying the note taker and scrum master for the current meeting.
    * General discussion of current state of our project.
    * Any new issues identified between meetings.
    * We would then move to code reviews.
    * As each code review was completed we would then merge the branch the team member was working on, fixing any conflicts together as a group.
    * Any issues related to the pull request were then closed.
    * Identifying the next set of tasks for each team member, creating new issues for the next steps of our implementation.
    * Reviewing the current state of the kanban board and issue tracker.
    * Pushing the meeting notes for the current meeting. 
* Code Reviews:
  * Code reviews were only held when all team members were available, and as we only met when everyone was available this was not an issue.
  * Before a pull request was made, the code submitting team member would do the following:
    * Share their screen.
    * Walk through any changes to previously implemented code that could affect another team members module, this would lead to an issue being created. 
    * Walk through newly implemented features of their module, ensuring all team members understand the new functionality.
    * Demonstrate all unittests are working, and the use of correct docstrings.
    * If new features could be immediately shown in game, a demonstration of the features working while playing. 
    * Making a pull request, and whoever is leading the code review would merge the PR.
    * If any conflicts with the merge, the reviewer would share their screen and fix them as a group, ensuring that the conflicts resolved properly.
    * The reviewer would then update our [Code Review Entries](CodeReviewEntries.md), with an entry pertaining to that specific review.
    * Generally we followed our [Code Review Checklist](pr_checklist.md)
* Performance Reviews:
  * At the end of our sprint each team member submitted their own updated performance reviews for each team member, along with some general commentary about the overall performance of the group throughout the sprint.
  * These can be found in our [Performance Reviews](performance_reviews_sprint2) directory.
* Backlog:
  * At the beginning of sprint 2, we incorporated a backlog to our kanban board.
  * The backlog contains future functionality that could be implemented in our tic-tac-toe game.
  * Each team member was required to make at least one card each in the backlog, and if any extra possible features were thought of during the sprint, they were to be added as well.
* Issues:
  * Creation of issues was generally sporadic throughout the sprint, if someone found something outside a meeting that required an issue they would create one.
  * The creator of the issue would either assign themselves, or if the issue pertained to something in someone else's module the person in charge of that module would be assigned.
  * We also tried to create at least a few issues at the beginning of our team meetings, this helped the team understand who was working on what at any specific time.
  * The closing of issues was mainly done in team meetings, usually after a code review was completed.
  * However, small issues regarding documentation or issues pertaining to the specific meeting may have been closed outside.
  * Issues created by a team member which were assigned to themselves were typically closed outside team meetings.
* Documentation:
  * We decided that the majority of documentation should be done at the end of the sprint, letting us focus on the core functionality of the game for the majority of the sprint.
  * However, coding standards(PEP 8 & PEP 257) were to be updated whenever new functionality was added.
  * Each team member worked on their individual documentation for their assigned task, including: 
    * Arch UML Diagram.
    * Framework proposal document for their module.
    * Performance Reviews.
    * A user story.
  * Things that required the entire teams attention, such as the overall Arch UML Diagram for the project, the video/user manual, the overall framework proposal document, and the README were some of the last things updated.
* Timing:
  * Code Reviews/Meetings/Pull Requests
    * Code Reviews were done based on the availability of team members, ensuring everyone was in attendance.
    * Meetings were done in the same fashion, we tried to meet at minimum twice a week online and at least once in class.
    * Pull Requests were only done during team meetings, so once again these followed the same fashion.
  * Sprint Deadlines:
    * Once individuals understood their next task in a meeting, we generally set a deadline for the implementation of the feature to the following meeting, occasionally setting it for a couple of meetings down the line.
    * We set a code related final deadline of Friday, April 5th.
    * The Same was done for documentation related items. 

We were able to follow this description of our process model fairly easily. Occasionally a team member would go outside of this and push a very minor change to the master branch without a review being done. But, this was usually for general cleanup, a one line code adjustment that had no impact on the other modules. We felt things like this were not necessary for a full team review and we each trusted each other to the point were this worked fine. Documentation was usually just pushed directly to the main branch without a pull request being made, but any issues were closed pertaining to that documentation. Our meetings generally aligned with our goal of meeting 2-3 times per week, occasionally this was not possible due to work schedules, conflicts with other classes, etc. But for the most part we were pretty consistent. Overall, we did a great job of keeping in line with our process model, and incorporating new pieces to the model to improve our performance from sprint 1 to sprint 2 definitely created a better and more effective work environment amongst the team.