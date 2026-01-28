# ICPC Club@Amrita NGL ,Automation System

An internal automation platform designed to monitor and encourage daily competitive programming activity for a student club using the Codeforces API.

## Problem
As a club lead, manually tracking daily practice, contest participation, and rating changes across multiple members is time-consuming and error-prone.

## Solution
This system automates:
- Daily activity tracking for all members
- Personalized inactivity reminders
- Upcoming contest alerts
- Post-contest participation and performance tracking
- Weekly performance and rating reports

All tasks run automatically using scheduled background jobs.

## Features
- Fetches real-time data using Codeforces APIs
- Daily practice monitoring with inactivity and streak detection
- Contest reminders before scheduled contests
- Post-contest analysis of registered members:
  - Participation status
  - Rank and number of problems solved
- Weekly performance and rating summary reports
- Cron-based automation (daily & weekly)
- Excel report generation
- Email notifications
- Failure logging and retry-safe design

## Architecture
Scheduled Club Check  
→ Member Activity Fetch  
→ Daily Practice Evaluation  
→ Inactivity & Streak Detection  
→ Contest Awareness & Reminder Engine  
→ Contest Performance Analysis  
→ Performance History Storage  
→ Member Notifications & Weekly Coach Report  

## Tech Stack
- Python, Flask
- SQLite / PostgreSQL
- Linux cron
- Pandas, OpenPyXL
- Docker, Render

## Reliability
- API failures are logged and skipped safely
- Email retries are isolated per user
- Jobs are idempotent to avoid duplicate processing

## Future Enhancements
- WhatsApp notifications via official API
- Admin dashboard for mentors
- Multi-club support
- Advanced contest analytics and trends

## Motivation
Built to solve a real leadership problem and demonstrate automation, backend, and reliability engineering skills through a real-world club management use case.
