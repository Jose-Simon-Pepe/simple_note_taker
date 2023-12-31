# Simple Note Taker

## What is this?

- A SIMPLE note taker for you to collect your new necessities. 

Simple because it is designed to be used easily and quickly, in addition to assessing availability.

The insight behind this is that, if we improve our capability at taking records, in a usable and maintainable way, we can improve our daily's inputs management, hence we are more capable of effectively carrying out medium to long-term plans and projects.

## Use cases

- Get a "Collector" component in your inbox system
- Take study notes (specially zettelkasten-like notes)
- Check what study pending items you have to study
- ...

## Requeriments:

- To define where you want to save all your notes (Simple Taker is gonna create a git repo up on it)
- To have "Cron" in your system (Cronied, Crond...)
- To have python-crontab

## Features board:

- Take a note from terminal and tag it: DONE
- Make note taker to be iterative: PENDING
  - Select a bunch of topics you want to study to be used a standard session tags
- Search by tag: DONE
- Search by title: PENDING
  - Implement fussy finder
  - Throw filepaths, no filenames
- Timer: PENDING
  - Choose how many time you wanna study
  - Choose sound bell
- Cohesive CLI: PENDING
  - Create a API
  - Create a cli using tmux
- Question taker: PENDING
  - Make questions about topics from terminal
  - Search questions on topics and list it
  - Select a bunch to be resolved in a study session
- Allow to make a note who solves a question: PENDING 
- Create a git repo: PROGRESSING
  - Allow github authentification, or leave it for user
- Create git backup daemon service with cron: DONE
  - Choose backup frequency
- Create installer and setup docu
