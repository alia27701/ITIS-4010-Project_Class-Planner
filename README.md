# Class Planner

## Overview
This system is a web application of a class planner. It allows students to be more organized by letting them to add in their classes, their assignments for those classes, mark the assignments as completed when they are done with them, and allow them to generate reminders based on the priority of what kind of assignment it is, like a project or an upcoming test to study for, and the due dates/time.

## Architecture Summary

For this system, it follows a 3-tier architecture:
- Frontend
  - HTML (structure)
  - CSS (styling)
  - JavaScript (logic, API calls)
- Backend
  - Python + Flask
- Database
  - MySQL (originally meant for storing the information of the users credentials. Current version uses in-memory storage)
 
## AI Models Used
- ChatGPT: Used for SDLC planning, Requirement Engineering, System & UI design, and Testing Strategies
- Cursor AI: Used for generating backend Flask Code for API routes for authentication, classes, assignments, and reminders.

## AI Engineering Analysis
### Strengths of AI Tools
- Helped SDLC documentation by generating ideas of what to add and making it in a professional format.
- Helped generate different lines of code and also helped explaining what he line of code did instead of manually doing it yourself
### Limitations
- It generated more complex ideas and lines of code that was not understandable at all
- You had to manually correct each line of code that it generated and some of the lines of code could of broken the entire system
### Tradeoffs
- Decided to do a more basic reminder system where you had to manually press a button to generate the reminders rather than having live notifications
- Prioritized a backend that was functional rather than an over-polished frontend
### Prompting Strategies
- Prompted smaller tasks instead of big ones as the smaller ones generated code that was more understanable
## Engineering Reflection
### What you would do differently without AI
- Without AI, the program would of been a lot simplier looking for what I was going for and the functions would of been less advance compared to the AI code.
### What AI improved vs. degraded
- For what AI improved, it made developing the program and planning the SDLC documentation a lot quicker since it would be the one to generate the possible ideas and I would just have to judge them.
- For degraded, AI had more inconsistent ideas with the SDLC and the code where it would either contradict what I was trying to do or end up giving me code that could of broken the system.
## Supporting Context Files

## ChatGPT Conversation
### Here is the full conversation between ChatGPT and I
https://chatgpt.com/share/69f566eb-d92c-83ea-99ad-d0b86e84c409

